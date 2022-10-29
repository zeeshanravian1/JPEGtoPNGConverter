"""
    This will convert the JPEG to PNG and then save the image with PNG.
"""
import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    filtered = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{filtered}.png', 'png')
