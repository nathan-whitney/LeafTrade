import string
def __main__(argv):
    """
    wrapper script to execute analysis functions
    :return: see selectionalgo functions
    """
    from SelectionAlgo import Selector
    import requests

    def examine_list(tick_list):
        sel = Selector(tick_list)
        watchlist = sel.select_stocks()
        print "Stocks to watch:\n"
        print watchlist
        print "\n"

    if argv is not None:
        tick_list = argv
        print tick_list
        for i in range(0, len(tick_list)):
            tick_list[i] = str.upper(tick_list[i])
        examine_list(tick_list)

    else:
        while 1:
            tick_list = list()
            print('Enter symbols to analyze, separated by a space \n'
                  'Enter \'reddit\' to switch from StockTwits scraping(default) to Reddit scraping')
            user_input = str.upper(raw_input("#"))
            if string.upper(user_input) == 'Q':
                import leafTrader
            if string.upper(user_input) == 'REDDIT':
                sel = Selector([""])
                print 'Stocks being discussed on Reddit:'
                print sel.parse_reddit()
                print '\n'
                continue
            # use trending list if no symbols supplied
            if user_input == "":
                resp = requests.get('https://api.stocktwits.com/api/2/trending/symbols.json')
                if resp.status_code != 200:
                    # This means something went wrong.
                    print('error ' + str(resp.status_code))
                    exit(resp.status_code)
                resp_json = resp.json()
                for s in resp_json['symbols']:
                    tick_list.append(s['symbol'])
            else:
                tick_list = str.split(user_input)

            examine_list(tick_list)
