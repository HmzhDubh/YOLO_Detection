import re
from ultralytics import YOLO

# Load a model
model = YOLO("last.pt")  # pretrained YOLOv8n model
model.predict()
# Run batched inference on a list of images
results = model(["dataset/image6.jpg"])  # return a list of Results objects
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk

classes = boxes.cls
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
# for i in range(len(clases)):
#     if clases[i] == 0.:
#         print("LeftOvers")
#         xywhn = boxes.xywhn[i]
#         print("The BOXES: ", xywhn)
#         for xywhn[i] in xywhn:
#             width = xywhn[i][2]
#             height = xywhn[i][3]
#         leftoversBoxSize = int(width * height)
#     elif clases[i] == 1.:
#         print("Plate")
#         xywhn = boxes.xywhn[i]
#         print("The BOXES: ", xywhn)
#         for xywhn[i] in xywhn:
#             width = xywhn[i][2]
#             height = xywhn[i][3]
#         plateBoxSize = int(width * height)
#
# print("Percentage: ")
# print((leftoversBoxSize / plateBoxSize) * 100)

#
# for xywh in xywh:
#         print("Width: ",xywh[2])
#         print("Height: ", xywh[3])