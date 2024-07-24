import os
from PIL import Image
from roboflow import Roboflow

from picDetect import detection

# This function uses API of the roboflow project where we annotate and deployed the model
# The function takes a path to the image which is being processed to be predicted
# It also uses the detection() method to return the percentage of the waste prediction.

rf = Roboflow(api_key="aEZAKqe87WUQ22o8TaW8")
project = rf.workspace().project("plate-waste-detection")
model = project.version(7).model

# infer on a local image
imgpath = "dataset/detection-images/image4.jpg"
# visualize your prediction
def DetectImgByAPI(img):
    counter = 1
    resultsSavePath = "dataset/API-Detection-results/rImage"+ str(counter)+".jpg"
    print(resultsSavePath)

    while (os.path.exists(resultsSavePath)):
        counter+=1
        resultsSavePath = "dataset/API-Detection-results/rImage"+ str(counter)+".jpg"
    print("new file name is : ",resultsSavePath)
    model.predict(imgpath, confidence=40, overlap=30).save(resultsSavePath)

    percResult = detection(imgpath)
    print(">>> The Waste in this plate is: " + format(percResult, ".2f") + "%")
    return percResult
print(DetectImgByAPI(imgpath))
