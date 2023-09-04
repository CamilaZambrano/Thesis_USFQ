% Cargar la imagen original y la máscara binaria
imagen_original = imread('crop/50994273_Mass_1.jpg');
mascara_binaria = imread('cropMasks/50994273_bw_Mass_1_crop.jpg');

% Convertir la máscara a una imagen RGB con canal alfa (transparencia)
mascara_rgb = cat(3, mascara_binaria, mascara_binaria, mascara_binaria);
mascara_rgb(:, :, 4) = 0.5 * double(mascara_binaria);  % Ajustar nivel de transparencia

% Mostrar la imagen original y sobreponer la máscara
figure;

subplot(1, 2, 1);
imshow(imagen_original);
title('Imagen Original');

subplot(1, 2, 2);
imshow(imagen_original);
hold on;
h = imshow(mascara_rgb);
set(h, 'AlphaData', mascara_binaria);  % Aplicar transparencia
title('Máscara Sobreponida');

% Ajustar propiedades de la figura
sgtitle('Sobreponer Máscara en Imagen Original');