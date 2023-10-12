%io = imread("images/24055464.jpg");
%iob_p1 = imread('masks/24055464_bw_Mass_1.png');
%iob_p = imread('masks/20586908_bw_Mass_2.png');

io = imread("images\22678833.jpg");
%iob_p1 = imread('masks\22678833_bw_Mass_1.png');
iob_p1 = imread('C:\Users\DELL\Downloads\morphsnakes-master\YOLO\mask_CVBWCF__22678833_final.png');

%iob_p=bwperim(iob_p);
%iob_p1=bwperim(iob_p1);
green=zeros(size(io,1),size(io,2),3);
green(:,:,2)=1;

red = zeros(size(io, 1),size(io, 2),3);
red(:,:,1) = 1;

figure,imshow(io)
hold on

h=imshow(green);
%h=imshow(red);
hold off
alpha_value = 0.2;
set(h, 'AlphaData', iob_p1 * alpha_value);
saveas(h, "WFoutput1.jpg");

%figure,imshow(io)
%hold on

%h=imshow(red);
%hold off
%alpha_value = 0.2;
%set(h, 'AlphaData', iob_p * alpha_value);
%saveas(h, "WFoutput2.jpg");
