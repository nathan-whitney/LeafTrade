import requests

class TwitScraper:
    """
    A class to gather data from stocktwits for a crowd-sourced information system
    """

    def __init__(self):
        self.messages = dict()
        self.trending = list()

    def ScrapeMessages(self, symbol):
        """
        Get the most recent messages for a symbol
        :param symbol: symbol to check
        :return: list of messages regarding this symbol
        """
        resp = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        self.messages[symbol] = resp_json['messages']
        return self.messages

    def ScrapeTrending(self):
        """
        Get the currently trending symbols
        :return: List of trending symbols
        """
        resp = requests.get('https://api.stocktwits.com/api/2/streams/trending.json')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        for i in range(len(resp_json['messages'])):
            self.trending.append(resp_json['messages'][i]['symbols'][0]['symbol'])
        return self.trending


