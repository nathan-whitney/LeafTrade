"""
The main process for the program
Return here after exiting a subprocess
"""

print("Enter desired function, or !help\nQ to quit")
while 1:
    user_input = str.upper(raw_input("#"))
    if user_input == 'Q' or user_input == 'QUIT':
        exit(1)
    elif user_input == '!HELP':
        print('Supported functions:\n'
              '    -QUOTE\n'
              '    -WATCH\n'
              '    -ANALYZE\n')
    elif user_input == 'QUOTE':
        import quote
        quote.__main__()

    elif user_input == 'WATCH':
        import watch
        watch.__main__()

    else:
        print("Invalid command")