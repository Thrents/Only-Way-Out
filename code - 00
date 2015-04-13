# Only-Way-Out
Voila un début de code pour le projet. Cette partie servirait à charger une image.

" " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "

import pygame
import sys
import math
import random
from pygame.locals import *
tourelle = pygame.image.load ('tank.jpg')
herbe = pygame.image.load ('herbe.jpg')

def affichage_fenetre():
    """
    Fonction qui affiche une fenêtre avec une image de fond.
    """
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption(("Notre projet"))
    background = herbe
    screen.blit(background, (500, 200))
    screen.blit(tourelle, (500, 400))
    pygame.display.update()
affichage_fenetre()
