import re

import cv2
from ultralytics import YOLO

model = YOLO("last.pt")
results = model(source=0, show=True, conf=0.3, save=True)

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk

classes = results.boxes.cls
# print(classes)
leftoversBoxSize = 0
plateBoxSize = 0
sumLeftoversBoxes = 0

for i in range(len(classes)):

    if str(classes[i]) == "tensor(1.)":
        print("plate")
        width = boxes.xywh[i][2]
        height = boxes.xywh[i][3]
        # widthInt = int(re.search(r'\d+', str(width)).group())
        # heightInt = int(re.search(r'\d+', str(height)).group())

        plateBoxSize = width * height
        plateBoxSize = int(re.search(r'\d+', str(plateBoxSize)).group())
        # print(plateBoxSize)

    elif str(classes[i]) == "tensor(0.)":
        print("LeftOvers")
        width = boxes.xywh[i][2]
        height = boxes.xywh[i][3]
        leftoversBoxSize = width * height
        leftoversBoxSize = int(re.search(r'\d+', str(leftoversBoxSize)).group())
        # print(leftoversBoxSize)
        sumLeftoversBoxes += leftoversBoxSize

perc = (sumLeftoversBoxes / plateBoxSize) * 100
print(int(perc), "% of The Food is Wasted")
