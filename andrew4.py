import os
import random

# Paths to your image and mask folders
image_folder = 'path/to/your/images'
mask_folder = 'path/to/your/masks'

# List all image files in the images folder
images_list = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Create a list of corresponding mask filenames based on image filenames
masks_list = [f for f in os.listdir(mask_folder) if os.path.isfile(os.path.join(mask_folder, f))]

# Choose a random index to pick one image and its corresponding mask
random_index = random.randint(0, len(images_list) - 1)

# Get the random image and mask based on the selected index
random_image = images_list[random_index]
random_mask = masks_list[random_index]

# Print the selected image and mask
print(f"Random Image: {random_image}")
print(f"Random Mask: {random_mask}")
