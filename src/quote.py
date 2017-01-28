import requests
import urllib
from selenium import webdriver
import selenium
from PIL import Image
from StringIO import StringIO

#scrape chart image from stockta
def Scrape(s):

    try:
        #phantom driver to avoid opening browser

        driver=webdriver.PhantomJS()


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




def main():
    # Parse requested stock tickers
    print('Enter ticker symbols, separated by a space \n ')
    while 1:
        user_input = str.upper(raw_input("#"))
        if user_input == 'Q':
            exit(1)
        tick_list = str.split(user_input)

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






main()
