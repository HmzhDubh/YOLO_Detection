import re
from ultralytics import YOLO
model = YOLO("last.pt")
model.predict("dataset/image1.jpg")


def detection():

    print("\n___________ Detection _____________")
    results = model(["dataset/image1.jpg"])

    for result in results:
        boxes = result.boxes
        masks = result.masks
        key_points = result.keypoints
        probs = result.probs
        obb = result.obb
        result.show()
        result.save(filename="result.jpg")

    classes = boxes.cls

    sumLeftoversBoxes = 0

    for i in range(len(classes)):

        if str(classes[i]) == "tensor(1.)":
            print("plate")
            width = boxes.xywh[i][2]
            height = boxes.xywh[i][3]

            plateBoxSize = width * height
            plateBoxSize = int(re.search(r'\d+', str(plateBoxSize)).group())

        elif str(classes[i]) == "tensor(0.)":
            print("LeftOvers")
            width = boxes.xywh[i][2]
            height = boxes.xywh[i][3]
            leftoversBoxSize = width * height
            leftoversBoxSize = int(re.search(r'\d+', str(leftoversBoxSize)).group())

            sumLeftoversBoxes += leftoversBoxSize

    perc = (sumLeftoversBoxes / plateBoxSize) * 100
    print(int(perc), "% of The Food is Wasted")

    return perc


percentage = detection()
print("{0}%".format(format(percentage, ".2f")))
