MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}
message=input("enter your message: ")
def encrypt(message):
    ciphered=''
    for letter in message:
        if letter != '':
            letter=letter.upper()
            ciphered += MORSE_CODE_DICT[f'{letter}']
        else:
            print('enter your message to be ciphered')
    print(ciphered)
    
encrypt(message)

