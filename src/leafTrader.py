import quote

while 1:
    user_input = str.upper(raw_input("#"))
    if user_input =='Q':
        exit(1)
    elif user_input == 'QUOTE':
        quote.main()
    else:
        print("Invalid command")


