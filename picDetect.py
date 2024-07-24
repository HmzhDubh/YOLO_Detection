import re
from ultralytics import YOLO
model = YOLO("best.pt")

# model.predict(img_path)

# Using our trained model to predict images by passing it through detection() function
# the img variable represents the path to the image

img = ""
def detection(img):
    image = img
    # print("\n___________ Detection _____________")
    # print(image)
    # if image.startswith("dataset/detection-images/"):
    #     print("image path is correctly formed")
    # else:
    #
    #     image = "dataset/detection-images/" + image
    #
    # print("image = ", image)
    results = model([image])

    for result in results:
        boxes = result.boxes
        masks = result.masks
        key_points = result.keypoints
        probs = result.probs
        obb = result.obb
        result.show()
        #result.save(filename="result.jpg")

    classes = boxes.cls

    sumLeftoversBoxes = 0

    for i in range(len(classes)):

        if str(classes[i]) == "tensor(1.)":
            #print("plate")
            width = boxes.xywh[i][2]
            height = boxes.xywh[i][3]

            plateBoxSize = width * height
            plateBoxSize = int(re.search(r'\d+', str(plateBoxSize)).group())

        elif str(classes[i]) == "tensor(0.)":
            #print("LeftOvers")
            width = boxes.xywh[i][2]
            height = boxes.xywh[i][3]
            leftoversBoxSize = width * height
            leftoversBoxSize = int(re.search(r'\d+', str(leftoversBoxSize)).group())

            sumLeftoversBoxes += leftoversBoxSize

    perc = (sumLeftoversBoxes / plateBoxSize) * 100
    # perc = perc - 20 # buffer value    print(int(perc), "% of The Food is Wasted")

    return perc

#percentage = detection(img)
#print("{0}%".format(format(percentage, ".2f")))
