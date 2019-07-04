# Structjour -- a daily trade review helper
# Copyright (C) 2019 Zero Substance Trading
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
'''
Re-implementing the ib statement stuff to get a general solution that can be stored in a db
@author: Mike Petersen
@creation_data: 06/15/19
'''

import os
import urllib.request

import pandas as pd
from bs4 import BeautifulSoup

from journal.dfutil import DataFrameUtil
from journal.statements.findfiles import getDirectory, findFilesSinceMonth
from journal.statements.ibstatementdb import StatementDB

# pylint: disable = C0103


def readit(url):
    '''Copied this from statement.py. I think this will be its home-- '''
    data = ''
    if url.lower().startswith('http:'):
        data = urllib.request.urlopen(url).read()
    else:
        assert os.path.exists(url)
        with open(url) as f:
            data = f.read()
    return data



class IbStatement:
    '''
    Hold the column names for tables in Flex Queries. The names are a subset of the possible
    columns.
    '''

    # Not sure there is a difference between T_FLEX and TRADE
    # Going to attempt to treat CSV and Html version of activity statements the same once
    # the initial dataframes are created. For the subset of 3-4 tables we view, should be possible.
    I_TYPES = ["A_FLEX", "T_FLEX", "ACTIVITY", "TRADE"]
    def __init__(self):

        self.account = None
        self.statementname = None
        self.beginDate = None
        self.endDate = None
        self.inputType = None
        self.broker = None

    def parseTitle(self, t):
        '''
        The html title tag of the activity statement contains statement info. There are no specs to
        the structure of the thing. So on failure, raise exceptions.
        '''
        result = t.split('-')
        if len(result) == 2:

            t = result[0]
            broker = result[1].strip()
        elif len(result) == 3:
            t = result[0]
            endDate = result[1].strip()
            broker = result[2].strip()
            try:
                self.endDate = pd.Timestamp(endDate).date()
            except ValueError:
                raise ValueError('Failed to parse the statement date')
            

        # broker = broker.strip()
        self.broker = broker
        t = t.strip()
        t = t.split(' ')

        # The different lengths accout for Statement titles with different numbers of words, 1,
        # 2, or 3
        if len(t) == 7:
            account = t[0]
            sname = ''.join([t[1], t[2], t[3]])
            theDate = ' '.join([t[4], t[5], t[6]])
        elif len(t) == 6:
            account = t[0]
            sname = ' '.join([t[1], t[2]])
            theDate = ' '.join([t[3], t[4], t[5]])
        elif len(t) == 5:
            account = t[0]
            sname = t[1]
            theDate = ' '.join([t[2], t[3], t[4]])
        else:
            raise ValueError('Failed to parse the statement date')

        try:

            self.beginDate = pd.Timestamp(theDate).date()
            self.account = account
            self.statementname = sname

        except:
            raise ValueError('Failed to parse the statement date')

    def combinePartialsHtml(self, df):
        '''
        Combine the partial entries in a trades table. The Html refers to the origin of the table.
        This is a table without a DataDiscriminator or LevelOfDetail column. The Partials were
        identified in html with classes and the user identifies them with expanding thingys. So
        woopdy do for that. The discriminator now is equal[DateTime, Codes, Symbol](Codes must
        include a P). The first of the bunch has the summary Quantity, 'the rest' add to the first.
        Filter out 'the rest.'
        '''
        newdf = pd.DataFrame()
        hasPartials = False
        tickers = df['Symbol'].unique()
        for tickerKey in tickers:
            if tickerKey.lower().startswith('closed') or tickerKey.lower().startswith('wash sale'):
                hasPartials = True
        if not hasPartials:
            return df

        for tickerKey in df['Symbol'].unique():
            ticker = df[df['Symbol'] == tickerKey]
            if len(tickerKey) > 6:
                # This is probably not a ticker assert to verify
                for code in ticker['Codes'].unique():
                    assert code.find('O') == -1
                    assert code.find('C') == -1
                    assert code.find('P') == -1
                continue

            codes = ticker['Codes'].unique()
            for code in codes:
                parts = ticker[ticker['Codes'] == code]
                if code.find('P') > -1:
                    if len(parts) == 1:
                        pass

                    else:
                        # print()
                        addme = []
                        curTotal = 0

                        for count, (i, row) in enumerate(parts.iterrows()):
                            share = int(row['Quantity'])
                            if curTotal == 0:
                                curTotal = share
                                addme.append(count)
                            else:
                                curTotal = curTotal - share
                        assert curTotal == 0
                        x = 3
                        for x in addme:
                            newdf = newdf.append(parts.iloc[x])
                else:
                    newdf = newdf.append(parts)

        return newdf

    def doctorHtmlTables(self, tabd):
        '''
        Fix the idiosyncracies in the tables from an html IB Statement
        '''
        keys = list(tabd.keys())
        for key in keys:
            if key not in  ['AccountInformation', 'OpenPositions', 'Transactions',
                            'Trades', 'LongOpenPositions', 'ShortOpenPositions']:
                raise ValueError('Unknown table needs to be examined')
            if key in ['OpenPositions', 'Transactions', 'Trades', 'LongOpenPositions',
                       'ShortOpenPositions']:
                df = tabd[key]
                df = df[df['Symbol'].str.startswith('Total') == False]
                df = df.iloc[2:]
                # Using 'tbl' prefix to identify the html specific table
                ourcols = self.getColsByTabid('tbl' + key)
                if ourcols:
                    ourcols, missingcols = self.verifyAvailableCols(list(df.columns), ourcols,
                                                                    'tbl' + key)
                    df = df[ourcols]
                if key == 'Trades':
                    df = df.rename(columns={'Acct ID': 'Account', 'Trade Date/Time': 'DateTime',
                                            'Comm': 'Commission'})
                    df = self.unifyDateFormat(df)
                if key == 'Transactions':
                    df = df.rename(columns={'Date/Time': 'DateTime', 'T. Price': 'Price',
                                            'Comm/Fee': 'Commission', 'Code': 'Codes'})

                    df['Account'] = self.account
                    df = self.combinePartialsHtml(df)
                    df = self.unifyDateFormat(df)
                tabd[key] = df.copy()

            elif key == 'AccountInformation':
                tabd[key].columns = ['Field Name', 'Field Value']

            if key in ['LongOpenPositions', 'ShortOpenPositions']:
                t = tabd[key]

                t = tabd[key][tabd[key]['Mult'] == '1']

                if 'OpenPositions' in tabd.keys():
                    tabd['OpenPositions'] = tabd['OpenPositions'].append(t)
                else:
                    tabd['OpenPositions'] = t.copy()
                del tabd[key]
        return tabd

    def openIBStatementHtml(self, infile):
        '''
        Open an IB Statement in html form
        '''
        if not os.path.exists(infile):
            return
        soup = BeautifulSoup(readit(infile), 'html.parser')
        tbldivs = soup.find_all("div", id=lambda x: x and x.startswith('tbl'))
        title = soup.find('title').text
        self.parseTitle(title)
        tables = dict()
        tablenames = dict()
        for tableTag in tbldivs:
            continueit = True
            tabKey = ''
            for key in ['tblAccountInformation', 'tblOpenPositions', 'tblLongOpenPositions',
                        'tblShortOpenPositions', 'tblTransactions', 'tblTrades']:
                if tableTag['id'].startswith(key):
                    continueit = False
                    tabKey = key[3:]
                    break
            if continueit:
                continue

            tab = tableTag.find("table")
            if not tab:
                continue
            df = pd.read_html(str(tab))
            assert len(df) == 1
            df = df[0]  # .replace(np.nan, '')
            tables[tabKey] = df
        if 'Transactions' not in tables.keys() and 'Trades' not in tables.keys():
            # This should maybe be a dialog
            msg = 'The statment lacks a trades table; it has no information of interest.'
            print(msg)
            return dict(), dict()
        self.doctorHtmlTables(tables)
        tname = ''
        if 'Trades' in tables.keys():
            tname = 'Trades'
        elif 'Transactions' in tables.keys():
            tname = 'Transactions'

        if tname:
            ibdb = StatementDB()
            ibdb.processStatement(tables[tname], self.account, self.beginDate, self.endDate)
        else:
            raise ValueError('This code should not have come here')
        for key in tables:
            tablenames[key] = key
        tablenames[tabKey] = tabKey
        return tables, tablenames

    def openIBStatement(self, infile):
        '''
        Open an IB Statement in either csv or html form
        '''
        if os.path.splitext(infile)[1] == '.csv':
            return self.openIBStatementCSV(infile)
        elif os.path.splitext(infile)[1] == '.html':
            return self.openIBStatementHtml(infile)
        else:
            print('Only htm or csv files are recognized')

    def openIBStatementCSV(self, infile):
        '''
        Identify a csv file as a type of IB Statement and send to the right place to open it
        '''
        df = pd.read_csv(infile, names=[x for x in range(0, 100)])
        df = df
        if df.iloc[0][0] == 'BOF'  or df.iloc[0][0] == 'HEADER':
            # This is a flex activity statement with multiple tables
            self.inputType = "A_FLEX"
            return self.openActivityFlexCSV(df)

        elif df.iloc[0][0] == 'ClientAccountID':
            return self.openTradeFlexCSV(infile)

        elif df.iloc[0][0] == 'Statement':
            # This is a multi table statement like a default statement
            self.inputType = 'ACTIVITY'
            return self.getTablesFromDefaultStatement(df)
        return dict(), dict()

    def unifyDateFormat(self, df):
        '''
        Ib sends back differnt formats from different files. All statement processing should call
        this method.
        '''
        df['DateTime'] = df['DateTime'].str.replace('-', '').str.replace(
            ':', '').str.replace(',', ';').str.replace(' ', '')
        if df.any()[0]:
            assert len(df.iloc[0]['DateTime']) == 15
        return df

    def parseDefaultCSVPeriod(self, period):
        '''
        The printed perod at the top of the staement comes in at least 3 formats. I have found no
        specs. If this fails, the program will set covered dates by the min and max trade dates.
        '''
        try:
            test = period.split('-')
            if len(test) == 1:
                # Expecting a full date like January 25, 2019
                self.beginDate = pd.Timestamp(period).date()
            elif len(test) == 3:
                # Expecting 14-Jun-9 or 2019-01-03
                self.beginDate = pd.Timestamp(period).date()
            else:
                # Expecting a range like January 1, 2019 - January 31, 2019
                self.beginDate = test[0].strip()
                self.endDate = test[1].strip()
                self.beginDate = pd.Timestamp(self.beginDate).date()
                self.endDate = pd.Timestamp(self.endDate).date()
        except ValueError:
            msg = f'Failed to parse the statement date period: {period}'
            print(msg)

    def doctorDefaultCSVStatement(self, tables, mcd):
        '''
        Fix up the idiosyncracies in the tables from a default csv statement'''
        # for key in tables:
        if 'Statement' in tables.keys():
            t = tables['Statement']
            self.broker = t[t['Field Name'] == 'BrokerName']['Field Value'].unique()[0]
            self.statementname = t[t['Field Name'] == 'Title']['Field Value'].unique()[0]
            period = t[t['Field Name'] == 'Period']['Field Value'].unique()[0]
            self.parseDefaultCSVPeriod(period)
            tables['Statement'] = t

        if 'AccountInformation' in tables.keys():
            self.account = tables['AccountInformation'].iloc[1][1]

        if 'OpenPositions' in tables.keys():
            d = self.endDate if self.endDate else self.beginDate
            tables['OpenPositions']['Date'] = d.strftime('%Y%m%d')
            if 'ClientAccountID' in mcd['OpenPositions']:
                if self.account:
                    tables['OpenPositions']['Account'] = self.account
            else:
                tables['OpenPositions'] = tables['OpenPositions'].rename(
                    columns={'ClientAccountID': 'Account'})
        if 'Trades' in tables.keys():
            t = tables['Trades']
            if 'order' in t['DataDiscriminator'].str.lower().unique():
                t = t[t['DataDiscriminator'].str.lower() == 'order']
            elif 'execution' in t['DataDiscriminator'].str.lower():
                # TODO
                raise ValueError('Need to implement combine partials for the default statement')
            elif 'trade' in t['DataDiscriminator'].str.lower():
                raise ValueError('Need to either implement a cludge or disable the statement')
            t = t.rename(columns={'T. Price': 'Price', 'Comm/Fee': 'Commission'})
            t['Account'] = self.account
            t = t.drop('DataDiscriminator', axis=1)
            t = t.rename(columns={'Code': 'Codes', 'Date/Time': 'DateTime'})
            t = self.unifyDateFormat(t)
            tables['Trades'] = t
        return tables

    def getTablesFromDefaultStatement(self, df):
        '''
        From a default Activity statement csv, retrieve AccountInformation, OpenPositions, and
        Trades
        '''
        # df = pd.read_csv(infile, header=range(0,15))
        keys = df[0].unique()
        tables = dict()
        tablenames = dict()
        mcd = dict()
        for key in keys:
            if key not in ['Statement', 'Account Information', 'Open Positions',
                           'Short Open Positions', 'Long Open Positions', 'Trades']:
                continue

            t = df[df[0] == key]
            headers = t[t[1].str.lower() == 'header']
            if len(headers) > 1:
                msg = '\nMulti account statment not supported.'
                return dict(), msg
            assert t.iloc[0][1].lower() == 'header'
            currentcols = list(t.columns)
            headers = headers.iloc[0]
            t = t[t[1].str.lower() == 'data']
            assert len(currentcols) == len(headers)
            t.columns = headers
            ourcols = self.getColsByTabid(key)
            ourcols, missingcols = self.verifyAvailableCols(headers, ourcols, key)
            if not ourcols:
                continue
            t = t[ourcols]

            if key in ['Long Open Positions', 'Short Open Positions']:
                t = t[t['DataDiscriminator'].str.lower() == 'summary']
                key = 'OpenPositions'
                ourcols = self.getColsByTabid(key)
                if ourcols:
                    ourcols, missingcols = self.verifyAvailableCols(
                        list(t.columns), ourcols, key)
                    t = t[ourcols].copy()

                if 'OpenPositions' in tables.keys():
                    if not set(tables['OpenPositions'].columns) == set(t.columns):
                        msg = 'A Programmer thing-- see it occur before I write code'
                        raise ValueError(msg)

                    tables['OpenPositions'] = tables['OpenPositions'].append(t)
                    tablenames['OpenPositions'] = 'OpenPositions'
                    continue
                else:
                    key = 'OpenPositions'

            key = key.replace(' ', '')
            mcd[key] = missingcols
            tables[key] = t
            tablenames[key] = key
        tables = self.doctorDefaultCSVStatement(tables, mcd)

        if 'Trades' not in tables.keys():
            # This should maybe be a dialog
            msg = 'The statment lacks a trades table'
            return dict(), msg

        if self.account is None:
            msg = '''This statement lacks an account number. Can't add it to the database'''
            return dict(), msg
        ibdb = StatementDB()
        openpos = None
        if 'OpenPositions' in tables.keys():
            openpos = tables['OpenPositions']
        ibdb.processStatement(tables['Trades'], self.account, self.beginDate, self.endDate, openpos)
        return tables, tablenames

    def combinePartialsFlexTrade(self, t):
        '''
        The necessity of a new method to handle this is annoying...BUT gdmit, The Open/Close info
        is not in any of the available fields. Instead, a less rigorous system is used based on
        OrderID
        '''
        lod = t['LevelOfDetail'].unique()
        if len(lod) > 1:
            assert ValueError('I need to see this')
        if lod[0].lower() != 'execution':
            assert ValueError('I need to see this')

        t = t[t['LevelOfDetail'].str.lower() == 'execution']
        newdf = pd.DataFrame()
        for tickerKey in t['Symbol'].unique():
            ticker = t[t['Symbol'] == tickerKey]
            # ##### New Code
            ticketKeys = ticker['OrderID'].unique()
            for ticketKey in ticketKeys:
                ticket = ticker[ticker['OrderID'] == ticketKey]
                if len(ticket) > 1:
                    codes = ticket['Codes']
                    for code in codes:
                        assert code.find('P') > -1

                    thisticket = DataFrameUtil.createDf(ticket.columns, 1)
                    net = 0.0
                    # Need to figure the average price of the transactions and sum of quantity
                    # and commission
                    for i, row in ticket.iterrows():
                        net = net + (float(row['Price']) * int(row['Quantity']))
                    for col in list(thisticket.columns):
                        if col not in ['Quantity', 'Price', 'Commission']:
                            thisticket[col] = ticket[col].unique()[0]
                    thisticket['Quantity'] = ticket['Quantity'].map(int).sum()
                    thisticket['Commission'] = ticket['Commission'].map(float).sum()
                    thisticket['Price'] = net / ticket['Quantity'].map(int).sum()
                    newdf = newdf.append(thisticket)

                else:
                    newdf = newdf.append(ticket)
        return newdf

    def openTradeFlexCSV(self, infile):
        '''
        Open a Trade flex statement csv file. This is a single table file. The headers are in the
        top row so just reading it with read_csv will collect them. This table is missing the
        Open/Close data.
        '''
        df = pd.read_csv(infile)
        self.inputType = 'T_FLEX'

        # This one table file has no tableid
        currentcols = list(df.columns)
        ourcols = self.getColsByTabid('FlexTrades')
        ourcols, missingcols = self.verifyAvailableCols(currentcols, ourcols, 'DailyTrades')
        df = df[ourcols].copy()
        df = df.rename(columns={'Date/Time': 'DateTime', 'Code': 'Codes',
                                'ClientAccountID': 'Account'})

        lod = df['LevelOfDetail'].str.lower().unique()
        if 'order' in lod:
            pass
        elif 'execution' in lod:
            if 'OrderID' in missingcols:
                msg = 'This table contains transaction level data but lacks OrderID.'
                return dict(), msg
            else:
                # df = df.rename(columns={'OrderID': 'IBOrderID'})
                df = self.combinePartialsFlexTrade(df)
        else:
            # TODO 2019-07-03 if this never trips, blitz the statmement for just in case
            raise ValueError("If this trips, detemine if the data is savlagable")
        if len(df) < 1:
            msg = 'This statement has no trades.'
            return dict(), msg

        # The Codes col acks the OpenClose codes so were done with it.
        df = df.drop(['LevelOfDetail', 'Codes'], axis=1)
        df = self.unifyDateFormat(df)
        self.account = df['Account'].unique()[0]

        beg = df['DateTime'].min()
        end = df['DateTime'].max()
        assert beg
        assert end
        try:
            self.beginDate = pd.Timestamp(beg).date()
            self.endDate = pd.Timestamp(end).date()
        except ValueError:
            msg = f'Unknown date format error: {beg}, {end}'
            return dict(), msg

        ibdb = StatementDB()
        ibdb.processStatement(df, self.account, self.beginDate, self.endDate)

        return {'Trades': df}, {'Trades': 'Trades'}

    def combinePartials(self, t):
        '''
        In flex Statements, the TRNT (Trades) table input might be in transacations instead of
        tickets identified by LevelOfDetail=EXECUTION without the summary rows identified by
        LevelOfDetail=ORDERS. This is fixable (in both Activity statements and Trade statements)
        by changing Options to inclue Orders. If we have Executions only, we need to recombine
        the partials as identified by IBOrderID. If we also lack that column, blitz the sucker.
        Its not that hard to get a new statment
        :t: Is a TRNT DataFrame. That is a Trades table from a CSV multi table doc in which TRNT
                 is the tableid.
        :assert: Tickets written at the exact same time are partials, identified by
                 Notes/Codes == P (change name to Codes) and by having a single Symbol
        :prerequisite: Must have the columns
                        ['Price', 'Commission', 'Quantity', 'LevelOfDetail', 'Codes']
        '''
        lod = t['LevelOfDetail'].unique()
        if len(lod) > 1:
            assert ValueError('I need to see this')
        if lod[0].lower() != 'execution':
            assert ValueError('I need to see this')

        t = t[t['LevelOfDetail'].str.lower() == 'execution']
        newdf = pd.DataFrame()
        for tickerKey in t['Symbol'].unique():
            ticker = t[t['Symbol'] == tickerKey]
            ##### New Code
            codes = ticker['Codes'].unique()
            for code in codes:
                if isinstance(code, float):
                # if math.isnan(code):
                    continue
                parts = ticker[ticker['Codes'] == code]
                ticketKeys = parts['IBOrderID'].unique()
                for ticketKey in ticketKeys:
                    ticket = parts[parts['IBOrderID'] == ticketKey]
                    if len(ticket) > 1:
                        thisticket = DataFrameUtil.createDf(ticket.columns, 1)
                        net = 0.0
                        # Need to figure the average price of the transactions and sum of
                        # quantity and commission
                        for i, row in ticket.iterrows():
                            net = net + (float(row['Price']) * int(row['Quantity']))
                        for col in list(thisticket.columns):
                            if col not in ['Quantity', 'Price', 'Commission']:
                                thisticket[col] = ticket[col].unique()[0]
                        thisticket['Quantity'] = ticket['Quantity'].map(int).sum()
                        thisticket['Commission'] = ticket['Commission'].map(float).sum()
                        thisticket['Price'] = net / ticket['Quantity'].map(int).sum()
                        newdf = newdf.append(thisticket)

                    else:
                        newdf = newdf.append(ticket)
        return newdf

    def doctorActivityFlexTrades(self, t, missingcols):
        '''
        Deal with idiosyncracies;
        set uniform format in the Activity Flex Trades table (tableid = TRNT)
            1) Some statements' TRNT table include TradeDate and TradeTime seperately. Others may
               have the combined DateTime. And, maybe, some statements use Date/Time
            2) The missing possibly required fields are provided in missingcols
            3) Combine Open/CloseIndicator and Notes/Codes into Codes-- required if we need to
               combine partials
            4) LevelOfDetail may include ORDER and/or  EXECTION. We want the ORDER info but if
               we have only EXECUTION, combine the partials. One or the other is required.
            5) Set uniform columns names and date format.
        '''
        # 1
        if 'Date/Time' in t.columns:
            raise ValueError('wtf ib!?!, Maybe you should hire me to do this stuff.')
            # t = t.rename(columns={'Date/Time': 'DateTime'})
        elif 'DateTime' in t.columns:
            pass
        elif 'TradeDate' and 'TradeTime' in t.columns:
            t['DateTime'] = t['TradeDate'].map(str) + ';' + t['TradeTime']
            t = t.drop(['TradeDate', 'TradeTime'], axis=1)
        else:
            msg = '\n'.join(['''This Activity Flex statement is missing order'
                               'time information. Please include the',
                               'Date/Time' column or ['TradeDate','TradeTime'] columns. '''])
            self.beginDate = None
            return pd.DataFrame(), msg

        # 2
        missingcols = set(missingcols) - set(['TradeDate', 'TradeTime', 'DateTime', 'Date/Time',
                                              'IBOrderID'])
        if missingcols:
            msg = f'Statment is missing cols: {list(missingcols)}'
            return pd.DataFrame, msg
        # 5
        t = t.rename(columns={'TradePrice': 'Price', 'IBCommission': 'Commission',
                              'ClientAccountID': 'Account'})

        # 3
        t['Codes'] = ''
        for i, row in t.iterrows():
            OC = row['Open/CloseIndicator']
            P = row['Notes/Codes']
            if isinstance(OC, float):
                OC = ''
            if isinstance(P, str):
                if (OC.find('O') > -1 and P.find('O') > -1) or (
                        OC.find('C') > -1 and P.find('C') > -1):
                    codes = P
                else:
                    codes = f'{OC};{P}'
            else:
                codes = OC
            t.at[i, 'Codes'] = codes
        t = t.drop(['Open/CloseIndicator', 'Notes/Codes'], axis=1)

        # 4
        # lod =  list(t['LevelOfDetail'].unique())
        lod = [x.lower() for x in list((t['LevelOfDetail'].unique()))]
        if 'order' in lod:
            t = t[t['LevelOfDetail'].str.lower() == 'order']
        elif 'execution' in lod:
            if not 'IBOrderID' in t.columns:
                self.beginDate = None
                msg = '\n'.join(['This Activity Flex statement Includes EXECUTION level data'
                                 '(aka partials) To combine the partial executions',
                                 'into readable trades, the column "IBOrderID" must be included'
                                 'in the Flex Query Trades table. Alternately,',
                                 'select the Orders Options.'])
                return pd.DataFrame(), msg

            t = t[t['LevelOfDetail'].str.lower() == 'execution']
            t = self.combinePartials(t)
        elif len(t) > 0:
            msg = '\n'.join(['This Activity Flex statement is missing partial execution data.'
                             'Please include the Orders or Execution Options for',
                             'the Trades Table in your Activity flex statement. '])
            return pd.DataFrame(), msg

        t = self.unifyDateFormat(t)
        dcolumns, mcolumns = self.verifyAvailableCols(
            list(t.columns), ['LevelOfDetail', 'IBOrderID', 'TradeDate'], 'utility')
        t = t.drop(dcolumns, axis=1)
        return t, ''

    def getFrame(self, fid, df):
        '''
        Retrieve the rows between (fid[0], fid[1]) in df
        :fid: A section identifier like ('BOF', 'EOF')
        '''
        x = df[df[0] == fid[0]]
        metadata = []
        ldf = []
        for i in range(0, len(x)):
            started = False
            # newdf = pd.DataFrame()
            data = []

            for j, row in df.iterrows():
                if row[0] == fid[0] and not started:
                    md = [x for x in row if isinstance(x, str)]
                    metadata.append(md)
                    started = True
                    continue
                elif started and row[0] != fid[1]:
                    data.append(row.values)
                    # newdf = newdf.append(row)
                elif started:
                    newdf = pd.DataFrame(data=data, columns=df.columns)
                    ldf.append(newdf)
                    break
        return ldf, metadata

    def doctorFlexTables(self, tables, mcd):
        '''
        Fix up the idiosyncracies in the tables in from an Activity Flex Statement
        '''
        if 'TRNT' in tables.keys():
            missingcols = mcd['TRNT']
            tables['TRNT'], m = self.doctorActivityFlexTrades(tables['TRNT'], missingcols)
            # A statement with no trades and a beginDate can update the ib_covered table. But w/o
            # the date or Trades, this statement has no use.
            if tables['TRNT'].empty and not self.beginDate:
                m = m + '\nThis statement has no trades and no begin or end date.'
                return dict(), m
        if 'ACCT' in tables.keys():
            tables['ACCT'] = tables['ACCT'].rename(columns={'ClientAccountID': 'Account'})
            self.account = tables['ACCT']['Account'].values[0]
        if 'POST' in tables.keys():
            # If the statement lacks date metadata, the next best thing is the the first and last
            # dates for trades
            d = self.endDate if self.endDate else self.beginDate if self.beginDate else None
            if d is None:
                # Bit of a catch 22 in the processing produces unsure  ???
                if 'TRNT' in tables.keys():
                    beginDate = tables['TRNT']['DateTime'].min()
                    endDate = tables['TRNT']['DateTime'].max()

            tables['POST']['Date'] = d.strftime('%Y%m%d')
            tables['POST'] = tables['POST'].rename(columns={'ClientAccountID': 'Account'})
        return tables, ''

    def openActivityFlexCSV(self, df):
        '''
        This will process a flex activity statement with headers and with or without  metadata. The
        metadata rows are itendified with BOF BOA BOS columns.
        Setting up to process multiple accounts but the table names are still messed up
        Raise error if multiple accounts are sent in for now
        '''

        tables = dict()
        tablenames = dict()
        mcd = dict()
        accounts = []
        ldf, filemetadata = self.getFrame(('BOF', 'EOF'), df)
        accountsmetadata = []
        if ldf and isinstance(ldf[0], pd.DataFrame):
            accounts, accountsmetadata = self.getFrame(('BOA', 'EOA'), ldf[0])
            if len(accounts) > 1:
                raise ValueError('Multiple accounts is not enabled for Ib Statement parsing')
            filemetadata = filemetadata[0]
            accountsmetadata = accountsmetadata[0]
        else:
            accounts.append(df)
        for dfa in accounts:
            if filemetadata:
                # self.account = filemetadata[1]
                self.statementname = filemetadata[2]
                beginDate = filemetadata[4]
                self.beginDate = pd.Timestamp(beginDate).date()
                endDate = filemetadata[5]
                self.endDate = pd.Timestamp(endDate).date()
            if accountsmetadata:
                self.account = accountsmetadata[1]

            tabids = dfa[1].unique()
            for tabid in tabids:
                t = dfa[dfa[1] == tabid]
                if 'BOS' in t[0].unique():
                    tab, tabmetadata = self.getFrame(('BOS', 'EOS'), t)
                    assert len(tab) == 1
                    assert len(tabmetadata) == 1
                    t = tab[0]
                    tabmetadata = tabmetadata[0]
                currentcols = list(t.columns)
                headers = list(t[t[0] == 'HEADER'].iloc[0])
                t = t[t[0] == 'DATA']
                assert len(currentcols) == len(headers)
                t.columns = headers
                ourcols = self.getColsByTabid(tabid)
                ourcols, missingcols = self.verifyAvailableCols(headers, ourcols, tabid)
                if not  ourcols:
                    continue
                t = t[ourcols]
                mcd[tabid] = missingcols

                # Assign to dict and return
                tables[tabid] = t.copy()
                tablenames[tabid] = tabid
            tables, msg = self.doctorFlexTables(tables, mcd)
            if not len(tables.keys()):
                # TODO When enabling multi accounts-- fix this to not return
                return tables, msg
            ibdb = StatementDB()
            positions = None
            if 'POST' in tables.keys():
                positions = tables['POST']
            ibdb.processStatement(tables['TRNT'], self.account, self.beginDate, self.endDate,
                                  positions)
        return tables, tablenames

    def getColsByTabid(self, tabid):
        '''
        Using the tableids from the Flex queries and other Statements, we are interetsed in these
        tables only and in the columns we define here only.
        The column headers are a subset as found in the input files. eturns different
        column names in
            flex(TRNT)
            csv Activity Statements(Trades)
            html Activity statements (Transactions)
        Fixing the differences is not done here.
        '''
        if tabid not in ['ACCT', 'POST', 'TRNT', 'Open Positions', 'OpenPositions', 'Statement',
                         'Account Information', 'Long Open Positions', 'Short Open Positions',
                         'Trades', 'FlexTrades', 'tblTrades', 'tblTransactions', 'tblOpenPositions',
                         'tblLongOpenPositions', 'tblShortOpenPositions']:
            return []
        if tabid == 'ACCT':
            return ['ClientAccountID', 'AccountAlias']

        if tabid in ['POST', 'Open Positions', 'OpenPositions', 'tblOpenPositions']:
            return ['ClientAccountID', 'Symbol', 'Quantity']


        if tabid in ['Long Open Positions', 'Short Open Positions']:
            # DataDiscriminator is temporary to filter results
            return ['ClientAccountID', 'Symbol', 'Quantity', 'DataDiscriminator']

        if tabid in ['tblLongOpenPositions', 'tblShortOpenPositions']:
            # Not a great data discriminator (Mult=='1')
            return ['ClientAccountID', 'Symbol', 'Quantity', 'Mult']

        # Trades table from fllex csv
        # It seems some statements use DateTime and others Date/Time. (not sure)  Baby sit it
        # with an exception to try to find out.
        if tabid == 'TRNT':
            return ['ClientAccountID', 'Symbol', 'TradeDate', 'TradeTime', 'Date/Time', 'DateTime',
                    'Quantity', 'TradePrice', 'IBCommission', 'Open/CloseIndicator', 'Notes/Codes',
                    'LevelOfDetail', 'IBOrderID']

        if tabid == 'Trades':
            return ['Symbol', 'Date/Time', 'Quantity', 'T. Price', 'Comm/Fee', 'Code',
                    'DataDiscriminator']

        if tabid == 'FlexTrades':
            return ['ClientAccountID', 'Symbol', 'Date/Time', 'Quantity', 'Price', 'Commission',
                    'Code', 'LevelOfDetail', 'OrderID']

        if tabid == 'tblTrades':
            return ['Acct ID', 'Symbol', 'Trade Date/Time', 'Quantity', 'Price', 'Comm']

        if tabid == 'tblTransactions':
            return ['Symbol', 'Date/Time', 'Quantity', 'T. Price', 'Comm/Fee', 'Code']

        ####### Activity Statement non flex #######
        if tabid in ['Statement', 'Account Information']:
            return ['Field Name', 'Field Value']

        if tabid.find('Positions') > -1:
            raise ValueError('Fix it!!!')

        raise ValueError('What did we not catch?')

    def verifyAvailableCols(self, flxcols, ourcols, tabname):
        '''
        Check flxcols against ourcols, remove any cols in ourcols that are missing in flxcols and
        send a warning
        :return: ourcols are the requested cols that exist, missing is complement
        '''
        missingcols = set(ourcols) - set(flxcols)
        if missingcols:
            for col in missingcols:
                ourcols.remove(col)
        return ourcols, missingcols


def notmain():
    ''' Run local stuff'''
    t = StatementDB()
    t.popHol()

def localStuff():
    '''Run local stuff'''
    d = pd.Timestamp('2018-04-01')
    files = dict()
    # files['annual'] = ['_2018_2018.csv', getBaseDir]

    files['stuff'] = ['U2.csv', getDirectory]
    files['flexAid'] = ['ActivityFlexMonth.369463.csv', getDirectory]
    files['flexAid'] = ['ActivityFlexMonth.csv', getDirectory]
    files['flexTid'] = ['TradeFlexMonth.csv', getDirectory]
    files['activityDaily'] = ['ActivityDaily.663710.csv', getDirectory]
    files['U242'] = ['U242.csv', getDirectory]
    files['activityMonth'] = ['CSVMonthly.644225.csv', getDirectory]
    files['dtr'] = ['DailyTradeReport.html', getDirectory]
    files['act'] = ['ActivityStatement.html', getDirectory]
    files['atrade'] = ['trades.643495.html', getDirectory]

    das = 'trades.csv'                          # Search verbatim with searchParts=False
                                                # TODO How to reconcile IB versus DAS input?

    badfiles = []
    goodfiles = []
    for filekey in files:
        # fs = findFilesInDir(files[key][1](d), files[key][0], searchParts=sp)
        fs = findFilesSinceMonth(d, files[filekey][0])
        for f in fs:
            ibs = IbStatement()
            x = ibs.openIBStatement(f)
            if x[0]:
                goodfiles.append(f)
                print()
                for key in x[0]:
                    print(key, list(x[0][key].columns), len(x[0][key]))


            if x[1] and not x[0]:
                badfiles.append([f, x[1]])
                msg = f'\nStatement {f} \n{x[1]}'
                print(msg)
        print()

if __name__ == '__main__':
    # notmain()
    localStuff()
