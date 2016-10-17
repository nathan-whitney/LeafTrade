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
        subprocess.call(" python quote.py", shell=True)
    elif user_input == 'WATCH':
        subprocess.call(" python watch.py", shell=True)
    else:
        print("Invalid command")


