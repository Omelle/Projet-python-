import random
import time

def displayIntro():
    print('''Tu es dans le pays rempli de dragons.Devant toi,tu vois deux grottes.
Dans l'une, le dragon est amical et partagera son trésor avec toi.
Dans l'\autre, le dragon est affamé et
te dévorera s'il te voit.''')
    print()

def chooseCave():
    cave=''
    while cave!='1'and cave!='2':
        print('Dans quelle grotte vas-tu entrer (1 ou 2) ?')
        cave = input()
    return cave


def checkCave(ChosenCave):
    print('Tu t\'approches de la grotte...')
    time.sleep(2)
    print('Tout est sombre et effrayant...')
    time.sleep(2)
    print('Un énorme dragon saute juste devant toi !'
          + 'Il ouvre grand ses mâchoires et...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if ChosenCave == str(friendlyCave):
        print('te donne son trésor !'+ 'You win')
    else:
        print('t\'avale d\'un seul coup !'+ 'Game over')
    print()

playAgain = 'oui'
while playAgain == 'oui' or playAgain == 'o':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Veux-tu rejouer (oui ou non)?')
    playAgain = input()
    
