# YOLO
## This project aim to Train, Detect, and Use live camera to detect classes in the trained model.

# ***Requirements***
- Python
- YOLO from Ultralytics
- Opencv - python (4.6.0.66) recommended
- Roboflow or other annotation tool

> [!note]
> You can install pretrained YOLO models config and weights files from [YOLO Site](https://pjreddie.com/darknet/yolo/).
> Or train a model by your self see [Roboflow Custom dataset Training](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/).
> Edit the data.yaml File as suitable for your project 

##  Train
* Install ultralytics `pip install ultralytics`
And import it in your project
* Specify Your model either pretrained or a new one `yolov8n.py`
* Call train to the model and specify data and number of epochs `data="data.yaml, epochs=10`

## Detect Images
To use your model to detect and predict new images do the following
* Import YOLO
* Specify the model
* Specify the location of the images to be detected

`note:` the `picDetect.py` script returns a percentage and the result of the detection in the image  
## Live Camera
* Install cv2 `pip intall opencv-python==4.6.0.66`
* Prepare the model used to detect live photos
* Prepare the Camera that is used for detection

## API Model
You are able to use external API to detect data see [robo flow API documentation](https://inference.roboflow.com/quickstart/explore_models/#run-a-private-fine-tuned-model)
* Define image path and model by its name 
* Run infer and detection 
* Display the image