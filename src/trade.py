import datetime

from journalfiles import JournalFiles
from journal.pandasutil import InputDataFrame, ToCSV_Ticket as Ticket
from journal.tradeutil import TradeUtil
from withstyle.layoutsheet import LayoutSheet
from withstyle.tradestyle import TradeFormat
from withstyle.mstksum import MistakeSummary

# jf=JournalFiles(theDate=datetime.date(2018, 10, 19), infile="trades2.csv", outdir="out/", mydevel=True)

jf=JournalFiles(infile="hypothetical.csv", mydevel=True, outdir="out/")
jf._printValues()
        
tkt = Ticket(jf)
trades, jf =tkt.newDFSingleTxPerTicket()
# trades = pd.read_csv(jf.inpathfile)

idf = InputDataFrame()
trades = idf.processInputFile(trades)

tu = TradeUtil()
inputlen, dframe, ldf = tu.processOutputDframe(trades)

#Process the openpyxl excel object using the output file DataFrame. Insert images and Trade Summaries.
sumSize = 25
margin=25

# Create the space in dframe to add the summary information for each trade. Then create the Workbook.
ls = LayoutSheet(sumSize,margin, inputlen)
imageLocation, dframe = ls.createImageLocation(dframe, ldf)
wb, ws, nt =ls.createWorkbook(dframe)
ls.styleTop(ws, nt)

tf = TradeFormat(wb)
assert (len(ldf) == len(imageLocation))

mstkAnchor = (len(dframe.columns) + 2, 1)
mistake = MistakeSummary(numTrades=len(ldf), anchor=mstkAnchor)
mistake.mstkSumStyle(ws, tf, mstkAnchor)
     
tradeSummaries = ls.createSummaries(imageLocation, ldf, jf, ws, tf)
ls.createMistakeForm(tradeSummaries, mistake, ws, imageLocation)    
    
ls.save(wb, jf)
