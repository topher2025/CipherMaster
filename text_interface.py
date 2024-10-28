import encoder
from os import name, system

def interface():
    print('\nCipherMaster')
    user_input = input('$ ')
    if user_input == 'clear':
        system('cls' if name == 'nt' else 'clear')
        return 1
    if user_input == 'help':
        print("ceaser INPUT [-SHIFT]\nclear\nhelp [COMMAND]\nquit")
        return 1
    if user_input == 'quit':
        system('cls' if name == 'nt' else 'clear')
        return 0
    
    if user_input[0: 6] == 'ceaser':
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
        print(encoder.ceaser(shift, plaintext))
        return 1

    else:
        print(f"'{user_input}' is not a recognized command. Type 'help' for a list of all commands with arguments.")
        return 1


system('cls' if name == 'nt' else 'clear')
print("'help' for help")
while True:
    if interface() == 1:
        pass
    else:
        break