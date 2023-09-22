% Cargar la imagen original y la máscara binaria recortada
imagen_original = imread('masks\22670147_bw_Mass_1.png');
mascara_binaria_recortada = imread('C:\Users\DELL\Downloads\morphsnakes-master\YOLO\mask_GACBWCF__22670147.jpg');

% Obtener las dimensiones de ambas imágenes
[alto_original, ancho_original, ~] = size(imagen_original);
[alto_recortado, ancho_recortado] = size(mascara_binaria_recortada);

% Crear una máscara negra del tamaño de la imagen original
mascara_negra = zeros(alto_original, ancho_original, 'uint8');

% Definir las coordenadas de recorte en la imagen original
xmin = 2274; 
ymin = 1095; 
xmax = 2907;
ymax = 1579;

y = ymin:ymax-1;
x = xmin:xmax-1;

% Colocar la máscara binaria recortada en las coordenadas adecuadas de la máscara negra
mascara_negra(y, x) = mascara_binaria_recortada;

% Guardar la máscara binaria ajustada
imwrite(mascara_negra, 'C:\Users\DELL\Downloads\morphsnakes-master\YOLO\mask_GACBWCF__22579730_2_final.png');