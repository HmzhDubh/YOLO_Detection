from roboflow import Roboflow
import supervision as sv
import cv2
from ultralytics import YOLO

rf = Roboflow(api_key="aEZAKqe87WUQ22o8TaW8")
project = rf.workspace().project("food-waste-detection-abkdx")
model = project.version(1).model


result = model.predict("image2.jpg", confidence=40, overlap=30).json()

labels = [item["class"] for item in result["predictions"]]

detections = sv.Detections.from_roboflow(result)

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

image = cv2.imread("image2.jpg")

annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)

sv.plot_image(image=annotated_image, size=(16, 16))