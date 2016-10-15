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

            for item in resp:
                print(item)




main()