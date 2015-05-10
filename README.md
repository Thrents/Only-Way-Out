import pygame
from pygame
fond = pygame.image.load('image-jeux.png')
jeep = pygame.image.load('jeep.png')
obus_1 = pygame.image.load('obus_1.png')
obus_2 = pygame.image.load('obus_2.png')
obus_3 = pygame.image.load('obus_3.png')
obus_4 = pygame.image.load('obus_4.png')
image_de_fin = pygame.image.load('Game Over.jpg')
victoire = pygame.image.load('victoire.jpg')
jeep_position = [56,688]


def affichage_fenetre():
    """
    Fonction qui affiche une fenêtre avec une image de fond.
    """
    pygame.init()
    pygame.display.set_mode((1100, 920))
    pygame.display.set_caption(("Only Way Out"))
    pygame.blit(fond(0,0))
    pygame.blit(jeep(jeep_position))
    pygame.display.update()

affichage_fenetre()

def moveup():
    fond.move(0, 10)
    jeep_position[1] += 10


def movedown():
    fond.move(0, -10)
    jeep_position[1] -= 10


def moveleft():
    fond.move(-10, 0)
    jeep_position[0] -= 10


def moveright():
    fond.move(10, 0)
    jeep_position[0] += 10


def mouvement():
    """
    Fonction qui gère les déplacements du personnage.
    """
    continuer = 1    
    
    while continuer == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveup()
                    pygame.display.update()
                if event.key == K_DOWN:
                    movedown()
                    pygame.display.update()
                if event.key == K_RIGHT:
                    moveright()
                    pygame.display.update()
                if event.key == K_LEFT:
                    moveleft()
                    pygame.display.update()
                if (evenement.key == K_ESCAPE):
                    continuer = 0
                    pygame.quit() # On quitte le programme.
                    
                pygame.display.update()
    return continuer

def liste_tank_et_bunker():
    """
    Fonction qui n'a pas de rôle particulier mais qui permet de 
    regrouper toutes les liste de tuples des différents types de
    tourelles.
    """
    
    tank_bas = [(108,609), (321,611), (205,548), (118,412), (71,375), (531,341), (746,532), (335,78)]    
    tank_haut = [(30,710), (203,686), (205,528), (174,474), (232,475), (93,455), (90,266), (152,275), (322,408), (447,441), (608,440), (666,412), (734,473), (727,644), (894,613), (830,408), (707,344), (798,273), (669,271), (417,269), (754,150), (561,146), (464,140), (262,186), (145,80), (59,84)]
    tank_gauche = [(367,654), (320,439), (427,536), (596,585), (425,341), (952,562), (930,455), (654,200), (415,150), (155,165), (974,420), (980,303), (960,167), (322,25), (450,25), (647,25)]
    tank_droite = [(23,654), (99,664), (253,310), (562,509), (505,446), (832,343), (754,205), (345,206), (928,358)]

    bunker_haut = [(266,705), (449,703), (531,705), (779,422), (737,283), (382,305), (208,280), (508,61)]
    bunker_bas = [(497,503), (161,377), (245,378), (893,380), (454,187), (88,126), (840,17), (257,54)]
    bunker_gauche = [(222,616), (717,536), (494,460), (572,412), (974,232), (905,135), (971,85), (976,18), (1085,123), (1085,150), (1085,181)]
    bunker_droit = [(26,609), (408,652), (826,638), (822,533), (50,495), (528,272), (830,198), (191,151), (662,89), (61,23)]

    return tank_bas, tank_haut, tank_gauche, tank_droite, bunker_haut, bunker_bas, bunker_gauche, bunker_droit


def tir_bas():
    """
    variation des positions des image obus pour les tirs.
    """
    while True:
        for tankb in tank_bas:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                pygame.image.load(obus_1(tankb))
                obus_1_position = tankb
            if temps % 500 == 0:
                obus_1_position.move(0, -30)

def tir_haut():

    while True:
        for tankh in tank_haut:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                pygame.image.load(obus_2(tankh))
                obus_2_position = tankh 
            if temps % 500 == 0:
                obus_2_position.move(0, 30)


def tir_gauche():

    while True:
        for tankg in tank_gauche:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                pygame.image.load(obus_3(tankg))
                obus_3_position = tankg 
            if temps % 500 == 0:
                obus_3_position.move(-30, 0)


def tir_droite():

    while True:
        for tankd in tank_droite:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                pygame.image.load(obus_4(tankd))
                obus_4_position = tankd 
            if temps % 500 == 0:
                obus_4_position.move(0, 30)
            
            
def fin_jeu():
    """
    fonction qui vérifie si le jeu doit se terminer.
    """
    position_fin_hauteur = [1050 , 1051 , 1052 , 1053 , 1054 , 1055 , 1056 , 1057 , 1058 , 1059 , 1060]
    position_fin_longueur = [40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50]    
    
    
    if obus_1_position == jeep_position:
        pygame.blit(image_de_fin(0,0))
        pygame.quit()
    
    elif obus_2_position == jeep_position:
        pygame.blit(image_de_fin(0,0))
        pygame.quit()
    
    elif obus_3_position == jeep_position:
        pygame.blit(image_de_fin(0,0))
        pygame.quit()
    
    elif obus_4_position == jeep_position:
        pygame.blit(image_de_fin(0,0))
        pygame.quit()


    for h in position_fin_hauteur:
        for l in position_fin_longueur:
            if (jeep_position[0] == h) and (jeep_position[1] == l):
                pygame.blit(victoire(0,0))
                pygame.quit()
