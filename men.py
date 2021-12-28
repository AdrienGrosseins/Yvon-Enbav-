import pygame
import jeu
import butt
import ball
import man

pygame.init()
"""initialisations"""
pygame.init()

bgmenu = pygame.image.load("./foot.png")
soundmenu = pygame.mixer.Sound("./Music accueil.mp3")
soundgame = pygame.mixer.Sound("./Crowd.wav")
"""creation écran"""
screen = pygame.display.set_mode((1205, 686))
"""Titre et icon"""
pygame.display.set_caption("Jeu de baby foot")
icon = pygame.image.load('./baby foot icon.png').convert_alpha()
pygame.display.set_icon(icon)
"""arriere plan"""

"""Texte titre"""
font = pygame.font.SysFont("Arial", 60)
txt = font.render('Jeu de Baby Foot', True, (0, 0, 0))
tx = 410
ty = 25



ball = ball.Ball()
manette = man.Manette()
partie = jeu.Partie()

class Game():
    screen = pygame.display.set_mode((1205, 686))
    pygame.display.set_caption("Jeu")
    def run(self):
        run = True
        while run:
            partie.imagerie(screen)
            partie.calculer_score(screen)
            manette.manette(screen)
            pygame.display.update()