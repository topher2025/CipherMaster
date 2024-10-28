import encoder
from os import name, system



def help(input):
    if input == 'caesar':
        print('\nCaesar Cipher\nEncodes using caeser cipher\nThe shift input can take integers from 1 to 37\nNOTE: With no shift input, the function will default to 3\n\n---Example---\n    $ caesar Have fun with this!! -4\n    lezi jyr amxl xlmw!!')
        return 1
    if input == 'clear':
        print("Clears the console.")
        return 1
    if input == 'help':
        print('\nGives a list of all commands\nWhen used with a specific comand it explains arguments for that function\n\n---Example---\n    $ help quit\n    Quits the program.')
        return 1
    if input == 'polibius':
        print('\nPolibius Cipher\nEncodes using a 5x5 square\nThe order input can take 1 (xy) or 0 (yx)\nNOTE: With no order input, the function defaults to xy (instead of yx)\n\n---Example---\n    $ polibius Have fun with this!! -0\n    23 11 51 15  21 45 33  52 24 44 23  44 23 24 43 !!')
        return 1
    if input == 'quit':
        print("Quits the program.")
        return 1
    else:
        print(f"'{input}' is not a known help command.")
        return 1

def caesar(input):
    if input[len(input)-2] == '-':
        try:
            shift = int(input[len(input)-1:])
        except:
            print('Invalid shift argument.')
            return 1
        plaintext = input[0:len(input)-3]
    elif input[len(input)-3] == '-':
        try:
            shift = int(input[len(input)-2:])
        except:
            print('Invalid shift argument.')
            return 1
        plaintext = input[0:len(input)-4]
    else:
        shift = 3
        plaintext = input
    print(encoder.caesar(shift, plaintext))
    return 1

def polibius(input):
    if input[len(input)-2] == '-':
        try:
            order = int(input[len(input)-1])
        except:
            print('Invalid order argument.')
            return 1
        plaintext = input[0:len(input)-3]
    else:
        order = 1
        plaintext = input
    print(encoder.polibius(plaintext, order))
    return 1



def interface():
    print('\nCipherMaster')
    user_input = input('$ ')
    if user_input == 'clear':
        system('cls' if name == 'nt' else 'clear')
        return 1
    if user_input == 'help':
        print("\nType 'help' to see this list of defined commands.\nType 'help name' to find out more about command 'name'\n\ncaesar INPUT [-SHIFT]\nclear\nhelp [COMMAND]\npolibius INPUT [-ORDER]\nquit")
        return 1
    if user_input == 'quit':
        system('cls' if name == 'nt' else 'clear')
        return 0
    
    if user_input[0:6] == 'caesar':
        caesar(user_input[7:])
        
    if user_input[0:8] == 'polibius':
        polibius(user_input[9:])

    if user_input[0:5] == 'help ':
        help(user_input[5:])
        
    else:
        print(f"'{user_input}' is not a known command. Type 'help' for a list of all commands with arguments.")
        return 1



system('cls' if name == 'nt' else 'clear')
print("'help' for help")
while True:
    if interface() == 1:
        pass
    else:
        break