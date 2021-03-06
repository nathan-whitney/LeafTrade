import requests
import urllib
from selenium import webdriver
import selenium
from PIL import Image
from StringIO import StringIO


def Scrape(s):
    """
    scrape stock chart from stockta
    :param s: symbol to check
    :return: displays chart of symbol
    """
    try:
        #phantom driver to avoid opening browser

        driver=webdriver.PhantomJS(executable_path=r'/home/nathan/PycharmProjects/LeafTrade/src/driver/bin/phantomjs')


        try:
            driver.get('http://www.stockta.com/cgi-bin/analysis.pl?symb='+ s +
                    '&cobrand=&mode=stock')
        except AttributeError:
            print('AttributeError: is the phantomJS executable in your PATH?')

        #search for img tag
        images = driver.find_elements_by_tag_name('img')
        for image in images:
            src = image.get_attribute("src")
            #only take url with ticker name in it (i.e. the chart)
            if src and s in src:
                urllib.urlretrieve(src, "chart.png")
                img = Image.open("chart.png")
                img.show()
    except selenium.common.exceptions.WebDriverException:
        print('Chart cannot be displayed: is the phantomJS executable in your PATH?')


def process_tickers(tick_list):
    """
    get info quotes for all tickers listed
    :param tick_list: list of symbols
    :return: robinhood API statistics for symbols
    """
    # use trending list if no symbols supplied
    if len(tick_list) == 0:
        resp = requests.get('https://api.stocktwits.com/api/2/trending/symbols.json')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        for s in resp_json['symbols']:
            tick_list.append(s['symbol'])

    # Process tickers
    for s in tick_list:
        resp = requests.get('https://api.robinhood.com/quotes/' + s + '/')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        print('\n' + resp_json['symbol'] + '\n')
        print('Last trade price: ' + resp_json['last_trade_price'])
        print('Previous close: ' + resp_json['previous_close'])
        print('Ask price: ' + resp_json['ask_price'])
        print('Bid price: ' + resp_json['bid_price'])
        print('Ask volume: ' + str(resp_json['ask_size']))
        print('Bid volume: ' + str(resp_json['bid_size']))
        print('Last updated: ' + str(resp_json['updated_at']))

        Scrape(s)

def __main__(argv):
    """
    Initiate quote function
    :return: price quote for given stock
    """
    # Parse requested stock tickers
    if argv is not None:
        tick_list = argv
        for i in range(0, len(tick_list)):
            tick_list[i] = str.upper(tick_list[i])
        process_tickers(tick_list)
    else:
        print('Enter ticker symbols, separated by a space \n ')
        while 1:
            user_input = str.upper(raw_input("#"))
            if user_input == 'Q':
                import leafTrader
            tick_list = str.split(user_input)
            process_tickers(tick_list)








