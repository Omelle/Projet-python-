# Creer un graphique avec pygame
import pygame,sys
from pygame.locals import *

# Initiale pygame
pygame.init()

# Configure la fenêtre.

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Bonjour tout le monde!')

# Configure les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configure la police de caractères.
basicFont = pygame.font.SysFont(None, 48)

#   Configure le texte.
text = basicFont.render('Bonjour tout le monde !, TRUE , WHITE, BLUE')
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().century

# Remplit de l'arrière-plan.
windowSurface.fill(WHITE)

# Dessiner une figure géométrique exemple polygone vert .
pygame.draw.polygon(windowSurface, GREEN, ((146, 0),
                    (291, 106), (236, 277), (56, 277), (0, 106)))

#Dessiner des lignes bleues.
pygame.draw.line(windowSurface, BLUE, (60,60), (120,60),4)
pygame.draw.line(windowSurface, BLUE,(120,60), (20,120))
pygame.draw.line(windowSurface, BLUE,(60,120), (120,120), 4)

#Dessine un cercle bleu.
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20,0)

#Dessiner une ellipse rouge.
pygame.draw.circle(windowSurface, RED, (300,250, 40, 80),1)

#Dessiner un rectangle d'arrière-plan du texte .
pygame.draw.rect(windowSurface, RED, (textRect.left-20, textRect.top-20, textRect. width-40, textRect.height+40)) # Ici on defini la largeur du rectangle et sa taille 

# Color le pixel.
pixArray = pygame.PixelArray(windowSurface)
pixArray [480][380] = BLACK
del pixArray

#Trace le texte.
windowSurface.blit(text, textRect)

#Affiche la fenêtre de l'écran 
pygame.display.update()

#Boucle principale .
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

