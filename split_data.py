import os
import random
import shutil

# Input and output directories
raw_dir = 'raw-labeled/im_raw'
label_dir = 'raw-labeled/im_labeled'
output_img = 'dataset/images'
output_lbl = 'dataset/labels'

# Create destination folders
for split in ['train', 'val']:
    os.makedirs(os.path.join(output_img, split), exist_ok=True)
    os.makedirs(os.path.join(output_lbl, split), exist_ok=True)

# Get and shuffle image list
image_files = [f for f in os.listdir(raw_dir) if f.endswith(('.jpg', '.png'))]
random.shuffle(image_files)

# 80-20 train-val split
split_idx = int(len(image_files) * 0.8)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Function to copy files and generate empty label if needed
def copy_files(split, files):
    for file in files:
        name, ext = os.path.splitext(file)
        img_src = os.path.join(raw_dir, file)
        label_src = os.path.join(label_dir, name + '.txt')

        img_dst = os.path.join(output_img, split, file)
        label_dst = os.path.join(output_lbl, split, name + '.txt')

        # Copy image
        shutil.copy(img_src, img_dst)

        # Copy label if exists, otherwise create empty label file
        if os.path.exists(label_src):
            shutil.copy(label_src, label_dst)
        else:
            open(label_dst, 'w').close()  # Create empty file
            print(f"Created empty label for: {file}")

# Run for both splits
copy_files('train', train_files)
copy_files('val', val_files)

print("Dataset split, copied, and labeled successfully.")
