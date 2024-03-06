import chess
import chess.svg

board = chess.Board()

img  = chess.svg.board(board)
print(img)