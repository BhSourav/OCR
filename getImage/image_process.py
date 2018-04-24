#import necessary packages
from PIL import Image
import pytesseract
import cv2
import os
path = "/home/darth_sourav/Work/python/untitled/test_images/"
arg = "threshold"

#load the input image and convert to grayscale
image = cv2.imread(path+'example_03.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#check which preprocessing to apply
if arg == "threshold":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
elif arg == "blur":
    gray = cv2.medianBlur(image, 3)

#write grayscale image to disk for ocr to work
filename = path + '{}.png'.format(os.getpid())
cv2.imwrite(filename, gray)

#load the image as a PIL image, apply OCR and then delete the temporary image file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)


#show the images
cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.waitKey(0)