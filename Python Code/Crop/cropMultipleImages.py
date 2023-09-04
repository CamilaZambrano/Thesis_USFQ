import os
from PIL import Image

def crop_image(input_path, output_path, top_left, bottom_right):
    image = Image.open(input_path)
    left, top = top_left
    right, bottom = bottom_right
    # Recorta la imagen utilizando las coordenadas
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)

filePath = 'Crop/Coordenates/boundingBoxCrop.txt'

inputImages = 'DatabaseImages/InBreast/Original/'
outputImages = 'Crop/Original'

inputMasks = 'Masks/InBreast_Masks/GroundTrueMasks/'
outputMasks = 'Crop/Masks/GroundTrue'

with open(filePath, 'r') as file:
    for line in file:
        # Eliminar espacios en blanco y separar por comas
        data = line.strip().split(',')

        # Asignar los datos a variables
        file_name = data[0]
        category = data[1]
        bbox_Xminpoint = data[2]
        bbox_Yminpoint = data[3]
        bbox_Xmaxpoint = data[4]
        bbox_Ymaxpoint = data[5]

        nameImage = file_name + '_' + category
        nameMask = file_name + '_bw_' + category
        des = category.strip().split('_')
        numberMass = des[1]

        top_left = (int(bbox_Xminpoint), int(bbox_Yminpoint))
        bottom_right = (int(bbox_Xmaxpoint), int(bbox_Ymaxpoint))

        input_image = os.path.join(inputImages, file_name + '.jpg')
        output_image = os.path.join(outputImages, nameImage + '.jpg')
        crop_image(input_image, output_image, top_left, bottom_right)

        input_mask = os.path.join(inputMasks, nameMask + '.png')
        output_mask = os.path.join(outputMasks, nameMask + '_crop.jpg')
        crop_image(input_mask, output_mask, top_left, bottom_right)

print("Se han guardado correctamente todos los crops")
