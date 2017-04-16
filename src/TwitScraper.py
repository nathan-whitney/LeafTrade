import requests

class TwitScraper:

    def __init__(self):
        self.messages = dict()
        self.trending = list()

    def ScrapeMessages(self, symbol):
        resp = requests.get('https://api.stocktwits.com/api/2/streams/symbol/' + symbol + '.json')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        self.messages[symbol] = resp_json['messages']
        return self.messages

    def ScrapeTrending(self):
        resp = requests.get('https://api.stocktwits.com/api/2/streams/trending.json')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        for i in range(len(resp_json['messages'])):
            self.trending.append(resp_json['messages'][i]['symbols'][0]['symbol'])
        return self.trending


