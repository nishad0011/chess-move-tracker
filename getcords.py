import cv2,sys,os
from ast import literal_eval
from YOLOv8py import run_yolo
from ultralytics import YOLO

os.system("cls")

#Global variables
print("loading model")
model = YOLO('./YOLOv8/runs/detect/train/weights/best.pt')
print("model loaded")

radius = 1
color = (255, 0, 0) 
thickness = 2

edge_coords=[]
square_coords = {}
movelist0 = []
movelist1 = []
				
def lerp(min, max, x) :
    return min + ((max - min) * x)

def lerp2(mn , mx, x):
    l = (mx-mn)*x
    le = 2*min(l ,mx-(l+mn))
    return int(mn+le)

path1 = r'Z:\Program Code\Python\Chess\move0.jpg'
img = cv2.imread(path1, 1)

path2 = r'Z:\Program Code\Python\Chess\move1.jpg'
img2 = cv2.imread(path2, 1)

img = cv2.resize(img, (600, 600), interpolation = cv2.INTER_LINEAR)
img2 = cv2.resize(img2, (600, 600), interpolation = cv2.INTER_LINEAR)

def Capture_Event(event, x, y, flags, params):
	# If the left mouse button is pressed

	if event == cv2.EVENT_LBUTTONDOWN:
		string = (x,y)
		edge_coords.append(string)
		print("coords = "+str(x)+" "+str(y))

def set_squares():
	global edge_coords,square_coords,color,radius,thickness,img

	# Show the Image
	cv2.imshow('img',img)

	# Set the Mouse Callback function, and call
	# the Capture_Event function.
	cv2.setMouseCallback('img', Capture_Event)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


	topl = edge_coords[0]
	topr = edge_coords[1]
	bottr = edge_coords[2]
	bottl = edge_coords[3]


	# Finding A-file coordinates
	for i in range(0,8):
		x = lerp(topl[0], topr[0] , i/7)
		y = lerp(topl[1], topr[1] , i/7)
		co = (int(x) , int(y))

		square_coords["a{x}".format(x=i+1)] = co
		img = cv2.circle(img, co, radius, color, thickness)

	# Finding h-file coordinates
	for i in range(0,8):
		x = lerp(bottl[0], bottr[0] , i/7)
		y = lerp(bottl[1], bottr[1] , i/7)
		co = (int(x) , int(y))

		square_coords["h{x}".format(x=i+1)] = co

		img = cv2.circle(img, co, radius, color, thickness)

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

			img = cv2.circle(img, co, radius, color, thickness)

	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

set_squares()

color = (0, 255, 0)
radius = 5
font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 0.5
			

print("Running model on image")
yolo_dict = run_yolo(model,img)
print("model done")

file1 = open("yolodictionary.txt", "w")
L = str(yolo_dict)
file1.writelines(L)
file1.close()

for i in yolo_dict.items():
	x = round(i[1][1][0] - 0.5*i[1][1][2])
	y = round(i[1][1][1] - 0.5*i[1][1][3])
	wid = round(i[1][1][2])
	hei = round(i[1][1][3])

	center_of_piece = (round(x+wid*0.5),round(y+hei*0.8))

	#Lables
	# img  = cv2.putText(img, i[0], co, font, fontScale, color, thickness, cv2.LINE_AA) 

	#Bounding box 
	img = cv2.rectangle(img, (x,y), (x+wid,y+hei), color, thickness)

	#circles
	img = cv2.circle(img,center_of_piece,radius,color,thickness)

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
	movelist0.append((i[1][0],sq))
	img = cv2.line(img, center_of_piece, square_coords[sq], (0,0,255), thickness) 

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("Running model on image")
yolo_dict2 = run_yolo(model,img2)
print("model done")
file1 = open("yolodictionary2.txt", "w")
L = str(yolo_dict2)
file1.writelines(L)
file1.close()

for i in yolo_dict2.items():
	x = round(i[1][1][0] - 0.5*i[1][1][2])
	y = round(i[1][1][1] - 0.5*i[1][1][3])
	wid = round(i[1][1][2])
	hei = round(i[1][1][3])

	center_of_piece = (round(x+wid*0.5),round(y+hei*0.8))

	#Lables
	# img  = cv2.putText(img, i[0], co, font, fontScale, color, thickness, cv2.LINE_AA) 

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
	movelist1.append((i[1][0],sq))
	img2 = cv2.line(img2, center_of_piece, square_coords[sq], (0,0,255), thickness) 

print(movelist0)
print(movelist1)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

