function paintROI(idImage)
    splitValues = split(idImage, '_');
    nameImage = splitValues{1};
    numberImage = splitValues{2};

    input_path = 'images/' + nameImage + '.jpg';
    input_OriginalMask = 'masks/'+ nameImage + '_bw_Mass_' + numberImage + '.png';
    input_CVMask = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/masks/whole/CV/mask_CVBWCF_' + idImage + '_final.jpg';
    %input_GACMask = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/masks/whole/GAC/mask_GACBWCF_' + idImage + '_final.jpg';

    output_CVMask = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/overlay/CV/CV_' + idImage + '_overlay.jpg';
    %output_GACMask = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/overlay/GAC/GAC_' + idImage + '_overlay.jpg';
    output_OriginalMask = 'C:/Users/DELL/Downloads/morphsnakes-master/YOLO/overlay/original/original_' + idImage + '_overlay.jpg'

    io = imread(input_path);
    iob_p = imread(input_OriginalMask);
    iob_pCV = imread(input_CVMask);
    %iob_GAC = imread(input_GACMask);

    green = zeros(size(io,1),size(io,2),3);
    green(:,:,2)=1;
    red = zeros(size(io, 1),size(io, 2),3);
    red(:,:,1) = 1;

    figure,imshow(io)
    hold on
    h=imshow(green);
    hold off
    alpha_value = 0.2;
    set(h, 'AlphaData', iob_pCV * alpha_value);
    saveas(h, output_CVMask);

    %figure,imshow(io)
    %hold on
    %h=imshow(green);
    %hold off
    %alpha_value = 0.2;
    %set(h, 'AlphaData', iob_pGAC * alpha_value);
    %saveas(h, output_GACMask);

    figure,imshow(io)
    hold on
    h=imshow(red);
    hold off
    alpha_value = 0.2;
    set(h, 'AlphaData', iob_p * alpha_value);
    saveas(h, output_OriginalMask);

    disp('Overlays completed');
end