import pygame
import time
import math
import butt

pygame.init()
"""initialisations"""
pygame.init()

bgmenu = pygame.image.load("C:/Users/rosta\PycharmProjects/baby foot/foot.png")
soundmenu = pygame.mixer.Sound("C:/Users/rosta\PycharmProjects/baby foot/Music accueil.mp3")
soundgame = pygame.mixer.Sound("C:/Users/rosta\PycharmProjects/baby foot/Crowd.wav")
"""variables"""
music_counter = 2
a = "On"
music_counter2 = 2
a2 = "On"
"""creation écran"""
screen = pygame.display.set_mode((1205, 686))
"""Titre et icon"""
pygame.display.set_caption("Jeu de baby foot")
icon = pygame.image.load('C:/Users/rosta\PycharmProjects/baby foot/baby foot icon.png').convert_alpha()
pygame.display.set_icon(icon)
"""arriere plan"""

"""Texte titre"""
font = pygame.font.SysFont("Arial", 60)
txt = font.render('Jeu de Baby Foot', True, (0, 0, 0))
tx = 410
ty = 25


def musicstop():
    global music_counter
    global a
    if music_counter % 2 == 0:
        soundmenu.stop()
        a = "Off"
    else:
        a = "On"
        soundmenu.play(-1)
    music_counter += 1

def musicstop2():
    global music_counter2
    global a2
    if music_counter2 % 2 == 0:
        soundgame.stop()
        a2 = "Off"
    else:
        a2 = "On"
        soundgame.play(-1)
    music_counter2 += 1




bggame = pygame.image.load("C:/Users/rosta\PycharmProjects/baby foot/stadium.jpg")
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
        if ball.x < 160 and 245 < ball.y < 405:
            self.score[1] += 1
            partie.engagement()
            ball.change_x = 1.5
        if ball.x > 1040 and 245 < ball.y < 405:
            self.score[0] += 1
            partie.engagement()
            ball.change_x = -1.5
        font = pygame.font.SysFont("Arial", 60)
        txt1 = font.render(f'{self.score[0]} - {self.score[1]}', True, (0, 0, 0))
        screen.blit(txt1, (540, 7))


class Manette():
    def __init__(self):
        self.change_y = 0
        self.size = 7
        self.color = (0, 0, 0)
        self.color_players = (0, 0, 0)
        self.min = 85
        self.max = 565
        self.width = 20
        self.width_ = 18
        self.length = 25
        self.tir_ = [0, 0]
        self.rect = 0
        self.rect_posx = 0
        self.manette_info = {
            "manette0": {"equipe": 1, "posx": 175, "footballeur": 1, "posy0": 315, "max": 65, "pos": 0},
            "manette1": {"equipe": 1, "posx": 300, "footballeur": 2, "posy0": 235, "posy1": 395, "max": 150, "pos": 0},
            "manette2": {"equipe": 2, "posx": 420, "footballeur": 3, "posy0": 200, "posy1": 315, "posy2": 430,
                         "max": 115, "pos": 0},
            "manette3": {"equipe": 1, "posx": 540, "footballeur": 5, "posy0": 155, "posy1": 238, "posy2": 320,
                         "posy3": 401, "posy4": 475, "max": 70, "pos": 0},
            "manette4": {"equipe": 2, "posx": 650, "footballeur": 5, "posy0": 155, "posy1": 238, "posy2": 320,
                         "posy3": 401, "posy4": 475, "max": 70, "pos": 0},
            "manette5": {"equipe": 1, "posx": 780, "footballeur": 3, "posy0": 200, "posy1": 315, "posy2": 430,
                         "max": 115, "pos": 0},
            "manette6": {"equipe": 2, "posx": 900, "footballeur": 2, "posy0": 235, "posy1": 395, "max": 150, "pos": 0},
            "manette7": {"equipe": 2, "posx": 1015, "footballeur": 1, "posy0": 315, "max": 65, "pos": 0}}

    def manette(self, screen):
        for i in range(8):
            self.rect_posx = self.manette_info[f'manette{i}']["posx"] - 10
            if self.manette_info[f'manette{i}']["equipe"] == equipe.equipe:
                self.manette_info[f'manette{i}']["pos"] += self.change_y
            pygame.draw.line(screen, self.color, (self.manette_info[f'manette{i}']["posx"], self.min),
                             (self.manette_info[f'manette{i}']["posx"], self.max), self.size)
            for n in range(self.manette_info[f'manette{i}']["footballeur"]):
                if self.manette_info[f'manette{i}']["equipe"] == 1:
                    self.color_players = (0, 0, 255)
                elif self.manette_info[f'manette{i}']["equipe"] == 2:
                    self.color_players = (255, 0, 0)
                self.rect = pygame.Rect(self.rect_posx,
                                        self.manette_info[f'manette{i}'][f"posy{n}"] + self.manette_info[f'manette{i}'][
                                            "pos"], self.width, self.length)
                self.truerecttop = pygame.Rect(self.rect_posx + 1, self.manette_info[f'manette{i}'][f"posy{n}"] +
                                            self.manette_info[f'manette{i}']["pos"] - ball.size / 2, self.width_,
                                               (self.length + ball.size)/2)  # 1/4 of total rectangle

                self.truerectbot = pygame.Rect(self.rect_posx + 1, self.manette_info[f'manette{i}'][f"posy{n}"] +
                                               self.manette_info[f'manette{i}']["pos"] + self.length - ball.size, self.width_,
                                               (self.length + ball.size) / 2)  # 1/4 of total rectangle
                Manette.collision_joueur(self, screen)
            Manette.etirement_manette(self, screen)
            if self.manette_info[f'manette{i}']["pos"] + 20 > self.manette_info[f'manette{i}']["max"]:
                self.manette_info[f'manette{i}']["pos"] = self.manette_info[f'manette{i}']["max"] - 20
            elif self.manette_info[f'manette{i}']["pos"] - 10 < -self.manette_info[f'manette{i}']["max"]:
                self.manette_info[f'manette{i}']["pos"] = -self.manette_info[f'manette{i}']["max"] + 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if equipe.equipe == 1:
                        if event.key == pygame.K_LEFT:
                            self.width += 10
                    if equipe.equipe == 2:
                        if event.key == pygame.K_RIGHT:
                            self.width += 10
                            self.rect_posx -= 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.width = 20
                    if event.key == pygame.K_RIGHT:
                        self.width = 20
                        self.rect_posx = self.manette_info[f'manette{i}']["posx"] - 10


    def collision_joueur(self, screen):
        collide = self.rect.collidepoint(ball.x, ball.y)
        collidetop = self.truerecttop.collidepoint(ball.x, ball.y)
        collidebot = self.truerectbot.collidepoint(ball.x, ball.y)
        if collidetop == True:
            ball.change_x = - ball.change_x
            ball.change_y = - math.cos(ball.change_y) / 4  # This will change when we implement power*
        pygame.draw.ellipse(screen, self.color_players, self.truerecttop)
        if collidebot == True:
            ball.change_x = - ball.change_x
            ball.change_y = math.cos(ball.change_y) / 4  # This will change when we implement power*
        pygame.draw.ellipse(screen, self.color_players, self.truerectbot)
        if collide == True:
            ball.change_x = -ball.change_x
            ball.change_y = ball.change_y  # This will change when we implement power*
        pygame.draw.rect(screen, self.color_players, self.rect)


    def etirement_manette(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_y = -0.6
                if event.key == pygame.K_DOWN:
                    self.change_y = 0.6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.change_y = 0


class Ball():
    def __init__(self):
        self.x = 600
        self.y = 325
        self.change_x = 1.5
        self.change_y = 0
        self.size = 12
        self.color = (51, 25, 0)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def contact_mur(self):
        if self.x + self.size > 1052 or self.x - self.size < 148:
            self.change_x = -self.change_x
        if self.y + self.size > 550 or self.y - self.size < 100:
            self.change_y = -self.change_y

class Equipe():
    def __init__(self):
        self.equipe = 0
        self.color1 = (186, 186, 186)
        self.color2 = (186, 186, 186)
        self.color3 = (186, 186, 186)
    def choix_team(self, screen):
        bbleu = butt.Bouton.button_(screen, self.color1, (15, 15), " Equipe Bleu ")
        brouge = butt.Bouton.button_(screen, self.color2, (850, 15), " Equipe Rouge ")
        bstart = butt.Bouton.button_(screen, self.color3, (850, 600), " Commencer ")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bbleu.collidepoint(pygame.mouse.get_pos()):
                    self.equipe = 1
                    self.color1 = (0, 255, 255)
                    self.color2 = (186, 186, 186)

                if brouge.collidepoint(pygame.mouse.get_pos()):
                    self.equipe = 2
                    self.color2 = (255, 0, 0)
                    self.color1 = (186, 186, 186)
                if bstart.collidepoint(pygame.mouse.get_pos()):
                    self.color3 = (0, 255, 0)


ball = Ball()
manette = Manette()
partie = Partie()
equipe = Equipe()

class Game():
    screen = pygame.display.set_mode((1205, 686))
    pygame.display.set_caption("Jeu")
    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            partie.imagerie(screen)
            equipe.choix_team(screen)
            partie.calculer_score(screen)
            ball.move()
            manette.manette(screen)
            ball.draw(screen)
            ball.contact_mur()
            pygame.display.update()




