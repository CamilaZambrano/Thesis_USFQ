import os

def mean(max, min):
    m = (max + min) / 2
    return m

filePath = 'Coordenates/boundingBoxes.txt'
output_folder = 'Coordenates/CenterPoints'

with open(filePath, 'r') as file:
    for line in file:
        # Eliminar espacios en blanco y separar por comas
        data = line.strip().split(',')

        # Asignar los datos a variables
        file_name = data[0]
        category = data[3]
        bbox_Xminpoint = data[4]
        bbox_Yminpoint = data[5]
        bbox_Xmaxpoint = data[6]
        bbox_Ymaxpoint = data[7]

        name = file_name + '_' + category
        des = category.strip().split('_')
        numberMass = des[1]

        centerx = mean(int(bbox_Xmaxpoint), int(bbox_Xminpoint))
        centery = mean(int(bbox_Ymaxpoint), int(bbox_Yminpoint))

        output_file = os.path.join(output_folder, name + '.txt')

        with open(output_file, 'w') as file_out:
            file_out.write(file_name + ',' + numberMass + ',' + str(centerx) + ',' + str(centery))

print("Se han guardado correctamente todos los center points")