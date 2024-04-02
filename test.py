import os
import chess,chess.pgn

os.system("cls")

game = chess.pgn.Game()
node = game.add_variation(chess.Move.from_uci("e2e4"))
node = node.add_line([chess.Move.from_uci("e7e5")])
node = node.add_line([chess.Move.from_uci("b1c3")])
node = node.add_line([chess.Move.from_uci("h7h5")])

print(game.mainline_moves())