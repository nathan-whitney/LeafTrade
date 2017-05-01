"""
The main process for the program
Return here after exiting a subprocess
"""
import sys

def execute_command(user_input, argv):
    """
    dispatcher function to activate subroutines
    :param user_input: the function to activate
    :param argv: CLI-style argv arguments, if applicable
    """
    if user_input == 'Q' or user_input == 'QUIT':
        exit(1)
    elif user_input == '!HELP':
        print('Supported functions:\n'
              '    -QUOTE\n'
              '    -WATCH\n'
              '    -ANALYZE\n')
    elif user_input == 'QUOTE':
        import quote
        quote.__main__(argv)

    elif user_input == 'WATCH':
        import watch
        watch.__main__(argv)

    elif user_input == 'ANALYZE':
        import Analyze
        Analyze.__main__(argv)

    else:
        print("Invalid command")


if len(sys.argv) > 1:
    execute_command(str.upper(sys.argv[1]), sys.argv[2:])

else:
    print("Enter desired function, or !help\nQ to quit")
    while 1:
        user_input = str.upper(raw_input("#"))
        execute_command(user_input, None)

