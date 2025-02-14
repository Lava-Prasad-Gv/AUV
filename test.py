from ultralytics import YOLO
import cv2


model = YOLO('best.pt')
img =cv2.imread('testimg.jpeg')
print("No of class:",model.names)
results = model(img,conf = 0.7)
print('results acquired:')
for result in results:
    print('processing single result:')
    boxes = result.boxes
    print(len(boxes))
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy.tolist()[0]
        c = box.cls
        print('class:',c)
