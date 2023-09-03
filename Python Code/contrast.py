import cv2
import os
from PIL import Image

input_folder = "DatabaseImages/InBreast/Original/"
output_folder = "DatabaseImages/InBreast/Processed/"
gray_folder = "DatabaseImages/InBreast/GrayScale/"
clahe_folder = "DatabaseImages/InBreast/CLAHE/"

# Obtener la lista de archivos en la carpeta
images = os.listdir(input_folder)

for image in images:
    image_name = image

    # Cargar la imagen en formato RGB
    img_rgb = Image.open(input_folder + image_name)
    # Convertir la imagen a escala de grises
    img_grayscale = img_rgb.convert('L')
    # Guardar la imagen resultante en formato JPG
    img_grayscale.save(gray_folder + "grayscale_" + image_name)

    # Cargar la imagen de entrada en escala de grises
    imagen_entrada = cv2.imread(gray_folder + "grayscale_" + image_name, cv2.IMREAD_GRAYSCALE)
    # Crear un objeto CLAHE con los parámetros deseados
    clahe = cv2.createCLAHE(clipLimit=3)
    # Aplicar el algoritmo CLAHE a la imagen de entrada
    imagen_salida = clahe.apply(imagen_entrada)
    # Guardar la imagen resultante en formato JPG
    cv2.imwrite(clahe_folder + "clahe_" + image_name, imagen_salida, [int(cv2.IMWRITE_JPEG_QUALITY), 10])

    # Cargar la imagen en formato RGB
    img_rbg1 = Image.open(clahe_folder + "clahe_" + image_name)
    # Convertir la imagen a escala de grises
    img_RGB = img_rbg1.convert('RGB')
    # Guardar la imagen resultante en formato JPG
    img_RGB.save(output_folder + "contrast_" + image_name)
