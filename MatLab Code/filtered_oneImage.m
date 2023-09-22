inputFile = "C:/Users/DELL/Downloads/morphsnakes-master/YOLO/grayscale_22670147_1_crop.jpg"
outputFile = "C:/Users/DELL/Downloads/morphsnakes-master/YOLO/22670147_1_crop_F.jpg";

grayImage = imread(inputFile);
paddingSize = floor([5 5] / 2);
paddedImage = padarray(grayImage, paddingSize, 'replicate');

% Aplica el filtro mediano
filteredImage = medfilt2(paddedImage, [5 5]);
filteredImage = filteredImage(paddingSize(1)+1:end-paddingSize(1), paddingSize(2)+1:end-paddingSize(2));

[rows, cols] = size(filteredImage);
rgbImage = cat(3, filteredImage, filteredImage, filteredImage);

imwrite(rgbImage, outputFile);

disp('Proceso completado.');