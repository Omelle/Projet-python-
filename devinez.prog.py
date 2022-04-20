# Jeu devinez le nombre.
import random

guessesTaken = 0 #GuessesTaken est une variable pour stocker les nombres de réponses proposées.

print('Bonjour! Comment tappelles-tu')
myName = input()

number=random.randint(1,20) # Random.randint est une variable qui génère des nombres aléatoires.
print('Bien'+myName+',Je pense à un nombre entre 1 et 20.')

for guessesTaken in range(6):
    print('Essaie de le deviner.')#Quatre espaces devant"print"
    guess=input()
    guess=int(guess) # Chaque espace de chaque variable ou  s'appelle une identation.

    if guess < number:
        print('Trop petit')#Huit espaces devant "print"

    if guess>number:
        print('Trop grand')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken+1)
    print('Bravo,'+myName+'! Tu as trouvé mon nombre en'+guessesTaken+'essai(s)!')

if guess != number:
    number = str(number)
    print('Raté!Le nombre auquel je pensais était'+ number +'.')
