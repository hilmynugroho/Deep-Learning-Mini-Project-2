from ultralytics import YOLO

model = YOLO("runs/detect/train5/weights/best.pt")
results = model("C:/Users/ideapad/Downloads/train_video.mp4", save=True)
