import cv2 as cv
import os
import re

video_path = "C:/Users/ideapad/Downloads/youtube_GFI5cIGe7tk_1920x1080_h264.mp4"
output_dir = 'raw-labeled/im_raw'
os.makedirs(output_dir, exist_ok=True)

# Find the highest frame number in the directory
def get_next_frame_number():
    highest_num = -1
    if os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            # Match filenames like frame_0123.jpg
            match = re.match(r'frame_(\d+)\.jpg', filename)
            if match:
                num = int(match.group(1))
                highest_num = max(highest_num, num)
    
    # Start from the next number, or 0 if no files exist
    return highest_num + 1 if highest_num >= 0 else 0

# Get the starting frame number
img_count = get_next_frame_number()
print(f"Starting extraction from frame_{img_count:04d}.jpg")

cap = cv.VideoCapture(video_path)
frame_rate = 10  # Extract a frame every 20 seconds
fps = int(cap.get(cv.CAP_PROP_FPS))
interval = fps * frame_rate
frame_count = 0
frames_saved = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count % interval == 0:
        # Create filename with the next sequential number
        filename = os.path.join(output_dir, f'frame_{img_count:04d}.jpg')
        
        # Save the frame
        cv.imwrite(filename, frame)
        img_count += 1
        frames_saved += 1
    
    frame_count += 1

cap.release()
print(f"Extracted {frames_saved} new frames")
print(f"Last frame saved: frame_{img_count-1:04d}.jpg")