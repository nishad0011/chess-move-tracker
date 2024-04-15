import cv2,pygame,os
import sys
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
	stockfish = Stockfish(path="stockfish/stockfish-windows-x86-64-sse41-popcnt", depth=10, parameters={"Threads": 1, "Minimum Thinking Time": 30,"UCI_Elo": 3000})
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
		return str("Evaluation: "+str(int( eval.get('value') )/100) )
	elif(eval['type'] == 'mate') and (eval['value'] == 0):
		return "Checkmate"
	else: # eval['type'] == 'value'
		return str("Evaluation: #"+str(eval.get('value') ) )

def see_yolo_working(yolo_dict2:dict,img2,square_coords:dict):
	color = (0, 255, 0)
	radius = 5
	thickness = 2
	font = cv2.FONT_HERSHEY_SIMPLEX 
	fontScale = 0.5

	for i in yolo_dict2.items():
		x = round(i[1][1][0] - 0.5*i[1][1][2])
		y = round(i[1][1][1] - 0.5*i[1][1][3])
		wid = round(i[1][1][2])
		hei = round(i[1][1][3])
		label = i[1][0]
		center_of_piece = (round(x+wid*0.5),round(y+hei*0.8))

		#Lables
		img2  = cv2.putText(img2, label, (x,y-10), font, fontScale, color, 1, cv2.LINE_AA) 

		#Bounding box 
		img2 = cv2.rectangle(img2, (x,y), (x+wid,y+hei), color, thickness)

		#circles
		img2 = cv2.circle(img2,center_of_piece,radius,color,thickness)

		min = sys.maxsize
		sq = "Null"
		for j in square_coords.items():
			dist = abs( 
				((center_of_piece[0]-j[1][0])**2 + (center_of_piece[1]-j[1][1])**2)**0.5
			)
			if (dist<min):
				min = dist
				sq = j[0]
		
		# print(f"piece:{i[1][0]} is on {sq}, dist: {min}")
  
		img2 = cv2.line(img2, center_of_piece, square_coords[sq], (0,0,255), thickness) 

	cv2.imshow('img',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

