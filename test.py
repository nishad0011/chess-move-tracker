import os
import chess,chess.pgn
from copy import deepcopy,copy

os.system("cls")

""" game = chess.pgn.Game()
node = game.add_variation(chess.Move.from_uci("e2e4"))
node = node.add_line([chess.Move.from_uci("e7e5")])
node = node.add_line([chess.Move.from_uci("b1c3")])
node = node.add_line([chess.Move.from_uci("h7h5")])

print(game.mainline_moves()) """
# a=1
# a=1.1
# print(a)

ll1 = [('black-bishop', 'b3'), 
       ('white-knight', 'b1'), 
       ('white-bishop', 'b3'), 
       ('white-bishop', 'a5'), 
       ('white-pawn', 'f3'), 
       ('white-king', 'e1'), 
       ('black-rook', 'b7'), 
       ('black-pawn', 'f7'), 
       ('white-queen', 'b4'), 
       ('black-king', 'd8'), 
       ('black-pawn', 'd5'), 
       ('black-knight', 'h6'), 
       ('black-bishop', 'f5')]

ll2 = [('white-knight', 'b1'), 
       ('black-bishop', 'a2'), 
       ('black-rook', 'b7'), 
       ('white-queen', 'b4'), 
       ('white-king', 'e1'), 
       ('black-king', 'd8'), 
       ('black-pawn', 'f7'), 
       ('white-pawn', 'f3'), 
       ('white-bishop', 'a5'), 
       ('black-pawn', 'd5'), 
       ('black-knight', 'h6'), 
       ('black-bishop', 'f5')]

def get_move(l1: list,l2:list):
    temp1 = deepcopy(l1)
    temp2 = deepcopy(l2)
    for i in l1:
        for j in l2:
            if i[0] == j[0] and i[1] == j[1]:
                temp1.remove(j)
                temp2.remove(i)
    
    for i in temp1:
        if temp2[0][0] == i[0]:
            print(str(temp1[0][1])+str(i[1]))


get_move(ll1,ll2)