import time
import unittest
from subprocess import Popen, PIPE

from SelectionAlgo import Selector
from TextAnalysis import SentimentAnalyzer
from TwitScraper import TwitScraper


class TestFunctions(unittest.TestCase):

    # def test_driver(self):
    #     """
    #     test usage of phantom web driver with selenium
    #     :return success if driver operation succeeds
    #     """
    #     from selenium import webdriver
    #     driver=webdriver.PhantomJS(executable_path=r'/home/nathan/PycharmProjects/LeafTrade/src/driver/bin/phantomjs')
    #     try:
    #         driver.get('http://www.stockta.com/cgi-bin/analysis.pl?symb='+ 'MSFT' + '&cobrand=&mode=stock')
    #     except AttributeError:
    #         print('AttributeError: is the phantomJS executable in your PATH?')
    #     self.assertEquals(1,1)

    def test_main(self):
        p = Popen('python /home/nathan/PycharmProjects/LeafTrade/src/leafTrader.py', stdin=PIPE, shell=True)
        p.stdin.write('quote\n')
        time.sleep(0.1)
        p.stdin.write('Q\n')
        time.sleep(0.1)
        p.stdin.write('Q\n')


    #
    # def test_scrape(self):
    #     """
    #     test scraping of charts
    #     :return: success if scrape is valid
    #     """
    #     import quote
    #     quote.Scrape('MSFT')
    #     self.assertEquals(1,1)

    def test_twit_scrape(self):
        ts = TwitScraper()
        ts.ScrapeMessages('AAPL')
        self.assertTrue(ts.messages['AAPL'] is not None)
        # ts.ScrapeMessages('ZZZZZZZZ')


    def test_trending_scrape(self):
        ts = TwitScraper()
        ts.ScrapeTrending()
        self.assertTrue(ts.trending[0] is not None)

    def test_sentiment_analysis(self):
        sa = SentimentAnalyzer()
        self.assertTrue(sa.positive_words[1] == 'abound')
        # self.assertTrue(sa.AnalyzeSentiment('bullish bearish', 'MSFT')==0)
        # self.assertTrue(sa.AnalyzeSentiment('gem bullish', 'AAPL')==4)
        # self.assertTrue(sa.AnalyzeSentiment('bullish is bearish', 'AMRS')==1)
        # self.assertTrue(sa.AnalyzeSentiment('is', 'GOOG')==0)
        sa.AnalyzeSentiment('is good bullish word gem')
        # self.assertTrue(sa.AnalyzeSentiment('is', 'GOOG')==1)
        # self.assertTrue(sa.ratings_dict['AAPL']=='Watch')
        sa.AnalyzeSentiment('bad evil mean terrifying')

    def test_selector(self):
        symbolslist = ['UVXY', 'MITK', 'MCD', 'CSX', 'OCLR', 'ZZZZZZ', 'AMRS']

        sel = Selector(symbolslist)
        print sel.select_stocks()

    def test_reddit(self):
        symbolslist = ['UVXY', 'MITK', 'MCD', 'CSX', 'OCLR', 'ZZZZZZ', 'AMRS']

        sel = Selector(symbolslist)
        sel.parse_reddit()




