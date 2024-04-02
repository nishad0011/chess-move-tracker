from os import system
import pygame
from fentoboardimage import fenToImage, loadPiecesFolder

system('cls')

##Setup Pygame:
pygame.init()
width, height = 1080,650
screen = pygame.display.set_mode((width, height))

logo = pygame.image.load("./pieces_png/black/Pawn.png").convert_alpha()
pygame.display.set_caption('CamChess')
pygame.display.set_icon(logo)

clock = pygame.time.Clock()


image = fenToImage(
	fen="rnbqkbnr/pp3Qpp/2pp4/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR",
	squarelength= 50,
	pieceSet=loadPiecesFolder("./pieces_png",cache=True),
	darkColor="#D18B47",
	lightColor="#FFCE9E"
)
mode = image.mode
size = image.size
data = image.tobytes()

img = pygame.image.fromstring(data, size, mode)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(img,(0,0))
    pygame.display.update()


    clock.tick(60)
    print(clock.get_fps())
pygame.quit()