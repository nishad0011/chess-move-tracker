import io
from os import system
import pygame
import chess
import chess.svg

# board.is_checkmate()
# board.is_stalemate()
# stockfish.is_move_correct('a2a3')

system('cls')

##Setup Pygame:
pygame.init()
 
width, height = 640, 640
screen = pygame.display.set_mode((width, height))

board1 = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
board1.push_san("e4")
boardsvg = io.BytesIO(chess.svg.board(board=board1 , size=1000).encode())
image = pygame.image.load(boardsvg)

image_cropped = pygame.transform.scale_by(image,1.5)

#Step 2: Blit the image
# image_cropped = pygame.transform.scale(image_cropped, (640, 640))


screen.blit(image_cropped,(0,0))
pygame.display.flip()
 
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()