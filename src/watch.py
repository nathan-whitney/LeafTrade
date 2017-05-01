import os
import requests
import time


def quoteloop(symbols):
    """
    loop to get quotes
    :param symbols: stocks to quote
    :return: repeatedly quotes prices of stocks
    """
    # use trending list if no symbols supplied
    if len(symbols) == 0:
        resp = requests.get('https://api.stocktwits.com/api/2/trending/symbols.json')
        if resp.status_code != 200:
            # This means something went wrong.
            print('error ' + str(resp.status_code))
            exit(resp.status_code)
        resp_json = resp.json()
        for s in resp_json['symbols']:
            symbols.append(s['symbol'])

    # Parse requested stock tickers
    while 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Process tickers
        for s in symbols:
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
        time.sleep(5)

def __main__(argv):
    """
    Main process for watching
    :return: N/A
    """
    if argv is not None:
        tick_list = argv
        for i in range(0, len(tick_list)):
            tick_list[i] = str.upper(tick_list[i])
        quoteloop(tick_list)
    else:
        print('Enter ticker symbols to monitor, separated by a space. Q to quit \n ')
        user_input = str.upper(raw_input("#"))
        if user_input == 'Q':
            import leafTrader
        tick_list = str.split(user_input)
        quoteloop(tick_list)