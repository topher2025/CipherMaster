import encoder
from os import name, system

def interface():
    print('\nCipherMaster')
    user_input = input('$ ')
    if user_input == 'clear':
        system('cls' if name == 'nt' else 'clear')
        return 1
    if user_input == 'help':
        print("\nType 'help' to see this list of defined commands.\nType 'help name' to find out more about command 'name'\n\ncaesar INPUT [-SHIFT]\nclear\nhelp [COMMAND]\nquit")
        return 1
    if user_input == 'quit':
        system('cls' if name == 'nt' else 'clear')
        return 0
    
    if user_input[0:6] == 'caesar':
        user_input = user_input[7:]
        if user_input[len(user_input)-2] == '-':
            try:
                shift = int(user_input[len(user_input)-1:])
            except:
                print('Invalid shift argument.')
                return 1
            plaintext = user_input[0:len(user_input)-3]
        elif user_input[len(user_input)-3] == '-':
            try:
                shift = int(user_input[len(user_input)-2:])
            except:
                print('Invalid shift argument.')
                return 1
            plaintext = user_input[0:len(user_input)-4]
        else:
            shift = 3
            plaintext = user_input
        print(encoder.caesar(shift, plaintext))
        return 1

    if user_input[0:5] == 'help ':
        user_input = user_input[5:]
        if user_input == 'caesar':
            print('\nCaesar Cipher\nEncodes using caeser cipher\nNOTE: With no shift input, the function will default to 3\n\n---Example---\n    $ caesar Have fun with this!! -4\n    lezi jyr amxl xlmw!!')
            return 1
        if user_input == 'clear':
            print("Clears the console.")
            return 1
        if user_input == 'help':
            print('\nGives a list of all commands\nWhen used with a specific comand it explains arguments for that function\n\n---Example---\n    $ help quit\n    Quits the program.')
            return 1
        if user_input == 'quit':
            print("Quits the program.")
            return 1
        else:
            print(f"'{user_input}' is not a known command.")
            return 1
    
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