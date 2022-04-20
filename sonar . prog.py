# Chasse au trésor

import random
import sys
import math

def getNewBoard():
    #Crée un nouveau plateau de 60 x15
    board = []
    for x in range(60): # Liste principale de 60 listes
        board.append([])
        for y in range (15): # Liste de 15 chaînes de 1 caractère
            # Représente l'océan avec différents caractères
            if random.randint(0, 1) ==0:
                board[x].append('~')
        else:
                    board[x].append('`')
                    return board

def drawBoard(board):
    #Dessine le plateau.
    tensDigitsLine = '    ' # 4 espaces à gauche des chiffres des dizaines
    for i in range(1, 6):
        tensDigitsLine += (' '* 9) +str(i)

    #Affiche les coordonnées du haut du plateau
        print(tensDigitsLine)
        print('   ' +('0123456789' *6)) #3 espaces à gauche
        print()

    #Affiche les 15 linges d'océan
    for row in range(15):
        #Justifie les 9 premiers nombres avec un espace.
        if row <10:
            extraSpace = ' ' #1 espace
        else:
            extraSpace= ''   #Chaîne vide

    #Crée une chaîne représentant une ligne d'océan
            boardRow = ''
            for column in range (60):
                boardRow += board[column][row]

    print('%s%s %s %s' %(extraSpace, row, boardRow, row))

    #Affiche les coordonnées du bas du plateau
    print()
    print('  '+('0123456789' *6)) # 3 espaces à gauche
    print(tensDigitsLine)

    def getRandomChests(numChests):
        #Crée une liste des coordonnées [x, y] ds trésors
        chests = []
        while len(chests) < numChests:
            newChest = [random.randint(0,59), random.randint(0,14)]
            if newChest not in chests: # Trésor pas déjà dans la liste
                chest.append(newChest)
        return chests

    def isOnBoard(x, y):
        #Vérifie que les coordonnées sont dans le plateau
        return x >= 0 and x <= 59 and y >=0 and y <= 14

    def makeMove(board, chests, x, y):
        #Ajoute un indice de sonar ( caractère) sur le plateau
        #Supprim un trésor de la liste quand il a été trouvé
        #Renvoie la chaîne résulatat du placement
        smallestDistance = 100 #Les trésors sont à moins de 100 m
        for cx, cy in chests:
            distance = math.sqrt((cx-x) * (cx-x) +(cy-y) *(cy-y))

            if distance < smallestDistance: # Trésor le plus proche
                smallestDistance = distance

    smallestDistance  = round(smallestDistance)

    if smallestDistance == 0:
        # Le sonar tombe sur un trésor
        chests.remove([x, y])
        return 'Tu as trouvé un des trésors !'
    else:
        if smallestDistance <10:
            board[x][y] = str(smallestDistance)
            return 'Un trésor est détecté à %s cases du sonar.'%(smallestDistane)
        else:
            board[x][y] = 'X'
            return 'Le sonar n\'a  détecté aucun trésor à proximité.'

        def enterPlayerMove(previousMoves):
            # Demande 2 coordonnées entières au joueur.Renvoie une lsite
            print('Ou veux-tu placer le prochain sonar ? (0-59 0-14)','(q pour quitter)')
            while True:
                move = input()
                if move.lower() =='q':
                    print('Merci d\'avoir joué !')
                    sys.exit()

                move = move.split()
                if len(move)==2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
                    if [int(move[0]), int(move[1])] in previousMoves:
                        print('Tu as déjà proposé cet endroit.')
                        continue
                    return [int(move[0]), int(move[1])]

                print('Entre un nombre entre 0 et 59, un espace, ','puis un nombre entre 0 et 14.')

                def showInstructions():
                    print('''Voici les règles du jeu : Tu es le capitaine du Simon, un bateau qui recherche des trésors engloutis.
Ta mission est d'utiliser des sonars pour localiser trois trésors , mais ils ne t'indiquent que la distance, pas la direction.



Entre les coordonnées d'un sonar. La carte de l'océan va t'indiquer à quelle distance se trouve le trésor le plus proche ou un X s'il est trop loin du sonar.


Sur l'exemple ci-dessous, les T montrent où sont les trésors.
Le sonar indique 3 car le plus proches est éloigné de 3 espaces.

	   1          2           3
    012345678901234567890123456789012
 0~~~~`~```~`~``~~~``~`~~~``~`~`~~~~~~`~~`0
 1~`~`~`~~`~```~~~~```~~~~`~`~`~~~~`~~`~`~1
 2 `~~~`T``3`~~~~`T`~~~~`````~~``~~~~``~~~2
 3``````````~~``````~~~`~``````~`~``~~``~~3
 4~`~~~~`~~`~~`T`~~`~~~~~~~`~~~~`~~~~``~~`4
     012345678901234567890123456789012
            1          2           3

(Dans uen vraie partie,  les trésors ne sont pas visibles.)

Appuie sur Entrée pour continuer...''')
                    input()

print('''Quand tu places un sonar directement sur un trésor, ce dernier est trouvé.
Les sonars se mettent alors à jour pour t'indiquer où est le deuxième trésor le plus proche.
Dans l'exemple ci-dessous, le sonar de droite indique donc 7
tandis que celui de gauche affiche X car la distance est trop grande.

          1             2                3
    0123456789012345678901234567890123456789012
 0~~~~`~`~~~~~~~~`~~~~`~~~~~`~~~~``~~~~~~~`~~~``~~0
 1 ~~~~~``~~~~~~``~`~~~~~~`~~~~~~`~~~~~~`~~~~`~~~`1
 2 `~~`~~X``7`~~~~`T`~~~~`````~~~``~~~``~~~~~`~~~`2
 3 ````````~~~~~`````~~~~``````~~~~~~`~`~`~`~`~``~3
 4~`~~~~~`~~`~~~~~~`~~~~`T`~~~`~~~~~`~~~~`~~`~~~~`4
    0123456789012345678901234567890123456789012
	  1             2                  3

Les trésors ne bougent pas. Les sonars peuvent les détecter jusqu'à une distance de 9 cases.

Essaie de déctecter les 3 trésors avant de ne plus avoir de sonars.
Bonne Chance !

Apppuie sur Entrée pour continuer....''')
input()



print('S O N A R !')
print()
print('Veux-tu lire les instructions (oui/non)?')
if input().lower().startswith('o'):
    def showInstructions (showInstructions):

        while True:
#Initatiation du jeu
            sonarDevices = 20
theBoard = getNewBoard()
theChests = getRandomChests(3)
drawBoard(theBoard)
previousMoves = []

while sonarDevices > 0:
		#Affiche combien il reste de sonars et de trésors
		print('Il te reste %s sonar(s) et %s trésor(s) à découvrir.'%(sonarDevices, len(theChests)))

		x, y = enterPlayerMove(previousMoves)
		previousMoves.append([x,y])# Pour mettre à jour les sonars

		moveResult = makeMove(theBoard, theChests, x, y)
		if moveResult == False:
			continue
		else:
			if moveResult == 'Tu as trouvé un des trésors !':
			 # Met à jour tous les sonars déjà placés
			 for x, y in previousMoves:
				 Makemove (theBoard, theChests, x, y)    
			     drawBoard(theBoard)
		    print(moveResult)

			if len(theChests) ==0:
				print('Tu as trouvé tous les trésors engloutis !','Bien joué , félicitations !')
				break

			sonarDevices -= 1

			if sonarDevices == 0:
				print('Tu es à court de sonars ! Fin du jeu !')
				print('Tu dois rentrer au port sans tes trésors .')
				print(' Voici  où étaient les trésors :')
				for x, y in theChest:
					print(' %s, %s' %(x,y))

				print('Veux-tu rejouer (oui/non) ?')
				if not input().lower().startwith('o'):
					sys.exit()
					break
