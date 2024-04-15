import requests
from bs4 import BeautifulSoup
import cv2,base64


url = 'http://192.168.29.249:5000/data'

r = requests.get(url)
soup = BeautifulSoup(r.text,features="html.parser")

para = soup.find_all('p')
for p in para:
    data = str(p.contents[0])
    data_strip = data[2:-1]

b = data_strip.encode('utf-8')

name = '4'
with open(f'Z:\Program Code\Python\Chess\YOLOv8\custom_data\images\{name}.jpg','wb') as f:
    f.write(base64.b64decode((b))) 
    print("decode complete")

img = cv2.imread(f'Z:\Program Code\Python\Chess\YOLOv8\custom_data\images\{name}.jpg')
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(f'Z:\Program Code\Python\Chess\YOLOv8\custom_data\images\{name}.jpg', rotated_img)