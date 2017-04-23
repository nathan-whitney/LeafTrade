def __main__():
    from SelectionAlgo import Selector
    while 1:
        print('Enter symbols to analyze, separated by a space \n ')
        user_input = str.upper(raw_input("#"))
        if user_input == 'Q':
            import leafTrader
        tick_list = str.split(user_input)
        sel = Selector(tick_list)
        watchlist = sel.select_stocks()
        print "Stocks to watch:\n"
        print watchlist
        print "\n"