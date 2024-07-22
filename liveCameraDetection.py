import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
print(model.names)

cam = cv2.VideoCapture(0)

while True:

    success, frame = cam.read()
    results = model.track(frame, classes=0, conf=0.8, imgsz=480)
    cv2.putText(frame, f"Total: {len(results[0].boxes)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Live Camera", results[0].plot())
    key = cv2.waitKey(1)

    if key == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break

