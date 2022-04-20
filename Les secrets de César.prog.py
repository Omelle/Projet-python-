#Chiffrement de César
from curses import KEY_TAB
from fnmatch import translate
from tkinter.messagebox import Message

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖŒabecdefghijiklmnopqrstuvwxyzäåæçèéêœëòóôõö123456890'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Veux-tu chiffrer (c) ou déchiffrer ou force brute (c/d/f)?')
        mode = input().lower()
        if mode[0] in ['c','d','f']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brut" or "b".')

def getMessage():
    print('Saisis ton message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Choisis la clé (1-%s)' %(MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0]=='d':
        key = -key
        translated = ''

for symbol in Message:

    symbolIndex = SYMBOLS.find(symbol)
    if symbolIndex == -1: # Symbole absent de SYMBOLS.
        # Ajoute juste ce symbole tel quel.
            translate += symbol

    else : symbolIndex += KEY_TAB  # Chiffre ou déchiffre.              

    if symbolIndex >= len(SYMBOLS):
        symbolIndex -= len(SYMBOLS)
    elif symbolIndex <0:
        symbolIndex += len(SYMBOLS)
        translate += SYMBOLS[symbolIndex]
        "return"(translate)
        
    mode = getMode()
    message = getMessage()
if mode[0] != 'b':
   key = getKey()
print('Le message traduit est :')
if mode[0] !='b':
   print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE +1):
        print(key, getTranslatedMessage('d', message, key))
