import sys,ast

""" def lerp(mn , mx, x):
    l = (mx-mn)*x
    le = 2*min(l ,mx-(l+mn))

    return int(mn+le)
for i in range(6):
    print(f"larp = {lerp(10,10,(i+1)/6)}") 

d1 ={0: ['black-bishop', (145.229, 64.5175, 25.3485, 62.5342)],
    1: ['black-rook', (274.3456, 68.7882, 26.8786, 54.0489)], 
    2: ['white-knight', (79.9763, 62.6289, 30.0702, 64.4431)], 
    3: ['white-bishop', (61.244, 267.4126, 32.8189, 65.6556)], 
    4: ['white-queen', (182.0623, 62.1887, 28.9344, 73.6199)], 
    5: ['white-king', (72.1473, 165.2027, 37.7857, 89.6613)], 
    6: ['black-king', (318.9753, 126.7951, 36.6845, 85.6313)],
    7: ['black-pawn', (290.7133, 225.849, 24.4498, 50.0181)], 
    8: ['white-bishop', (208.8752, 30.2432, 24.4234, 58.1365)], 
    9: ['black-pawn', (215.2393, 145.3759, 22.3766, 48.1175)], 
    10: ['black-knight', (268.2615, 319.436, 31.8515, 69.6694)], 
    11: ['white-pawn', (142.3823, 226.5931, 27.2477, 52.8395)], 
    12: ['black-bishop', (222.3599, 224.1397, 28.1539, 62.5126)], 
    13: ['white-rook', (210.6001, 399.0271, 40.2375, 33.9459)]}

for i in d1.items():
    print(i[1][1][1])

 #print(sys.maxsize)
# print(abs(1.23))

s = "[(118, 73), (443, 78), (498, 485)]"

edge_coords=ast.literal_eval(s)
print(edge_coords[1])
for i in list(s):
    print(i) """


""" edgecords_size_file = os.path.getsize('textfiles/edgecoords.txt')
if (edgecords_size_file == 0):
	print("Edge coords not found")
	set_squares()
	print("coords found")

	ec = open('textfiles/edgecoords.txt', "w")
	L = str(edge_coords)
	ec.writelines(L)
	ec.close()
else:
	print("Skipped finding ec")
	ec = open('textfiles/edgecoords.txt', "r")
	edge_coords = literal_eval(ec.read()) """

movelist0 = [('white-knight', 'b1'), 
            ('white-bishop', 'g1'), 
            ('black-bishop', 'b3'), 
            ('black-rook', 'b7'), 
            ('white-king', 'e1'), 
            ('white-bishop', 'a5'), 
            ('white-pawn', 'f3'), 
            ('white-queen', 'b4'), 
            ('black-pawn', 'f7'), 
            ('black-king', 'd8'), 
            ('black-knight', 'h6'), 
            ('black-pawn', 'd5'), 
            ('black-bishop', 'f5'),
              ('jlkdsjf')]

movelist1 =  [('white-knight', 'b1'), 
              ('white-bishop', 'g1'), 
              ('black-bishop', 'b3'), 
              ('black-rook', 'b7'), 
              ('white-king', 'e1'), 
              ('white-bishop', 'a5'), 
              ('white-pawn', 'f3'), 
              ('white-queen', 'b4'), 
              ('black-pawn', 'f7'), 
              ('black-king', 'd8'), 
              ('black-knight', 'h6'), 
              ('black-pawn', 'd5'), 
              ('black-bishop', 'h7')]


def get_move(movelist0,movelist1):
    l1 = movelist0.copy()
    l2 = movelist1.copy()

    for i in movelist0:
        if i in movelist1:
            l1.remove(i)
            l2.remove(i)

    for i in l2:
        for j in l1:
            if i[0] == j[0]:
                move = f'{j[1]}{i[1]}'
                return move
    return None

#print(get_move(movelist0,movelist1))

print(movelist0[0])