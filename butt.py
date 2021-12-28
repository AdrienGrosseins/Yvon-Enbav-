import pygame
"""definition du boutton"""
class Bouton():

    def button_(screen, color, position, text):
        font = pygame.font.SysFont("Arial", 50)
        text_render = font.render(text, True, (0, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x + w, y), 5)
        pygame.draw.line(screen, (0, 0, 0), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (0, 0, 0), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(screen, (0, 0, 0), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(screen, color, (x, y, w, h))
        return screen.blit(text_render, (x, y))