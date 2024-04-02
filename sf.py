from stockfish import Stockfish


stockfish = Stockfish(path="stockfish/stockfish-windows-x86-64-sse41-popcnt", depth=18, parameters={"Threads": 1, "Minimum Thinking Time": 30})

#Set board using moves from starting position
stockfish.set_position()

print(stockfish.get_fen_position())
print(stockfish.get_board_visual())

