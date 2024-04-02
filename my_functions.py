import cv2,pygame,os
from stockfish import Stockfish
from fentoboardimage import fenToImage, loadPiecesFolder

def lerp(min, max, x) :
    return min + ((max - min) * x)

def lerp2(mn , mx, x):
    l = (mx-mn)*x
    le = 2*min(l ,mx-(l+mn))
    return int(mn+le)

edge_coords =[]
def Capture_Event(event, x, y, flags, params):
	# If the left mouse button is pressed
	global edge_coords
	if event == cv2.EVENT_LBUTTONDOWN:
		string = (x,y)
		edge_coords.append(string)

def get_edge_coords(img):
	global edge_coords
	edge_coords =[]
	# Show the Image
	cv2.imshow('Set edge Coords',img)
	cv2.setMouseCallback('Set edge Coords',Capture_Event)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return edge_coords

def update_edge_coords(cords : list):
	with open("cords.txt", "r+") as f:
		#Get coords and save to cords.txt
		f.truncate(0)
		f.write(str(cords))
		print("File write complete")

def get_remaining_coords(edge_coords,img):
	topl = edge_coords[0]
	topr = edge_coords[1]
	bottr = edge_coords[2]
	bottl = edge_coords[3]
	square_coords = {}

	radius = 1
	color = (255, 0, 0) 
	thickness = 2

	# Finding A-file coordinates
	for i in range(0,8):
		x = lerp(topl[0], topr[0] , i/7)
		y = lerp(topl[1], topr[1] , i/7)
		co = (int(x) , int(y))

		square_coords["a{x}".format(x=i+1)] = co
		# img = cv2.circle(img, co, radius, color, thickness)

	# Finding h-file coordinates
	for i in range(0,8):
		x = lerp(bottl[0], bottr[0] , i/7)
		y = lerp(bottl[1], bottr[1] , i/7)
		co = (int(x) , int(y))

		square_coords["h{x}".format(x=i+1)] = co

		# img = cv2.circle(img, co, radius, color, thickness)

	# Finding coordinates of remaining squares
	for i in range(1,9):
		#Getting top and bottom coord of the file
		top = (square_coords[f'a{i}'][0] , square_coords[f'a{i}'][1])
		bottom = (square_coords[f'h{i}'][0] , square_coords[f'h{i}'][1])
		
		#Getting coords of the square in between top and bottom
		letters =('b','c','d','e','f','g')
		for j in letters:
			x = lerp(top[0], bottom[0] , (letters.index(j)+1)/7)
			y = lerp(top[1], bottom[1] , (letters.index(j)+1)/7) - (lerp2(12, 40 , (letters.index(j))/5))#correction function

			co = (int(x) , int(y))
			square_coords[f"{j}{i}"] = co

			# img = cv2.circle(img, co, radius, color, thickness)

	# cv2.imshow('img',img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	return square_coords

def sf():
	stockfish = Stockfish(path="stockfish/stockfish-windows-x86-64-sse41-popcnt", depth=16, parameters={"Threads": 1, "Minimum Thinking Time": 30,"UCI_Elo": 3000})
	stockfish.set_position()

	return stockfish

def get_board_img(current_fen) -> str:
	image = fenToImage(
	fen=current_fen,
	squarelength= 70,
	pieceSet=loadPiecesFolder("./pieces_png",cache=True),
	darkColor="#2e323e",
	lightColor="#6b7280"
	)
	img = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
	return img

def show_square_mapping(square_coords:dict , img):
	clear_img = img.copy()
	for x,y in square_coords.values():
		img = cv2.circle(clear_img, (x,y), 2, (0, 255, 0 ) , 3)
	cv2.imshow('Square Mapping',clear_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def get_current_eval_string(eval:dict):
	if(eval['type'] == 'cp'):
		return str("Evaluation: 0."+str( eval.get('value') ) )
	else: # eval['type'] == 'value'
		return str("Evaluation: #"+str(eval.get('value') ) )


