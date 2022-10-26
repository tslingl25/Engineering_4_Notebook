import board
# This is the library, it is like a dictionary for the pico.
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}


while True:
#This is the message, it prints on the serial monitor.
    try:
        print("Enter morse code message or type -q to break")
        message = input()
    
                

        if message == "-q": #This is if you wanna exit the true loop.
            break


        message = message.upper()
        #sequences the libary with a command
        for letter in message:
            print(MORSE_CODE[letter])
        print()
    except:
            print('BAD FORMATTING')