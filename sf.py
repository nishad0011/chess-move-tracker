from stockfish import Stockfish


stockfish = Stockfish(path="stockfish/stockfish-windows-x86-64-sse41-popcnt", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})

#Set board using moves from starting position
stockfish.set_position(["e2e3", "e7e5"])
stockfish.make_moves_from_current_position(["f2f4"])
stockfish.make_moves_from_current_position(["e5f4"])
stockfish.make_moves_from_current_position(["g2g4"])
stockfish.make_moves_from_current_position(["f4g3"])
stockfish.make_moves_from_current_position(["g1e2"])

print(stockfish.get_fen_position())
print(stockfish.get_board_visual())

