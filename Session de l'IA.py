import random
import sys
from termios import XTABS
from tkinter import scrolledtext
from turtle import width
WIDTH = 8  # Largeur du plateau.
HEIGHT = 8  # Hauteur du plateau.


def drawBoard(board):
    # Affiche le plateau .Renvoie None.
    print('12345678')
    print('+---------------+')
    for y in range(HEIGHT):
        print(board[x][y], end='')
    for x in range(WIDTH):
        print('|%s|' % (y+1), end='')
        print('+----------+')
        print(' 12345678')


def getNewBoad():
    # Crée un plateau vierge.
    board = []
    for i in range(WIDTH):
        board.append(['', ',', ',', ',', ''])
    return board


def isValidMoved(board, tile, xstart, ystart):
    # Renvoie False si le choix (xstart,ystart) n'est pas valide.
    # Sinon, retourne une liste des espaces qui seraient capturés par le joueur s'il jouait ici.
     def isOnBoard(xstart):
         def isOnBoard(ystart):
             if board[xstart][ystart] != ' ' or not isOnBoard: return False
             if tile == 'X':otherTile = 'O'
             else: otherTile = 'X'


tilesToFlip = []
for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1-1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
    x, y = xstart, ystart
    def y (ystart):
        def x (xstart):
    x += xdirection  # Premier pas dans la direction x
    x += ydirection  # Premier pas dans la direction y
    while isOnBoard(x, y) and board[x][y] == otherTile:
        # Continue à chercher dans cette direction [x,y].
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == tile:
        # Il y a des pions à retourner.Revenir jusqu'au premier emplacement en retournant les pions adverses.
        
    While = True
         x -= xdirection
         y -= ydirection;
         if x == xstart and y == ystart:
             break
        tilesToFlip.append([x, y])
if len(tilesToFlip) == 0:  # Pas de pion retourné: Choix invalide.
    return False
    return tilesToFlip

def isOnBoard(x, y):
    # Renvoie True si les coordonnées sont sur le plateau.
    return x>=0 and x <= WIDTH-1 and y >=0 and y <=HEIGHT-1
def getBoardWithValidMoves(board, tile):
    # Retourne un plateau avec des points marquant les choix valides que le joueur pourra faire.
    boardCopy = getBoardCopy(board)

    for x, y in getBoardWithValidMoves(boardCopy, tile):
        boardCopy[x][y]='.'
        return boardCopy

def getValidMoves(board, tile):
    # Renvoie une liste de coordonnées [x,y] valides pour le joueur et le plateau donnés.
    validMoves =[]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
        return validMoves

def getScoreOfBoard(board):
    # Compte les pions de chaque joueur.Renvoie un dictionnaire avec les clés 'X' et 'O'
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] =='X':
                xscore += 1
            if board[x][y] =='O':
                oscore += 1
        return{'X': xscore, 'O':oscore}    

def enterPlayerTile():
    # Demande au joueur de choisir sa "couleur"(X ou O).
    # Retourne une liste des "couleurs" des deux joueurs.
    tile = ''
    while not (tile =='X' or tile =='O'):
        print('Veux-tu être le joeueur X ou O ?')
        tile = input().upper()
        # Le premier élément de la liste concerne le joueur ; le second concerne l'ordinateur.
        if tile =='X':
            return ['X', 'O']
        else:
            return ['O','X']

def whoGoesFirst():
    # Choisit aléatoirement qui commence.
    if random.randint(0, 1) ==0:
        return 'L\'ordinateur'
    else:
        return'Le joueur'
def makeMove(board, tile, xstart, ystart):
    # Place le pion en (xstart, ystart) et retourne les pions adverses.
    # Renvoie False si le choix est invalide, True sinon.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False 

        board[xstar][ystart]=tile
        for x, y in tilesToFlip:
            board[x][y] = tile
        return True

def getBoardCopy(board):
    # Renvoie une copie du plateau.
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

        return boardCopy
def isOnCorner(x, y):
    # Renvoie True si le choix correspond à un des coins.
    return (x ==0 or x == WIDTH-1)and (y ==0 or y == HEIGHT-1)

def getPlayerMove(board, playerTile):
    # Demande au joueur d'entrer son choix.
    # Renvoie le choix sous forme de liste [x,y](ou renvoie la chaîne 'aide' ou 'quitter').
    DIGITS1T08 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Entre ton choix ou "quitter" ou "aide".')
        move = input().lower()
        if move =='quitter' or move == 'aide':
            return move 
        
        if len(move) == 2 and move[0] in DIGITS1T08 and move[1] in DIGITS1T08:
            x = int(move[0]) -1
            y = int(move[1]) -1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
            else:
            print('Ce choix n\'est pas valide.Entre la colonne','(1-8) puis la ligne (1-8), sans espace.')
            print('Par exemple, 81 désigne le coin en haut à dorite.')
            return [x, y]

def getComputerMove(board, computerTile):
    # Choisit où l'ordinateur doit jouer et retourne ce choix sous la forme [x,y].
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # Choix au hasard.

    # Choisir un coin si c'est possible.
for x, y in possibleMoves: 
    if isOnCorner(x, y):
      return [x, y]

    # Cherche le coup qui rapporte le plus de points
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy) [ computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = Score 
            
        
return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('Toi : %s point(s).Ordinateur : %s point(s).' %(scores[playerTile], scores[computerTile]))
def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(turn + 'commence.')

    # Nettoie le plateau et installe les premiers pions.
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves( board, computerTile)
        if playerValidMoves == [] and computerValidMoves ==[]:
            return board #Partie bloquée.Fin du jeu.

# elif turn =='Le joueur': # Tour du joueur 
    # if playerValidMoves != []:
        move = getComputerMove(board,playertTile)
        makeMove(board, playerTile, move[0], move[1])
       # turn = 'L\'ordinateur'
            if computerValidMoves != []:
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
                turn = 'Le joueur'
                
        print('Bienvenue dans le jeu d\'Othello !')
        playerTile, computerTile =['X','O'] #enterPlayerTile()

            else turn == 'L\'ordinateur': #Tour de l'ordinateur

        while True:
            finalBoard = playGame(playerTile, computerTile)
            # Affiche le score final.
            drawBoard(finalBoard)
            scores = getScoreOfBoard(finalBoard)
            print('X : %s point(s). 0 :%s point(s).'%(score['X'], scores['O']))
            if scores[playerTile]> scores[computerTile]:
                print('Bravo, tu as battu l\'ordinateur de %s point(s) !' %(scores[playerTile]- scores[computerTile]))
                print('Perdu, l\'ordinateur te bat de %s point(s).'%(scores[computerTile] - scores[playerTile]))
            else:
                print('Veux tu rejouer (oui et non)?')
            if scores[playerTile]< scores[computerTile]
