% Test the cropping function
input_image = 'WFoutput1.jpg'; % Replace with the actual path
cropped_image = crop_black_background(input_image);

% You can also save the cropped image using imwrite
imwrite(cropped_image, ['DBimg_g1.png']);

% Test the cropping function
%input_image = 'WFoutput2.jpg'; % Replace with the actual path
%cropped_image = crop_black_background(input_image);

% You can also save the cropped image using imwrite
%imwrite(cropped_image, ['DBimg_g2.png']);

function cropped_image = crop_black_background(input_image)
    % Read the input image
    image = imread(input_image);

    % Convert the image to grayscale
    gray_image = rgb2gray(image);

    % Define a threshold value to identify the background
    threshold = 200; % You can adjust this value based on your images

    % Create a binary mask where background pixels are set to 1
    background_mask = gray_image >= threshold;

    % Find the bounding box of the foreground (non-background) region
    [rows, cols] = find(~background_mask);
    top_row = min(rows);
    bottom_row = max(rows);
    left_col = min(cols);
    right_col = max(cols);

    % Crop the image to the bounding box
    cropped_image = image(top_row:bottom_row, left_col:right_col, :);

    % Display the cropped image
    imshow(cropped_image);
end