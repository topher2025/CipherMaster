# Ceaser Cipher
def caesar(shift, input):
    '''simple ceaser shift. Input is a interger for shift and a string for input. Retruns a string as output.'''
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