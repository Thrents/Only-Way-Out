import pygame
from pygame.locals import *


pygame.init()
background = pygame.image.load('image-jeux.png')
jeep = pygame.image.load('jeep.png')

def affichage_fenetre():
    """
    Fonction qui affiche une fenêtre avec une image de fond.
    """
    fenetre = pygame.display.set_mode((1100, 720))
    pygame.display.set_caption("Only Way Out")
    background = pygame.image.load('image-jeux.png').convert()
    jeep = pygame.image.load('jeep.png').convert()

    obus_1 = pygame.image.load('obus_1.png').convert()
    obus_2 = pygame.image.load('obus_2.png').convert()
    obus_3 = pygame.image.load('obus_3.png').convert()
    obus_4 = pygame.image.load('obus_4.png').convert()

    image_de_fin = pygame.image.load('Game Over.jpg')
    victoire = pygame.image.load('victoire.jpg')

    while True:
        fenetre.blit(background, (0, 0))
        background.blit(jeep, (145, 560))
        pygame.display.flip() #On rafraichie la fenêtre.
    jeep_position = [56, 688]

    return jeep_position, background, obus_1, obus_2, obus_3, obus_4

def moveup(jeep_position):
    jepp_position[1] += 10
    background.blit(jeep, (jeep_position))
    pygame.display.flip()
    return jeep_position #Sinon les modifications ne seront pas prises en compte par les autres fonctions.


def movedown(jeep_position):
    background.move(0, -10)
    jepp_position[1] -= 10
    return jeep_position


def moveleft(jeep_position):
    background.move(-10, 0)
    jepp_position[0] -= 10
    return jeep_position


def moveright(jeep_position):
    background.move(10, 0)
    jepp_position[0] += 10
    return jeep_position


def mouvement():
    """
    Fonction qui gère les déplacements du personnage.
    """
    continuer = 1    
    
    while continuer == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveup(jeep_position)
                    pygame.display.update()
                if event.key == K_DOWN:
                    movedown(jeep_position)
                    pygame.display.update()
                if event.key == K_RIGHT:
                    moveright(jeep_position)
                    pygame.display.update()
                if event.key == K_LEFT:
                    moveleft(jeep_position)
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
    
    tank_bas = [[108,609], [321,611], [205,548], [118,412], [71,375], 
    [531,341], [746,532], [335,78]]
    
    tank_haut = [[30,710], [203,686], [205,528], [174,474], [232,475], 
    [93,455], [90,266], [152,275], [322,408], [447,441], [608,440], 
    [666,412], [734,473], [727,644], [894,613], [830,408], [707,344], 
    [798,273], [669,271], [417,269], [754,150], [561,146], [464,140], 
    [262,186], [145,80], [59,84]]
    
    tank_gauche = [[367,654], [320,439], [427,536], [596,585], [425,341], 
    [952,562], [930,455], [654,200], [415,150], [155,165], [974,420], 
    [980,303], [960,167], [322,25], [450,25], [647,25]]
    
    tank_droite = [[23,654], [99,664], [253,310], [562,509], [505,446], 
    [832,343], [754,205], [345,206], [928,358]]

    bunker_haut = [[266,705], [449,703], [531,705], [779,422], [737,283], 
    [382,305], [208,280], [508,61]]
    
    bunker_bas = [[497,503], [161,377], [245,378], [893,380], [454,187], 
    [88,126], [840,17], [257,54]]
    
    bunker_gauche = [[222,616], [717,536], [494,460], [572,412], [974,232], 
    [905,135], [971,85], [976,18], [1085,123], [1085,150], [1085,181]]
    
    bunker_droit = [[26,609], [408,652], [826,638], [822,533], [50,495], 
    [528,272], [830,198], [191,151], [662,89], [61,23]]

    return tank_bas, tank_haut, tank_gauche, tank_droite, bunker_haut, 
    bunker_bas, bunker_gauche, bunker_droit


def tir_bas(obus_1,  tank_bas):
    """
    variation des positions des image obus pour les tirs.
    """
    while True:
        for tankb in tank_bas:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_1, (tankb))
                pygame.display.flip()
                obus_1_position = tankb
            if temps % 50 == 0:
                obus_1_position[1] -= 30 
                background.blit(obus_1, (obus_1_position))
                pygame.display.flip()

def tir_haut(obus_2,  tank_haut):

    while True:
        for tankh in tank_haut:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_2, (tankh))
                pygame.display.flip()
                obus_2_position = tankh 
            if temps % 50 == 0:
                obus_2_position[1] += 30
                background.blit(obus_1, (obus_1_position))
                pygame.display.flip()


def tir_gauche(obus_3,  tank_gauche):

    while True:
        for tankg in tank_gauche:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_3, (tankg))
                pygame.display.flip()
                obus_3_position = tankg 
            if temps % 50 == 0:
                obus_3_position[0] -= 30
                background.blit(obus_3, (obus_3_position))
                pygame.display.flip()


def tir_droite(obus_4,  tank_droite):

    while True:
        for tankd in tank_droite:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_4, (tankd))
                pygame.display.flip()
                obus_4_position = tankd 
            if temps % 50 == 0:
                obus_4_position[0] += 30
                background.blit(obus_4, (obus_4_position))
                pygame.display.flip()

def tir_bunker_bas(obus_1,  bunker_bas):
    while True:
        for bunkerb in bunker_bas:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_1(bunkerb))
                pygame.display.flip()
                obus_bunker_1_position = bunkerb
            if temps % 500 == 0:
                obus_bunker_1_position[1] -= 50
                background.blit(obus_1, (obus_2_position))
                pygame.display.flip()

def tir_bunker_haut(obus_2,  bunker_haut):
    while True:
        for bunkerh in bunker_haut:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_2(bunkerh))
                pygame.display.flip()
                obus_bunker_2_position = bunkerh
            if temps % 500 == 0:
                obus_bunker_2_position[1] += 50
                background.blit(obus_2, (obus_2_position))
                pygame.display.flip()


def tir_bunker_gauche(obus_3,  bunker_gauche):
    while True:
        for bunkerg in bunker_gauche:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_3(bunkerg))
                pygame.display.flip()
                obus_bunker_3_position = bunkerg
            if temps % 500 == 0:
                obus_bunker_3_position[0] -= 50
                background.blit(obus_3, (obus_3_position))
                pygame.display.flip()

def tir_bunker_droite(obus_4,  bunker_droit):
    while True:
        for bunkerd in bunker_droite:
            temps = pygame.time.get_ticks()
            if temps % 2000 == 0:
                background.blit(obus_4(bunkerd))
                pygame.display.flip()
                obus_bunker_3_position = bunkerd
            if temps % 500 == 0:
                obus_bunker_4_position[0] += 50
                background.blit(obus_4, (obus_4_position))
                pygame.display.flip()
            

  def delimitation():
    """
    Délimitation des zones interdites au joueur.
    """
    delimitation_1 = [1, 2, 3, 4]
    for coordonnees in delimitation_1:
        if jeep_position[0] == coordonnees and jeep_position[1] == coordonees:
            continuer = 0
            pygame.quit()
  
    if 0 <= X <= 10:
       * action choisie *
    if 0 <= Y <= 5:
       * action choisie  
    if 1097 <= X <= 1100:
       * action choisie *
    if 715 <= Y <= 720:
       * action choisie *
  
    X = jeep_position[0]
    Y = jeep_position[1]

    if 31 <= X <= 73 and 256 <= Y <= 285:
        * action choisie *
  
    if 85 <= X <= 127 and 78 <= Y <= 107:
        * action choisie *
  
    if 469 <= X <= 479 and 480 <= Y <= 720:
        * action choisie *

    if 269 <= X <= 479 and 480 <= Y <= 515:
        * action choisie *
  
    if 423 <= X <= 434 and 71 <= Y <= 121:
        * action choisie *
  
    if 487 <= X <= 529 and 131 <= Y <= 160:
        * action choisie *
  
    if 692 <= X <= 734 and 139 <= Y <= 168:
        * action choisie *
  
    if 924 <= X <= 935 and 143 <= Y <= 193:
        * action choisie *
  
    if 857 <= X <= 868 and 28 <= Y <= 60:
        * action choisie *
  
    if 911 <= X <= 922 and 28 <= Y <= 60:
        * action choisie *
  
    if 857 <= X <= 922 and 0 <= Y <= 28:
        * action choisie *
  
    if 924 <= X <= 935 and 143 <= Y <= 193:
        * action choisie *
  
  #Pour le long tunnel 
  
    if 558 <= X <= 705 and 600 <= Y <= 629:
        * action choisie *
  
    if 558 <= X <= 656 and 649 <= Y <= 678:
        * action choisie *
  
    if 694 <= X <= 705 and 630 <= Y <= 689:
        * action choisie *
  
    if 645 <= X <= 656 and 679 <= Y <= 719:
        * action choisie *
  
    if 657 <= X <= 1086 and 708 <= Y <= 719:
        * action choisie *
  
    if 706 <= X <= 1041 and 660 <= Y <= 689:
        * action choisie *
  
    if 1030 <= X <= 1041 and 193 <= Y <= 659:
        * action choisie *
  
    if 1075 <= X <= 1086 and 201 <= Y <= 707:
        * action choisie *


  
def fin_jeu():
    """
    fonction qui vérifie si le jeu doit se terminer.
    """
    position_fin_hauteur = [1050 , 1051 , 1052 , 1053 , 1054 , 1055 , 1056 , 
                            1057 , 1058 , 1059 , 1060]
    position_fin_longueur = [40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 
                             49 , 50]    
    
    
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
                temps_victoire = pygame.time.get_ticks()
                while temps_victoire % 2000 != 0: 
                    pygame.blit(victoire(0,0))



def main():
    """
    Fonction principale du programme
    """
    jeep_position, background, obus_1, obus_2, obus_3, obus_4 = affichage_fenetre()
    while continuer == 1:
        mouvement()
        if continuer == 0:
            temps_defaite = pygame.time.get_ticks()
            while temps_defaite % 2000 !=0:
                background.blit(image_de_fin(0,0))
