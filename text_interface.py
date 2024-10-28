import encoder
import simple_decoder as sd
from os import name, system



def help(input):
    if input == 'caesar':
        print("\nCaesar Cipher\nEncodes using caeser cipher\nThe shift input can take integers from 1 to 37.\nThe second argurment MUST be present, it is an 'e' for ENCODE and 'd' for DECODE. The argument always comes at the end\nNOTE: With no shift input, the function will default to 3\n\n---Example---\n    $ caesar Have fun with this!! -4e\n    lezi jyr amxl xlmw!!")
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
    if input[len(input)-3] == '-':
        try:
            shift = int(input[len(input)-2: len(input)-1])
        except:
            print('Invalid shift argument.')
            return 1
        plaintext = input[0:len(input)-4]
    elif input[len(input)-4] == '-':
        try:
            shift = int(input[len(input)-3: len(input)-1])
        except:
            print('Invalid shift argument.')
            return 1
        plaintext = input[0:len(input)-5]
    else:
        shift = 3
        plaintext = input
    if input[len(input)-1] == 'e':
        print(encoder.caesar(shift, plaintext))
        return 1
    else:
        print(sd.decode_caeser(shift, plaintext))
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
    elif user_input == 'help':
        print("\nType 'help' to see this list of defined commands.\nType 'help name' to find out more about command 'name'\nThe 'e' or 'd' arguments are always the last argument in the command.\n\ncaesar INPUT [-SHIFT][E\D]\nclear\nhelp [COMMAND]\npolibius INPUT [-ORDER]\nquit")
        return 1
    elif user_input == 'quit':
        system('cls' if name == 'nt' else 'clear')
        return 0   
    
    elif user_input[0:6] == 'caesar':
        value = caesar(user_input[7:])

    elif user_input[0:8] == 'polibius':
        value = polibius(user_input[9:])
        
    elif user_input[0:5] == 'help ':
        value = help(user_input[5:])       
    
    else:
        print(f"'{user_input}' is not a known command. Type 'help' for a list of all commands with arguments.")
        return 1
    return value


system('cls' if name == 'nt' else 'clear')
print("Type 'help' for help")
while True:
    if interface() == 1:
        pass
    else:
        break