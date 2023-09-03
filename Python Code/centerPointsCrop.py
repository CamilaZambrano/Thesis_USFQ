from PIL import Image
import os

inputPath = 'Crop/Original/'
output_folder = 'Crop/CenterPoints'
images = os.listdir(inputPath)

for image_file in images:
    imagePath = inputPath + image_file
    image = Image.open(imagePath)

    width, height = image.size
    centerx = width/2
    centery = height/2

    image_name = image_file.split('.')[0]
    output_file = os.path.join(output_folder, image_name + '_crop.txt')

    with open(output_file, 'w') as file_out:
        file_out.write(image_name + ',' + str(centerx) + ',' + str(centery))

print("Se han guardado correctamente todos los center points")