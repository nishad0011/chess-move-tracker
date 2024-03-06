import cv2
from YOLOv8py import run_yolo
from ultralytics import YOLO


model = YOLO('./YOLOv8/runs/detect/train/weights/best.pt')

def Capture_Event(event, x, y, flags, params):
	# If the left mouse button is pressed
	global count,coords #Uses the global variables in function

	if event == cv2.EVENT_LBUTTONDOWN:
		string = (x,y)
		coords.append(string)
		print("coords = "+str(x)+" "+str(y))
				
def lerp(min, max, x) :
    return min + ((max - min) * x)

def lerp2(mn , mx, x):
    l = (mx-mn)*x
    le = 2*min(l ,mx-(l+mn))
    return int(mn+le)

coords=[]
count = 0

path = r'Z:\Program Code\Python\Chess\move0.jpg'
img = cv2.imread(path, 1)
img = cv2.resize(img, (600, 600), interpolation = cv2.INTER_LINEAR)

# Show the Image
cv2.imshow('img',img)

# Set the Mouse Callback function, and call
# the Capture_Event function.
cv2.setMouseCallback('img', Capture_Event)

cv2.waitKey(0)
cv2.destroyAllWindows()

radius = 1
color = (255, 0, 0) 
thickness = 2

topl = coords[0]
topr = coords[1]
bottr = coords[2]
bottl = coords[3]

MyDictionary1 = {}

# Finding A-file coordinates
for i in range(0,8):
	x = lerp(topl[0], topr[0] , i/7)
	y = lerp(topl[1], topr[1] , i/7)
	co = (int(x) , int(y))

	MyDictionary1["a{x}".format(x=i+1)] = co


	img = cv2.circle(img, co, radius, color, thickness)

# Finding h-file coordinates
for i in range(0,8):
	x = lerp(bottl[0], bottr[0] , i/7)
	y = lerp(bottl[1], bottr[1] , i/7)
	co = (int(x) , int(y))

	MyDictionary1["h{x}".format(x=i+1)] = co

	img = cv2.circle(img, co, radius, color, thickness)

# Finding coordinates of remaining squares
for i in range(1,9):

	#Getting top and bottom coord of the file
	top = (MyDictionary1[f'a{i}'][0] , MyDictionary1[f'a{i}'][1])
	bottom = (MyDictionary1[f'h{i}'][0] , MyDictionary1[f'h{i}'][1])
	
	#Getting coords of the square in between top and bottom
	letters =('b','c','d','e','f','g')
	for j in letters:
		x = lerp(top[0], bottom[0] , (letters.index(j)+1)/7)
		y = lerp(top[1], bottom[1] , (letters.index(j)+1)/7) - (lerp2(12, 40 , (letters.index(j))/5))#correction function

		co = (int(x) , int(y))
		MyDictionary1[f"{j}{i}"] = co

		img = cv2.circle(img, co, radius, color, thickness)

# print(MyDictionary1)
cv2.imshow('img',img)
cv2.waitKey(0)
# Destroy all the windows
cv2.destroyAllWindows()

yolo_dict = run_yolo(model,img)
print("model done")

color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 0.5


""" + (0.5 * i[1][2])
+ (0.9 * i[1][3])) """
for i in yolo_dict.values():
	co =( round(i[1][0] ) ,
	      round(i[1][1]  ))
	img  = cv2.putText(img, i[0], co, font, fontScale, color, thickness, cv2.LINE_AA) 

cv2.imshow('img',img)
cv2.waitKey(0)