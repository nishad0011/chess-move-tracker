def split(s):
    st = str(s)
    return float(st[7:-1])

def run_yolo(model,img):
    results =model.predict(img)

    piecebox={}
    for result in results:

        detection_count = result.boxes.shape[0]

        for i in range(detection_count):
            cls = int(result.boxes.cls[i].item())
            name = result.names[cls]
            bx = (split(result.boxes.xywh[i][0]),
                  split(result.boxes.xywh[i][1]),
                  split(result.boxes.xywh[i][2]),
                  split(result.boxes.xywh[i][3]))
            piecebox[i]= [name,bx]
    
    return piecebox