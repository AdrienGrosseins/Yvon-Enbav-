import pygame
import butt
from men import Game


class Choix_team():

    def __init__(self):
        self.equipe = 0

    def choix_team(self):
        color1 = (186, 186, 186)
        color2 = (186, 186, 186)
        color3 = (186, 186, 186)
        screen = pygame.display.set_mode((1205, 686))
        screen.fill((255, 255, 255))
        pygame.display.set_caption("Choix Equipe")
        run = True
        while run:
            bbleu = butt.Bouton.button_(screen, color1, (250, 200), " Equipe Bleu ")
            brouge = butt.Bouton.button_(screen, color2, (650, 200), " Equipe Rouge ")
            bstart = butt.Bouton.button_(screen, color3, (450, 500), " Commencer ")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bbleu.collidepoint(pygame.mouse.get_pos()):
                        self.equipe = 1
                        color1 = (0, 255, 255)
                        color2 = (186, 186, 186)

                    if brouge.collidepoint(pygame.mouse.get_pos()):
                        self.equipe = 2
                        color2 = (255, 0, 0)
                        color1 = (186, 186, 186)
                    if bstart.collidepoint(pygame.mouse.get_pos()):
                        color3 = (0, 255, 0)
                        def_equipe = Game()
                        def_equipe.run()
            pygame.display.update()