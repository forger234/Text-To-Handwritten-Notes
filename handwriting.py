import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
text = open("handwriting.txt","r")
text=text.read()
filename=input("Enter your file name to create: ").strip()
img_height = 1000
img_width = 800
image = np.ones((img_height, img_width, 3), dtype=np.uint8) * 255#dtype=np.uint8: Specifies the data type as unsigned 8-bit integers, which is standard for images (range 0–255).
font_path = "handwriting.ttf" 
font_size = 32

font = ImageFont.truetype(font_path, font_size)
img_pil = Image.fromarray(image)
draw = ImageDraw.Draw(img_pil)
x, y = 50, 50
line_spacing = 10 
for line in text.split("\n"):
    draw.text((x, y), line, font=font, fill=(0, 0, 138))
    y += font_size + line_spacing
final_image = np.array(img_pil)
cv2.imwrite(filename+".png", final_image)
print("END")
