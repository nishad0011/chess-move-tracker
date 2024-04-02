import pygame

def initialize():
    ##Setup Pygame:
    pygame.init()
    width, height = 1000,650
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption('CamChess')
    logo = pygame.image.load("./pieces_png/black/Pawn.png").convert_alpha()
    pygame.display.set_icon(logo)
    return screen