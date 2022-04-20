import random

NUM_DIGITS =3
MAX_GUESS = 10

def getSecrectNum():
    #Retourne une chaîne de NUM_DIGITS caractères tous différents.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum =' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum

def getCluess(guess, secretNum):
        return 'Tu l\'as trouvé !'

        clues =[] 
        for i in rane(len(guess)):
            if guess[i] == secretNum[i]:
             clues.append('Fermi') 
        if guess[i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'

        clues.sort()
        return ' '.join(clues)

def isOnlyDigits(num):
    #Renvoie True si la chaîne contient uniquement des chiffres.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'. split():
            return False

        return True


print('Je pense à un nombre de %s chiffres.'%(NUM_DIGITS),'Essaie de le deviner.')
print('Les indices que je donne sont les suivants...')
print('Quand je dis:        Cela signifie:')
print('     Bagels      Aucun chiffre n\'est correct.')
print('     Pico        Un chiffre est correct mais mal placé.')
print('     Fermi       Un chiffre est correct et bien placé.')

while True:
    secretNum = 'getSecrectNum'
    print('Tu as droit à %s essais.'%(MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) !=NUM_DIGITS or not isOnlyDigits(guess):
            print('Essai #%s : '%(guessesTaken))
            guess = input()

        print(getCluess(guess, secretNum))
        guessesTaken +=1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('TU n\'as plus d\'essais;','La réponse était %s.'%(secretNum))

            print('Veux-tu rejouer(oui ou non)?')
            if not input().lower().startswith('o'):
                break 

    
