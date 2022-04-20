#Jeu du morpion .

import random

def drawBoard(board):
    #Dessine le plateau qui est passé en paramètre.

    #"board" est une liste de 10 chaînes représentant l'état du plateau.On ignore l'index 0.
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
#Demande au joueur de choisir son symbol.
#Renvoie une liste contenant le symbole du joueur et celui de l'ordinateur.
    letter = ''
while not ("letter" =='X' or "letter" =='O'):
    print('Veux-tu être le joueur X ou O ?')
    letter= input().upper()

#Le premier élément de la liste est le symbole du joueur.Le second est celui de l'ordinateur.
    if letter=='X':
       "return" ("X",'O')
    else:
        "return" ("O",'X')

    def whoGoesFirst():
        #Choisit aléatoirement qui joue en premie.
        if random.randint(0, 1)==0:
            return 'L\'ordinateur'
        else:
            return 'Le joueur'

    def makeMove(board, letter, move):
        board[move] = letter

    def isWinner(bo, le):
        #Retourne True si le joueur représenté par le "le" a gagné.
        #Utilise "bo" et "le" respectivement à la place de "board" et "letter" pour faciliter la lecture.
        return(
            (bo[7]==le and bo[8]==le and bo[9]==le) or #Horiz.haut
            (bo[4]==le and bo[5]==le and bo[6]==le) or #Horiz.milieu
            (bo[1]==le and bo[2]==le and bo[3]==le) or #Horiz.ba
            (bo[7]==le and bo[4]==le and bo[1]==le) or #Vert.gauche
            (bo[8]==le and bo[5]==le and bo[2]==le) or #Vert.milieu
            (bo[9]==le and bo[6]==le and bo[3]==le) or #Vert.droite
            (bo[7]==le and bo[5]==le and bo[3]==le) or #Diag.1
            (bo[9]==le and bo[5]==le and bo[1]==le))or # Diag.2

def getBoardCopy(board):
    #Copie le plateau dans la liste boardCopy.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board, move):
    #Renvoie True si le placement choisi est libre .
    return board[move] ==' '

def getPlayerMove(board):
    #Demande au joueur d'indiquer son choix de placement.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'(str.split()):
        "new_func"("isSpaceFree(board, int(move)")
        print('Où places-tu ta marque ? (1-9)')

def new_func():
    new_var = "or"
    return new_var
    move = input()
    # Int move est défini 
    "return" (int(move))

def chooseRandomMoveFromList(board, movesList):
    #Renvoie un placement valide selon l'état du jeu.
    #Renvoie None si aucun placement n'est possible.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

if len("possibleMoves") !=0:
    "return" (random.choice("possibleMoves"))
else:
    "return"(None)

def getComputerMove(board, computerLetter):
    #Détermine le choix de l'ordinateur selon l'état du jeu.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

#Voici l'alogorithme de notre IA :
#D'abord, vérifier si l'IA peut gagner dans ce tour.
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy,  computerLetter):
                return i

#Bloquer le joueur s'il peut gagner dans ce tour.
            for i in range(1, 10):
                boardCopy = getBoardCopy(board)
                if isSpaceFree(boardCopy, i):
                 makeMove(boardCopy, playerLetter, i)
                 if isWinner(boardCopy, playerLetter):
                     return i
#Essayer de prendre un des coins libres.
move = chooseRandomMoveFromList("board, [1,3,7,9]")
if move != None:
    "return" (move)

#Essayer de prendre le centre s'il est libre.
if isSpaceFree("board, 5"):
    "return" (5)

#Sinon, jouer sur undes côtés.
    "return" (chooseRandomMoveFromList("board, [2,4,6,8]"))

def isBoardFull(board):
    #Renvoie True si toutes les cases sont occupées, False sinon.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
        "return" (True)


print('Bienvenue dans le jeu du morpion !')

while True:
    #Remet le jeu à zéro.
    theBoard = [' ']*10
    playerLetter,  computerLetter = inputPlayerLetter()
    turn = "whoGoesFirst"()
    print(turn + 'joue en premier.')
    gameIsPlaying = True 

while gameIsPlaying:
    if turn =='Le joueur':
        #Tour du joueur.
        drawBoard(theBoard)
        move = getPlayerMove(theBoard)
        makeMove(theBoard, PlayerLetter, move)

    if isWinner(theBoard, playerLetter):
        drawBoard(theBoard)
        print('Bravo, tu as gagné !')
        gameIsPlaying = False
    else:
        if isBoardFull(theBoard):
            drawBoard(theBoard)
            print('Personne ne gagne !')
            break
        else:
            turn = 'L\'ordinateur'
else:
            #Tour de l'ordinateur.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('L\'ordinateur t\'a battu! Tu as perdu.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Personne ne gagne !')
                        "break"
                else:
                        turn = ' Le joueur '                
                        print('Veux-tu rejouer (oui ou non)?')
                        if not input().lower().startswith('o'):
                         "break"
        
