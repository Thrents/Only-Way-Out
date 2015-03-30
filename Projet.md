# Only-Way-Out
Voila un début de code pour le projet. Cette partie servirait à charger une image. Il y a deux lignes dont je ne comprend pas l'utilité mais elles étaient indiquées dans les tutos donc bon.

" " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
import pygame
import sys
import math
import random
from pygame.locals import *

def chargement_image(nom):
    """
    Fonction qui charge une image et qui retourne un objet image
    """
    try:
        image = pygame.image.load(nom)
        if image.get_alpha() is None:         ######
            image = image.convert()
        else:
            image = image.convert_alpha()     ######
    except:
        print("Impossible de charger l'image :", nom)
        raise SystemExit
    return image, image.get_rect()
