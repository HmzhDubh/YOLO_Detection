from ultralytics import YOLO
# Using the official Ultralytics YOLO Model to train a new model
# According to annotations and labeling in roboflow website
model = YOLO("best.pt")

results = model.train(data="data.yaml", epochs=25)
