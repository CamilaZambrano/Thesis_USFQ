close all;
clc;

input_image = 'DBimg1_g.jpg';
output_image = 'DBimg1_Mass_2_c.jpg';

bbox_Xminpoint = 447;
bbox_Yminpoint = 178;
bbox_Xmaxpoint = 506;
bbox_Ymaxpoint = 230;

top_left = [bbox_Xminpoint, bbox_Yminpoint];
bottom_right = [bbox_Xmaxpoint, bbox_Ymaxpoint];

crop_image(input_image, output_image, top_left, bottom_right);

function crop_image(input_path, output_path, top_left, bottom_right)
    image = imread(input_path);
    imshow(image)
    left = max(top_left(1), 1);
    top = max(top_left(2), 1);
    right = min(bottom_right(1), size(image, 2));
    bottom = min(bottom_right(2), size(image, 1));
    
    cropped_image = image(top:bottom, left:right, :);
    figure, imshow(cropped_image)
    imwrite(cropped_image, output_path);
end