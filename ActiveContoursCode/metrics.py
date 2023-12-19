import cv2
import os
import re
import numpy as np
from tensorflow.keras import backend as K

smooth = 100

def dice_coef(y_true, y_pred):
    y_truef = K.flatten(y_true)
    y_predf = K.flatten(y_pred)
    And = K.sum(y_truef * y_predf)
    return ((2 * And + smooth) / (K.sum(y_truef) + K.sum(y_predf) + smooth))

def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)

def iou(y_true, y_pred):
    intersection = K.sum(y_true * y_pred)
    sum_ = K.sum(y_true + y_pred)
    jac = (intersection + smooth) / (sum_ - intersection + smooth)
    return jac

def jac_distance(y_true, y_pred):
    y_truef = K.flatten(y_true)
    y_predf = K.flatten(y_pred)

    return - iou(y_truef, y_predf)

def adjust_data(mask):
    mask = mask / 255
    mask[mask > 0.5] = 1
    mask[mask <= 0.5] = 0
    return (mask)

if __name__ == '__main__':
    input_folder_t = "GroundTrueMasks/"
    input_folder_ac = "acResultsMasks/CV/" # cambiar CV to GAC
    output_folder = 'Metrics/'

    trueMasks = os.listdir(input_folder_t)
    iouArray = []
    diceArray = []

    for i in range(436): #cambar a 88 cuando se use GAC
        iouValues = []
        diceValues = []
        for mask_t in trueMasks:
            name_1 = input_folder_t + mask_t
            gray1 = cv2.imread(name_1, cv2.IMREAD_GRAYSCALE)
            ret, img1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
            imgT = adjust_data(img1)

            mask_id = re.search(r'\d+', mask_t).group()
            mask_number = name_1.split("_")[-1].split(".")[0]

            name_2 = input_folder_ac + 'mask_CVBW40' + '_' + mask_id + '_' + mask_number+ '.jpg' + '_iteration' + str(i) + '.jpg'
            gray2 = cv2.imread(name_2, cv2.IMREAD_GRAYSCALE)
            ret, img2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
            imgAC = adjust_data(img2)

            iouValues.append((iou(imgT, imgAC)).numpy())
            diceValues.append((dice_coef(imgT, imgAC)).numpy())

        iouArray.append(np.mean(iouValues))
        diceArray.append(np.mean(diceValues))

    file_name = 'IOU_40_CV' #cambiar CV a GAC
    output_file = os.path.join(output_folder, file_name + '.txt')

    file_name_1 = 'DICE_40_CV' #cambiar CV a GAC
    output_file_1 = os.path.join(output_folder, file_name_1 + '.txt')

    with open(output_file, 'w') as file:
        for j, metricI in enumerate(iouArray):
            file.write(str(j) + ',' + str(metricI) + "\n")

    with open(output_file_1, 'w') as file:
        for k, metricD in enumerate(diceArray):
            file.write(str(k) + ',' + str(metricD) + "\n")