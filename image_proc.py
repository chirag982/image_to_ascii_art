from PIL import Image
import numpy as np

img = Image.open('images.jfif')
width, height = img.size

print(f"width : {width}")
print(f"Height : {height}")

# Get all of the values of individual pixel from image to array(2-dimensional) using numpy 
pixel_1 = np.array(img)
print(pixel_1[1][1])

