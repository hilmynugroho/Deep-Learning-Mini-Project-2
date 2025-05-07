from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data='./data.yaml',
    epochs=100,
    imgsz=640,
    batch=16,
    exist_ok=True,
    lr0=0.001,
    optimizer='AdamW'
)