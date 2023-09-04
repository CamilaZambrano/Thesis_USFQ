% Leer la imagen binaria (máscara)
mask = imread('cropMasks/50994273_bw_Mass_1_crop.jpg');

% Encontrar los contornos del objeto en la máscara
contours = bwboundaries(mask);

% Crear una figura para mostrar el contorno
figure;
imshow("1.jpg");
hold on;

% Dibujar los contornos en la figura
for k = 1:length(contours)
    boundary = contours{k};
    plot(boundary(:,2), boundary(:,1), 'r', LineWidth=0.01); % Dibuja el contorno en rojo
end

hold off;
saveas(gcf, 'WFouput1_g.png');
