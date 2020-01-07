# BEHOLD. My own creation! ...Mostly... Translators are hard, ok?
import time
#Morse Code Dictionary
key = {"A":".-",
       "B":"-...",
       "C":"-.-.",
       "D":"-..",
       "E":".",
       "F":"..-.",
       "G":"--.",
       "H":"....",
       "I":"..",
       "J":".---",
       "K":"-.-",
       "L":".-..",
       "M":"--",
       "N":"-.",
       "O":"---",
       "P":".--.",
       "Q":"--.-",
       "R":".-.",
       "S":"...",
       "T":"-",
       "U":"..-",
       "V":"...-",
       "W":".--",
       "X":"-..-",
       "Y":"-.--",
       "Z":"--..",
       "0":"-----",
       "1":".----",
       "2":"..---",
       "3":"...--",
       "4":"....-",
       "5":".....",
       "6":"-....",
       "7":"--...",
       "8":"---..",
       "9":"----.",
       "?":"..--..",
       ",":"--..--",
       ".":".-.-.-",
       "=":"-...-",
       "!":"-.-.--",
       "/":"-..-.",
       "\"":".-..-.",
       "-":"-....-",
       "(":"-.--." ,
       ")":"-.--.-"
        }

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

def cont():
    time.sleep(.5)
    ask = input("Would you like to keep using the translator? (\'y\' to continue, \'n\' to quit) ")
    if 'y' in ask:
        time.sleep(.5)
        start()
    elif 'n' in ask:
        exit()
def encrypt(message):  #encrypts message into morse
    cipher = ' '
    for letter in message:
        if letter != ' ':
            #Looks in key and adds the corresponding morse
            #and adds a space to separate characters
            cipher += key[letter] + ' '
        else:
            #one spece indicates different characters
            #two spaces indicates different words
            cipher += ' '
    return cipher

def decrypt(message):  #decrypts message into english
    message += ' '  #adds extra space to the end to access last morse code
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '): #checks for space
            i = 0   #counter to keep track of space
            citext += letter    #storing morse code of a single character
        else:   #in case of space
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(key.keys())[list(key.values()).index(citext)]
                citext = ''
    return decipher

def start():
    time.sleep(1)
    intro = input("Welcome to the Morse Code Translator! Type \'n\' for encoding or \'d\' for decoding morse! ")
    if 'n' in intro:
        time.sleep(.5)
        message = input("Type something to be translated into morse code: ")
        result = encrypt(message.upper())
        time.sleep(.5)
        print(result)
        cont()
    elif 'd' in intro:
        time.sleep(.5)
        message = input("Type something in morse code using -'s and .'s (Put spaces between each character): ")
        result = decrypt(message)
        time.sleep(.5)
        print(result)
        cont()
    else:
        time.sleep(.5)
        print("You didn't pick an option! What a nerd!")
        cont()

start()
