import cv2 as cv
import os

video_path = "C:/Users/ideapad/Downloads/train_video720.mp4"
output_dir = 'dataset/images/raw'
os.makedirs(output_dir, exist_ok=True)

cap = cv.VideoCapture(video_path)
frame_rate = 20  

fps = int(cap.get(cv.CAP_PROP_FPS))
interval = fps * frame_rate
frame_count = 0
img_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % interval == 0:
        filename = os.path.join(output_dir, f'frame_{img_count:04d}.jpg')
        cv.imwrite(filename, frame)
        img_count += 1
    frame_count += 1

cap.release()
