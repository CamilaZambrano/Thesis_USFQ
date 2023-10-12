function cropToOriginalMaskGAC(coordenatesMin, coordenatesMax, idImage)
    splitValues = split(idImage, '_');
    nameImage = splitValues{1};
    numberImage = splitValues{2};

    input_maskOriginal = 'masks/' + nameImage + '_bw_Mass_' + numberImage + '.png'
    input_maskAC = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/masks/crop/GAC/mask_GACBWCF_' + idImage + '.jpg'
    output_maskAC = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/masks/whole/GAC/mask_GACBWCF_' + idImage + '_final.jpg'

    imagen_original = imread(input_maskOriginal);
    mascara_binaria_recortada = imread(input_maskAC);

    % Obtener las dimensiones de ambas imágenes
    [alto_original, ancho_original, ~] = size(imagen_original);
    [alto_recortado, ancho_recortado] = size(mascara_binaria_recortada);

    % Crear una máscara negra del tamaño de la imagen original
    mascara_negra = zeros(alto_original, ancho_original, 'uint8');

    % Definir las coordenadas de recorte en la imagen original
    xmin = coordenatesMin{1};
    ymin = coordenatesMin{2};
    xmax = coordenatesMax{1};
    ymax = coordenatesMax{2};

    y = ymin:ymax-1;
    x = xmin:xmax-1;

    % Colocar la máscara binaria recortada en las coordenadas adecuadas de la máscara negra
    mascara_negra(y, x) = mascara_binaria_recortada;

    % Guardar la máscara binaria ajustada
    imwrite(mascara_negra, output_maskAC);

    disp('GAC whole mask completed');
end