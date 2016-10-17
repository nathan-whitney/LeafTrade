import sys
import requests
import json



def main():
    user_input = ""

    # Parse requested stock tickers
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
                print(resp.status_code)
            resp_json = resp.json()
            print('\n' + resp_json['symbol'] + '\n')
            print('Last trade price: ' + resp_json['last_trade_price'])
            print('Previous close: ' + resp_json['previous_close'])
            print('Ask price: ' + resp_json['ask_price'])
            print('Bid price: ' + resp_json['bid_price'])
            print('Ask volume: ' + str(resp_json['ask_size']))
            print('Bid volume: ' + str(resp_json['bid_size']))
            print('Last updated: ' + str(resp_json['updated_at']))




main()