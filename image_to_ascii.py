from PIL import Image, ImageDraw, ImageFont
import numpy as np

img = Image.open('images.jfif')

# 0-255 grayscale values
ASCII_CHARS = "@%#*+=:. " #(convert 0-255 grayscale values to 9 values)

# function to convert pixel to grayscale values
def pixel_to_grayscale(pixel):
    value = np.dot(pixel, [0.2989, 0.5870, 0.1140])
    return value

# function to convert grayscale to ascii art
def grayscale_to_ascii(val):
    if val<(256/9)*1:
        return ASCII_CHARS[0]
    if val>=(256/9)*1 and val<(256/9)*2:
        return ASCII_CHARS[1]
    if val>=(256/9)*2 and val<(256/9)*3:
        return ASCII_CHARS[2]
    if val>=(256/9)*3 and val<(256/9)*4:
        return ASCII_CHARS[3]
    if val>=(256/9)*4 and val<(256/9)*5:
        return ASCII_CHARS[4]
    if val>=(256/9)*5 and val<(256/9)*6:
        return ASCII_CHARS[5]
    if val>=(256/9)*6 and val<(256/9)*7:
        return ASCII_CHARS[6]
    if val>=(256/9)*7 and val<(256/9)*8:
        return ASCII_CHARS[7]
    if val>=(256/9)*8 and val<(256/9)*8:
        return ASCII_CHARS[8]

# Get all of the values of individual pixel from image to array(2-dimensional) using numpy 
pixel_1 = np.array(img)
height, width = pixel_1.shape[:2]

# Initialized a 2d-array that stores the ascii values of each pixel of the image
matrix = [[0]*width]*height

str = ""

# Looping statement for storing values of ascii
for i in range(height):
    for j in range(width):
        val = pixel_1[i][j]
        matrix[i][j] = grayscale_to_ascii(pixel_to_grayscale(val))
        # print(matrix[i][j], end="")
        str += f"{matrix[i][j]}"
    str += "\n"

# Create an image
char_width, char_height = 8,16
img_width = char_width * 300
img_height = char_height * 168
img = Image.new("RGB", (img_width, img_height), color="white")

# Draw text
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

# Draw ASCII text on the image
draw.text((0,0), str, fill="black", font= font)

# Save as an image
img.save("ascii_output.png")
img.show()