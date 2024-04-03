from stockfish import Stockfish
import os
import chess,chess.pgn
from copy import deepcopy,copy

os.system("cls")



stockfish = Stockfish(path="stockfish/stockfish-windows-x86-64-sse41-popcnt", depth=18, parameters={"Threads": 1, "Minimum Thinking Time": 30})

#Set board using moves from starting position
stockfish.set_position()
stockfish.make_moves_from_current_position(["e2e4"])
stockfish.make_moves_from_current_position(["e7e5"])
stockfish.make_moves_from_current_position(["b1c3"])
stockfish.make_moves_from_current_position(["d8g5"])
stockfish.make_moves_from_current_position(["d2d4"])
stockfish.make_moves_from_current_position(["d7d5"])

# game = chess.pgn.Game()
# node = game.add_variation(chess.Move.from_uci("e2e4"))
# node = node.add_line([chess.Move.from_uci("e7e5")])
# node = node.add_line([chess.Move.from_uci("b1c3")])
# node = node.add_line([chess.Move.from_uci("d8g5")])
# node = node.add_line([chess.Move.from_uci("d2d4")])

# print(game[0][0])


topmoves = stockfish.get_top_moves(3)
m1 = topmoves[0]["Move"]
m2 = topmoves[1]["Move"]
m3 = topmoves[2]["Move"]
print(m1,m2,m3)
# print(stockfish.get_fen_position())


