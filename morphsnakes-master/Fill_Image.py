import cv2
import numpy as np

directory = 'dataset_mask/'
new_directory = 'C:/Users/DELL/Downloads/morphsnakes-master/images'
PATH_IMG_NODULE = 'images/C_0001_1.RIGHT_CC_Mask.jpg'

#for image in os.listdir(directory):
# Read image as grayscale
img = cv2.imread(PATH_IMG_NODULE, cv2.IMREAD_GRAYSCALE)
hh, ww = img.shape[:2]

# threshold
thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]

# get the (largest) contour
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

# draw white filled contour on black background
result = np.zeros_like(img)
cv2.drawContours(result, [big_contour], 0, (255,255,255), cv2.FILLED)

# save results
cv2.imwrite(new_directory + '/C_0001_1.RIGHT_CC_Mask_Full.jpg', result)