from os import system
import pygame
from fentoboardimage import fenToImage, loadPiecesFolder

system('cls')

##Setup Pygame:
pygame.init()
width, height = 400,400
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()


image = fenToImage(
	fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
	squarelength= 50,
	pieceSet=loadPiecesFolder("./pieces_png"),
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

    screen.blit(img,(0,0))
    pygame.display.update()
    clock.tick(10)
    print(clock.get_fps())
pygame.quit()