import cv2
import os

#Get the directory
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'image.jpg')  # Use a relative path

if not os.path.exists(image_path):
    raise FileNotFoundError(f"The file {image_path} does not exist.")

image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Failed to load image {image_path}")

#Resize
scale_percent = 5  # Percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image', resized_image)
cv2.imshow('Gray image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()