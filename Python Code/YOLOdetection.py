import torchvision.transforms as transforms
from ultralytics import YOLO
from PIL import Image
import matlab.engine
import os
import cropSingleImage as crop
import testCropF as AC
import grayscaleOne as GS
import cv2

image_path = "C:/Users/DELL/Downloads/morphsnakes-master/YOLO/22670147.jpg"
image = Image.open(image_path)

transform = transforms.Compose(
    [transforms.Resize((640, 640)), transforms.ToTensor()]
)
input_image = transform(image).unsqueeze(0)

model = YOLO('C:/Users/DELL/Downloads/morphsnakes-master/YOLO/best.pt')
detections = model(input_image)

print(detections[0].boxes)

bbooxModel = detections[0].boxes.xyxyn[0]
bbooxCoordenatesTensor = [bbooxModel[0],bbooxModel[1],bbooxModel[2],bbooxModel[3]]

bbooxCoordenatesPython = []
for coordinate in bbooxCoordenatesTensor:
    numpy_array = coordinate.numpy()
    python_float = float(numpy_array)
    bbooxCoordenatesPython.append(python_float)

outputPath = 'YOLO/22670147_1_crop.jpg'
OriginalImage = 'DatabaseImages/InBreast/Original/22670147.jpg'
top_left = (bbooxCoordenatesPython[0]*800, bbooxCoordenatesPython[1]*800)
bottom_right = (bbooxCoordenatesPython[2]*800, bbooxCoordenatesPython[3]*800)

im = cv2.imread(OriginalImage)
sizeh, sizew, channels = im.shape
ratioh, ratiow = sizeh/800, sizew/800
top_leftOriginal = [int(top_left[0]*ratiow), int(top_left[1]*ratioh)]
bottom_rightOriginal = [int(bottom_right[0]*ratiow), int(bottom_right[1]*ratioh)]

print(top_leftOriginal, bottom_rightOriginal)

crop.crop_and_save_image(OriginalImage, outputPath, top_leftOriginal, bottom_rightOriginal)
GS.gray()

script_directory = 'Matlab/'
matlab_script_path = os.path.join(script_directory, 'filtered_oneImage.m')
eng = matlab.engine.start_matlab()
eng.run(matlab_script_path, nargout=0)
eng.quit()

image = Image.open('YOLO/22670147_1_crop_F.jpg')
width, height = image.size
centerx = width/2
centery = height/2

centerPoint = [centerx, centery]
print(centerPoint)

AC.pipLine(centerPoint, "22670147")

script_directory = 'Matlab/'
matlab_script_path_CV = os.path.join(script_directory, 'cropToOriginalMaskCV.m')
matlab_script_path_GAC = os.path.join(script_directory, 'cropToOriginalMaskGAC.m')
eng = matlab.engine.start_matlab()
eng.run(matlab_script_path_CV, nargout=0)
eng.run(matlab_script_path_GAC, nargout=0)
eng.quit()

