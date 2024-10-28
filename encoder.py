from math import ceil

# Ceaser Cipher
def caesar(shift, input):
    '''Simple ceaser shift. Input is a interger for shift and a string for input. Retruns a string as output.'''
    try:
        input = input.lower()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z']
        output = ''
        for char in input:
            if char in alphabet:
                index = alphabet.index(char) + shift
                if index > len(alphabet)-1:
                    index = -1*(len(alphabet) - index)
                output = output + alphabet[index]
            else:
                output = output + char
        return output
    except Exception as e:
        return f'Failed. Reason: {e}'
    

def polibius(input, xy):
    '''5x5 square cipher, simple cooridinate system. Input is a interger for xy and a string for input. Retruns a string as output.'''
    try:
        input = input.lower()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z']
        output = ''
        for char in input:
            if char == 'j':
                char = 'i'
            if char in alphabet:
                num1 = str((alphabet.index(char)+6)%5)
                if num1 == '0':
                    num1 = '5'
                num2 = str(ceil((alphabet.index(char)+1)/5))
                if xy == 1:
                    output = output + num1 + num2 + ' '
                else:
                    output = output + num2 + num1 + ' '
            else:
                output = output + char
        return output
    except Exception as e:
        return f'Failed. Reason: {e}'
    
