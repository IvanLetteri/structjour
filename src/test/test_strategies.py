import os
import sqlite3
from unittest import TestCase
import unittest
from strategy.strategies import Strategy

class TestStrategy(TestCase):
    '''
    Test Strategy object
    '''

    def __init__(self, *args, **kwargs):
        super(TestStrategy, self).__init__(*args, **kwargs)

        ddiirr = os.path.dirname(__file__)
        os.chdir(os.path.realpath(ddiirr + '/../'))
        self.somestrats = ['ABCD', 'Bull Flag', 'Fallen Angel', 'VWAP Support', 'VWAP Reversal']

    def test_addStrategy(self):
        strat = Strategy()
        strat.dropTables()
        strat.createTables()
        strat.loadDefault()
        strat.addStrategy("SELL HIGHER")
        x = strat.getStrategy("SELL HIGHER")
        self.assertEqual(x[0], "SELL HIGHER")

    def test_removeStrategy(self):
        strat = Strategy()
        strat.dropTables()
        strat.createTables()
        strat.loadDefault()

        for s in self.somestrats:
            x = strat.getStrategy(s)
            self.assertEqual(x[0], s)
            strat.removeStrategy(s)
            xx = strat.getStrategy(s)
            self.assertTrue(not xx)

    def test_getStrategy(self):
        pass

    def test_getStrategies(self):
        strat = Strategy()
        strat.dropTables()
        strat.createTables()
        strat.loadDefault()
        strats = strat.getStrategies()
        slist = [s[1] for s in strats]
        for s in self.somestrats:
            self.assertIn(s, slist)
        print()


    def test_getDescription(self):
        strat = Strategy()
        strat.dropTables()
        strat.createTables()
        strat.loadDefault()

        # three strats that have written descriptions in strat.py
        strats = ['ORBU', 'ABCD', 'booty']
        for s in strats:
            ss = strat.getDescription(s)
            self.assertEqual(s, ss[0])
            self.assertGreater(len(ss[1]), 100)
    
    def test_droptables(self):
        '''test Strategy.dropTables'''
        strat = Strategy()
        strat.dropTables()
        strat.createTables()
        strat.loadDefault()
        x = strat.getStrategies()
        slist = list()

        self.assertGreater(len(x), 3)
        
        for s in x:
            slist.append(s[1])
        self.assertIn('ABCD', slist)
        self.assertIn('ORBU', slist)
        self.assertIn('Fallen Angel', slist)

        strat.dropTables()

        try:
            tested = False
            strat.getStrategy('ABCD')
        except sqlite3.OperationalError:
            tested = True
        self.assertTrue(tested, 'Failed to drop tables')


    def test_createTables(self):
        '''Test Strategy.createTables'''
        strat = Strategy()
        strat.dropTables()

        strat.createTables()
        conn = strat.getConnection()

        cursor = conn.execute('''SELECT name FROM sqlite_master 
                                WHERE type ='table' 
                                AND name NOT LIKE 'sqlite_%';''')
        slist = list()
        for row in cursor:
            slist.append(row[0])

        tablist = ['strategy', 'description', 'source', 'links']
        for t in tablist:
            self.assertIn(t, slist)

    def test_loadDefault(self):
        strat = Strategy()
        strat.dropTables()

        strat.createTables()
        strat.loadDefault()
        d = strat.getDescription('booty')
        self.assertEqual('booty', d[0])
        self.assertGreater(len(d[1]), 100)



def notmain():
    t = TestStrategy()
    # t.test_createTables()
    # t.test_loadDefault()
    # t.test_getDescription()
    # t.test_removeStrategy()
    # t.test_addStrategy()
    t.test_getStrategies()

if __name__ == '__main__':
    notmain()
    