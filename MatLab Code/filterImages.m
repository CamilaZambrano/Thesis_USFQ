inputDirectory = 'grayScaleMC/';
outputDirectory = 'filtered/';

fileList = dir(fullfile(inputDirectory, '*.jpg'));

for i = 1:numel(fileList)
    inputFile = fullfile(inputDirectory, fileList(i).name);

    grayImage = imread(inputFile);
    paddingSize = floor([5 5] / 2);
    paddedImage = padarray(grayImage, paddingSize, 'replicate');

    % Aplica el filtro mediano
    filteredImage = medfilt2(paddedImage, [5 5]);
    filteredImage = filteredImage(paddingSize(1)+1:end-paddingSize(1), paddingSize(2)+1:end-paddingSize(2));

    [rows, cols] = size(filteredImage);
    rgbImage = cat(3, filteredImage, filteredImage, filteredImage);

    [~, filename, ext] = fileparts(fileList(i).name);
    outputFile = fullfile(outputDirectory, [filename '_F' ext]);
    imwrite(rgbImage, outputFile);
end

disp('Proceso completado.');