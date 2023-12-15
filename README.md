# Segmentación de Masas de Cáncer de Mama Utilizando Técnicas de Procesamiento Digital de Imágenes
Este repositorio fue creado con el próposito de llevar el versionamiento y documentación de este proyecto.

## Ojetivo del Proyecto:
Desarrollar un método de segmentación basado en técnicas de procesamiento digital de imágenes para maximizar el desempeño de la segmentación de masas en imágenes de mamografías.

## Modo de Uso:
1. Intalar python 3.9 y Matlab R2023a
2. Descargar las carpetas: Python_Code y Matlab_Code
3. Opcional: crear un ambiente virutal usando conda (usar como guia el archivo install_conda.txt como guia)
4. Instalar en el IDE que se este usando las librearias requeridas usando el comando de la linea x del archivo install_conda.txt
5. 

## Base de Datos:
La base de datos utilizada para este proyecto fue INbreast y se puede encontrar en https://www.kaggle.com/datasets/ramanathansp20/inbreast-dataset?resource=download

## Procesamiento de la base de datos: 
1. Se uso el programa de Osirix para poder obtener las imágenes que tenían masas y, de igual manera, se obtuvieron las coordenadas de la curva del contorno de las masas (carpeta Jsons en Python_Code).
2. Utilizando jsonFilesSingleMasses.py y jsonFilesMultipleMasses.py (carpeta Python_Code), se contruieron los archivos .txt (carpeta Python_Code/Coordenates/INbreastCurves)
3. Uitlizando building_mask_GT.m (Matlab_Code), se obtuvieron las máscaras binarias para las imágenes que tenían masas (Matlab_Code/masks)
4. Se utilizo https://products.aspose.app/imaging/es/conversion/dcm-to-jpg para poder pasar la imágenes con masas del formato .dcm a .jpg (Python_Code/INbreast)
6. 
