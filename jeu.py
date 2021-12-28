import pygame
import ball
import time

bggame = pygame.image.load("./stadium.jpg")

class Partie():
    def __init__(self):
        self.gagnant = []
        self.nb_joueur = 8
        self.score = [0, 0]
        self.but1x = (1052, 245)
        self.but1y = (1052, 405)
        self.but2x = (148, 245)
        self.but2y = (148, 405)

    def imagerie(self, screen):
        """stadium"""
        screen.blit(bggame, (0, 0))
        """score"""
        pygame.draw.rect(screen, (255, 255, 255), (520, 7, 160, 65))
        """Field"""
        pygame.draw.line(screen, (255, 255, 255), (143, 95), (1057, 95), 15)
        pygame.draw.line(screen, (255, 255, 255), (150, 95), (150, 555), 15)
        pygame.draw.line(screen, (255, 255, 255), (143, 555), (1057, 555), 15)
        pygame.draw.line(screen, (255, 255, 255), (1050, 95), (1050, 555), 15)
        pygame.draw.rect(screen, (0, 150, 0), (150, 95, 900, 460))
        pygame.draw.line(screen, (255, 255, 255), (600, 95), (600, 245), 7)
        pygame.draw.line(screen, (255, 255, 255), (600, 555), (600, 405), 7)
        pygame.draw.circle(screen, (255, 255, 255), (600, 325), 80, 7)
        pygame.draw.circle(screen, (255, 255, 255), (600, 325), 7, 7)
        pygame.draw.line(screen, (255, 255, 255), (150, 245), (250, 245), 7)
        pygame.draw.line(screen, (255, 255, 255), (150, 405), (250, 405), 7)
        pygame.draw.line(screen, (255, 255, 255), (250, 245), (250, 405), 7)
        pygame.draw.line(screen, (255, 255, 255), (1050, 245), (950, 245), 7)
        pygame.draw.line(screen, (255, 255, 255), (1050, 405), (950, 405), 7)
        pygame.draw.line(screen, (255, 255, 255), (950, 245), (950, 405), 7)
        pygame.draw.line(screen, (255, 0, 0), self.but1x, self.but1y, 7)
        pygame.draw.line(screen, (255, 0, 0), self.but2x, self.but2y, 7)

    def engagement(self):
        screen = pygame.display.set_mode((1205, 686))
        time.sleep(1.5)
        font = pygame.font.SysFont("Arial", 120)
        if self.score[0] == 10:
            txt1 = font.render("Equipe Rouge gagne", True, (0, 0, 0))
            screen.blit(txt1, (240, 240))
        if self.score[1] == 10:
            txt2 = font.render("Equipe bleu gagne", True, (0, 0, 0))
            screen.blit(txt2, (240, 240))
            quit()
        ball.x = 600
        ball.y = 325
        ball.change_y = 0

    def calculer_score(self, screen):
        if ball.x < 190 and 245 < ball.y < 405:
            self.score[1] += 1
            partie.engagement()
            ball.change_x = 1.5
        if ball.x > 1000 and 245 < ball.y < 405:
            self.score[0] += 1
            partie.engagement()
            ball.change_x = -1.5
        font = pygame.font.SysFont("Arial", 60)
        txt1 = font.render(f'{self.score[0]} - {self.score[1]}', True, (0, 0, 0))
        screen.blit(txt1, (540, 7))

ball = ball.Ball()
partie = Partie()