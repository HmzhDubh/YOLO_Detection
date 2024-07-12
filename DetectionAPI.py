import os
from PIL import Image
from roboflow import Roboflow
rf = Roboflow(api_key="add your api key")
project = rf.workspace().project("name your project ")
model = project.version(7).model

# infer on a local image
imgpath = "dataset/image4.jpg"
# visualize your prediction
counter = 1
resultsSavePath = "dataset/API-Detection-results/rImage"+ str(counter)+".jpg"
print(resultsSavePath)

while (os.path.exists(resultsSavePath)):
    counter+=1
    resultsSavePath = "dataset/API-Detection-results/rImage"+ str(counter)+".jpg"
print("new file name is : ",resultsSavePath)
model.predict(imgpath, confidence=40, overlap=30).save(resultsSavePath)
