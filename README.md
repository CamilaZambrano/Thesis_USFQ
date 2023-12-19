# Segmentación de Masas de Cáncer de Mama Utilizando Técnicas de Procesamiento Digital de Imágenes

## Ojetivo del Proyecto:
Desarrollar un método de segmentación basado en técnicas de procesamiento digital de imágenes para maximizar el desempeño de la segmentación de masas en imágenes de mamografías.
 
## Modo de Uso:
1. Intalar python 3.9
2. Descargar la carpeta con el código
3. Opcional: crear un ambiente virutal usando conda (usar como guia el archivo install_conda.txt como guia)
4. Instalar en el IDE que se este usando las librearias requeridas usando el comando de la linea x del archivo install_conda.txt
5. Crear las carpeta acResultMasks y dentro de esta, las carpetas CV y GAC  
**Nota** CV iniciales para Chan-Vase y GAC iniciales para Geodésico
6. Correr el archivo test crop (los modelos están seteados por default con las configuraciones que dieron los mejores resultados)

## Base de Datos Original:
La base de datos utilizada para este proyecto fue INbreast y se puede encontrar en https://www.kaggle.com/datasets/ramanathansp20/inbreast-dataset?resource=download

## Importante:
Dado a que este proyecto forma parte de un trabajo de investigacion el código para la creación de la base de datos experimental y la máscaras creadas para obtener las métricas no vienen adjuntos. 
