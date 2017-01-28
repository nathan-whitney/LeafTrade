import subprocess

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
        retval = subprocess.call(" python quote.py", shell=True)
        if retval != 1:
            exit(retval)
        else:
            print("Enter desired function, or !help\nQ to quit")

    elif user_input == 'WATCH':
        retval = subprocess.call(" python watch.py", shell=True)
        if retval != 1:
            exit(retval)
        else:
            print("Enter desired function, or !help\nQ to quit")

    else:
        print("Invalid command")