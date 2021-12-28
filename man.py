import pygame
import ball
import math
import jeu
import network
import team

class Manette():
    def __init__(self):
        self.change_y = 0
        self.size = 7
        self.color = [0, 0, 0]
        self.min = 85
        self.max = 565
        self.width = 20
        self.width_ = 18
        self.length = 30
        self.rect = 0
        self.truerect = 0
        self.rect_posx = 0
        self.pos = []
        self.manette_info = {
    "manette0": {"equipe": 1, "posx": 175, "footballeur": 1, "posy0": 315, "max": 65, "pos": 0},
    "manette1": {"equipe": 1, "posx": 300, "footballeur": 2, "posy0": 235, "posy1": 395, "max": 150, "pos": 0},
    "manette2": {"equipe": 2, "posx": 420, "footballeur": 3, "posy0": 200, "posy1": 315, "posy2": 430, "max": 115, "pos": 0},
    "manette3": {"equipe": 1, "posx": 540, "footballeur": 5, "posy0": 155, "posy1": 238, "posy2": 320, "posy3": 401, "posy4": 475, "max": 70, "pos": 0},
    "manette4": {"equipe": 2, "posx": 650, "footballeur": 5, "posy0": 155, "posy1": 238, "posy2": 320, "posy3": 401, "posy4": 475, "max": 70, "pos": 0},
    "manette5": {"equipe": 1, "posx": 780, "footballeur": 3, "posy0": 200, "posy1": 315, "posy2": 430, "max": 115, "pos": 0},
    "manette6": {"equipe": 2, "posx": 900, "footballeur": 2, "posy0": 235, "posy1": 395, "max": 150, "pos": 0},
    "manette7": {"equipe": 2, "posx": 1015, "footballeur": 1, "posy0": 315, "max": 65, "pos": 0}}


    def manette(self, screen):
        Manette.etirement_manette(self, screen)
        ball.move()
        ball.draw(screen)
        ball.contact_mur()
        for i in range(8):
            self.rect_posx = self.manette_info[f'manette{i}']["posx"] - 10
            if self.manette_info[f'manette{i}']["equipe"] == 1:
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
                                               (self.length + ball.size) / 2)  # 1/4 of total rectangle

                self.truerectbot = pygame.Rect(self.rect_posx + 1, self.manette_info[f'manette{i}'][f"posy{n}"] +
                                               self.manette_info[f'manette{i}']["pos"] + self.length - ball.size,
                                               self.width_,
                                               (self.length + ball.size) / 2)  # 1/4 of total rectangle

                Manette.collision_joueur(self, screen)
            if self.manette_info[f'manette{i}']["pos"] + 20 > self.manette_info[f'manette{i}']["max"]:
                self.manette_info[f'manette{i}']["pos"] = self.manette_info[f'manette{i}']["max"] - 20
            elif self.manette_info[f'manette{i}']["pos"] - 10 < -self.manette_info[f'manette{i}']["max"]:
                self.manette_info[f'manette{i}']["pos"] = -self.manette_info[f'manette{i}']["max"] + 10
        """self.manette_info[f'manette{i}']["pos"], ball.x, ball.y, partie.score[0], partie.score[1] = self.parse_data(
            self.send_data())"""

    """def tir(self):
        global equipe
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if equipe == 1:
                    if event.key == pygame.K_LEFT:
                        self.width += 0
                    if event.key == pygame.K_RIGHT:
                        self.width += 10
                if equipe == 2:
                    if event.key == pygame.K_LEFT:
                        self.width += 10
                        self.rect_posx -= 10
                    if event.key == pygame.K_RIGHT:
                        self.width += 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.width -= 10
                if event.key == pygame.K_RIGHT:
                    self.width -= 10
                    self.rect_posx += 10"""

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

    """def send_data(self):
        data = str(net.id) + ":" + str(self.manette_info[f'manette0']["pos"]) + "," + str(ball.x) + "," + str(
            ball.y) + "," + str(partie.score[0]) + "," + str(partie.score[1])
        reply = net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")[2].split(",")[3].split(",")[4].split(",")
            return int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4])
        except:
            return 0, 0, 0, 0, 0"""



ball = ball.Ball()
partie = jeu.Partie()
net = network.Network()