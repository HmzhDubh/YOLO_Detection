from ultralytics import YOLO

model = YOLO("last.pt")

results = model.train(data="data.yaml", epochs=10)
