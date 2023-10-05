%
%
%
%
close all;
clear all;
clc;
txt_files = dir('textfiles/');
% reading all text files
for i=3:length(txt_files)
    [txt_filepath,txt_name,txt_ext] = fileparts(txt_files(i).name);
    [img_filepath,img_name,img_ext] = fileparts(strcat('images/',txt_name,'.jpg'));
    fileID = fopen(strcat('textfiles/',txt_name,txt_ext));
    img = imread(strcat(img_filepath,'/', img_name, img_ext));
    [img_height, img_width, ~] = size(img); % obtener las dimensiones de la imagen original
    % loop for reading and storing in an array structure each text file
    j=1;
    clear data;
    while ~feof(fileID)
        data(j).line = fgetl(fileID);
        j=j+1;
    end
    fclose(fileID);
    % processing each file/image to produce the binary mask image
    for k=1: length(data)
        if (contains(data(k).line, 'Mass'))
            lesion = data(k).line;
            x = str2num(data(k+1).line);
            y = str2num(data(k+2).line);
            bw = roipoly(img, x,y);
            bw_resized = imresize(bw,[size(img,1) size(img,2)]); % ajusta el tamaño de la máscara
            imwrite(bw_resized, strcat('masks','/',img_name, '_bw_', lesion, '.png'), 'png');
        end 
    end 
end


