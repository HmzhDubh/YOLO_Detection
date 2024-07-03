# YOLO
## This project aim to Train, Detect, and Use live camera to detect classes in the trained model.

# ***Requirements***
- Python
- YOLO from Ultralytics
- opencv - python (4.6.0.66) recommended
- roboflow or other annotation tool

> [!note]
> You can install pretrained YOLO models config and weights files from [YOLO Site](https://pjreddie.com/darknet/yolo/).
> Or train a model by your self see [Roboflow Custom dataset Training](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/).
> Edit the data.yaml File as suitable for your project 

##  Train
* install ultralytics `pip install ultralytics`
And import it in your project
* specify Your model either pretrained or a new one `yolov8n.py`
* call train to the model and specify data and number of epochs `data="data.yaml, epochs=10`

## Detect Images
To use your model to detect and predict new images do the following
* Import YOLO
* Specify the model
* Specify the location of the images to be detected

`note:` the `picDetect.py` script returns a percentage and the result of the detection in the image  
## Live Camera
* install cv2 `pip intall opencv-python`
* Prepare the model used to detect live photos
* prepare the Camera that is used for detection