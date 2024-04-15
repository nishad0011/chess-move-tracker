import requests
from bs4 import BeautifulSoup
import cv2,base64

def get_cur_img():
    url = 'http://192.168.29.249:5000/data'

    r = requests.get(url)
    soup = BeautifulSoup(r.text,features="html.parser")

    para = soup.find_all('p')
    for p in para:
        data = str(p.contents[0])
        data_strip = data[2:-1]

    b = data_strip.encode('utf-8')
    # b = data.encode()
    # <byte_object>.decode("utf-8")

    # file = open('encode.bin', 'wb') 
    # file.write(b) 
    # file.close()
    # print("success")

    # file2 = open('encode.bin', 'rb') 
    # byte = file2.read() 
    # file.close() 

    with open('image001.jpeg','wb') as f:
        f.write(base64.b64decode((b))) 
        print("decode complete")

    # # nparr = np.frombuffer(b, np.uint8)
    # # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # # print("done")

    img = cv2.imread('image001.jpeg')
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    # cv2.imwrite('image001r.jpg', rotated_img)
    return rotated_img