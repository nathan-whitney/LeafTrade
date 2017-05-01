from TextAnalysis import SentimentAnalyzer
import requests
from TwitScraper import TwitScraper
import math
import string
import requests


class Selector():
    """
    A class to select promising high-volatility stocks from a given list
    """

    def __init__(self, tickerlist):
        self.symbols = list(tickerlist)
        self.analyzer = SentimentAnalyzer()
        self.scraper = TwitScraper()
        self.selected_stocks = list()

    def parse_reddit(self):
        """
        Retrieve list of currently discussion symbols on reddit.com/r/stocks
        with help from
        https://www.reddit.com/r/learnpython/comments/574pn5/anyone_have_a_reddit_scraper/
        :return: list of currently discussed symbols on reddit
        """
        subreddit = 'stocks'

        r = requests.get(
            'http://www.reddit.com/r/{}.json'.format(subreddit),
            headers={'user-agent': 'Mozilla/5.0'}
        )

        # view structure of an individual post
        # print(json.dumps(r.json()['data']['children'][0]))
        posts = list()
        symbols = list()
        for post in r.json()['data']['children']:
            posts.append(post['data']['title'])
        for post in posts:
            words = string.split(post)
            for word in words:
                if '$' in word:
                    symbols.append(word)
        return symbols

    def select_stocks(self):
        """
        Select stocks from the object's list
        :return: top promising stocks
        """
        selected_stocks = list()

        for s in self.symbols:
            resp = requests.get('https://api.robinhood.com/quotes/' + s + '/')
            if resp.status_code != 200:
                # This means something went wrong.
                print('error ' + str(resp.status_code))
                continue
            resp_json = resp.json()

            # populate values
            last_trade = resp_json['last_trade_price']
            prev_close = resp_json['previous_close']
            ask_price = resp_json['ask_price']
            bid_price = resp_json['bid_price']
            ask_volume = resp_json['ask_size']
            bid_volume = resp_json['bid_size']
            extended_close = resp_json['last_extended_hours_trade_price']

            # standard metrics
            price_progress = float(last_trade) - float(prev_close)
            bid_ask_spread_percent = (float(ask_price) - float(bid_price))/float(ask_price)
            bid_ask_volume_spread = float(ask_volume) - float(bid_volume)

            # integrate stocktwits functions
            messages = self.scraper.ScrapeMessages(s)
            rating = 0
            for message in messages[s]:
                rating += self.analyzer.AnalyzeSentiment(message['body'])

            # the magic formula
            momentum = price_progress * bid_ask_volume_spread * bid_ask_spread_percent * 0.5 * rating + rating

            if rating < 0 and momentum > 0:
                momentum *= -1

            if momentum > 2:
                selected_stocks.append(s)


            print s
            print price_progress
            print bid_ask_spread_percent
            print bid_ask_volume_spread
            print rating
            print momentum
            print '\n'
        # print selected_stocks
        return selected_stocks
