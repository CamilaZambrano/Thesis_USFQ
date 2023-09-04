text_file = ['metrics/crop/Final/DICE_10_CVC.txt'];
fid = fopen(text_file, 'r');
valorx = [];
valory = [];
linea = fgetl(fid);
while ischar(linea)
    datos = textscan(linea, '%f, %f');
    dx = datos{1};
    dy = datos{2};
    valorx = [valorx,dx];
    valory = [valory,dy];
    linea = fgetl(fid);
end

fclose(fid);
plot(valorx, valory)
hold on