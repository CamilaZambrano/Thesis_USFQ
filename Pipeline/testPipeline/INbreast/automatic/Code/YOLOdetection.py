import torchvision.transforms as transforms
from ultralytics import YOLO
from PIL import Image
import matlab.engine
import cv2
import os

import cropSingleImage as crop
import testCropF as AC

def grayscale(inputPath, outputPath):
    img_rgb = Image.open(inputPath)
    # Convertir la imagen a escala de grises
    img_grayscale = img_rgb.convert('L')
    img_grayscale.save(outputPath)
    print("Grayscale completed")

input_folder_testing_images = 'YOLO/original/'
input_original_image_folder = 'DatabaseImages/InBreast/Original/'
output_crop = 'YOLO/crop/'
output_gray = 'YOLO/grayscale/'
output_filtered = 'YOLO/filtered/'

imagesOriginal = os.listdir(input_folder_testing_images)
for imageOriginal in imagesOriginal:
    # import the trained YOLO model
    model = YOLO('YOLO/best.pt')

    image_path = os.path.join(input_folder_testing_images, imageOriginal)
    image = Image.open(image_path)

    #resize a copy of the original image to fit the YOLO mode input
    transform = transforms.Compose([transforms.Resize((800, 800)), transforms.ToTensor()])
    YOLO_input_image = transform(image).unsqueeze(0)

    #made detections in the resize image with the YOLO model
    detections = model(YOLO_input_image)

    if detections[0].boxes.xyxyn[0].size().numel() > 0:
        nameImage = str(imageOriginal).split(".")[0]

        # obtain the size of the original image
        originalImage = os.path.join(input_original_image_folder, imageOriginal)
        im = cv2.imread(originalImage)
        sizeh, sizew, channels = im.shape
        ratioh, ratiow = sizeh / 800, sizew / 800

        # obtain the coordenates of the bounding boxes obtained from the YOLO model
        for i in range(len(detections[0].boxes.xyxyn)):
            idImage = nameImage + '_' + str(i + 1)
            cropImage = os.path.join(output_crop, idImage + '_crop.jpg')
            grayImage = os.path.join(output_gray, idImage + '_grayscale.jpg')
            filteredImage = os.path.join(output_filtered, idImage + '_filtered.jpg')

            bbooxModel = detections[0].boxes.xyxyn[i]
            bbooxCoordenatesTensor = [bbooxModel[0], bbooxModel[1], bbooxModel[2], bbooxModel[3]]
            bbooxCoordenatesPython = []

            # change the bounding box coordenates from tensorflow obtects to float
            for coordinate in bbooxCoordenatesTensor:
                numpy_array = coordinate.numpy()
                python_float = float(numpy_array)
                bbooxCoordenatesPython.append(python_float)

            # obtain the bounding box coordenates in terms of the original image scale
            top_left_YOLO = (bbooxCoordenatesPython[0] * 800, bbooxCoordenatesPython[1] * 800)
            bottom_right_YOLO = (bbooxCoordenatesPython[2] * 800, bbooxCoordenatesPython[3] * 800)
            top_left_Original = [int(top_left_YOLO[0] * ratiow), int(top_left_YOLO[1] * ratioh)]
            bottom_right_Original = [int(bottom_right_YOLO[0] * ratiow), int(bottom_right_YOLO[1] * ratioh)]

            # crop the ROI obtained from the detections in the YOLO model from the original image
            crop.crop_and_save_image(originalImage, cropImage, top_left_Original, bottom_right_Original)
            # pass the crop image to grascale
            grayscale(cropImage, grayImage)

            # pass the image through the Median filter to reduce noise
            eng = matlab.engine.start_matlab()
            eng.filtered_oneImage(grayImage, filteredImage, nargout=0)
            eng.quit()

            # preform the segmentation with Active Countour models (geodesic and chan-vase)
            image_input_AC = Image.open(filteredImage)
            width, height = image_input_AC.size
            centerx = width / 2
            centery = height / 2
            centerPoint = [centerx, centery]
            AC.pipLine(centerPoint, filteredImage)
            print("AC completed")

            # obtain the masks in terms of the original image
            eng = matlab.engine.start_matlab()
            eng.cropToOriginalMaskCV(top_left_Original, bottom_right_Original, idImage, nargout=0)
            #eng.cropToOriginalMaskGAC(top_left_Original, bottom_right_Original, idImage, nargout=0))

            # overlay the original image, the obtained masks and the actual mask
            eng.paintROI(idImage, nargout=0)
            eng.quit()
