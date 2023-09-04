close all;
clc;

filePath = 'boundingBoxCrop.txt';

inputImages = 'masks/';
outputImages = 'cropMasks/';

%inputMasks = 'Masks/InBreast_Masks/GroundTrueMasks/';
%outputMasks = 'Crop/Masks/GroundTrue/';

fid = fopen(filePath, 'r');

tline = fgetl(fid);
while ischar(tline)
    data = strsplit(tline, ',');

    file_name = data{1};
    category = data{2};
    bbox_Xminpoint = str2double(data{3});
    bbox_Yminpoint = str2double(data{4});
    bbox_Xmaxpoint = str2double(data{5});
    bbox_Ymaxpoint = str2double(data{6});

    %nameImage = strcat(file_name, '_', category);
    nameMask = strcat(file_name, '_bw_', category);
    des = strsplit(category, '_');
    numberMass = str2double(des{2});

    top_left = [bbox_Xminpoint, bbox_Yminpoint];
    bottom_right = [bbox_Xmaxpoint, bbox_Ymaxpoint];

    %input_image = fullfile(inputImages, strcat(file_name, '.jpg'));
    %output_image = fullfile(outputImages, strcat(nameImage, '.jpg'));
    %crop_image(input_image, output_image, top_left, bottom_right);

    input_mask = fullfile(inputImages, strcat(nameMask, '.png'));
    output_mask = fullfile(outputImages, strcat(nameMask, '_crop.jpg'));
    crop_image(input_mask, output_mask, top_left, bottom_right);

    tline = fgetl(fid);
end

fclose(fid);

function crop_image(input_path, output_path, top_left, bottom_right)
    image = imread(input_path);
    left = max(top_left(1), 1);
    top = max(top_left(2), 1);
    right = min(bottom_right(1), size(image, 2));
    bottom = min(bottom_right(2), size(image, 1));
    
    cropped_image = image(top:bottom, left:right, :);
    imwrite(cropped_image, output_path);
end
