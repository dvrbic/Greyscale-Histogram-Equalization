import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def histogram_equalize(img):
    image = np.asarray(img)
    
    ints_array = np.zeros(256)
    x_axis, y_axis = image.shape[:2]
    for i in range(0, x_axis):
        for j in range(0, y_axis):
            ints = image[i,j]
            ints_array[ints] = ints_array[ints] + 1

    

    MN = 0
    for i in range(1, 256):
        MN = MN + ints_array[i]
   
    
    array_pdf = ints_array/MN
   

    CDF = 0
    CDF_matrix = np.zeros(256)
    for i in range(1, 256):
        CDF = CDF + array_pdf[i]
        CDF_matrix[i] = CDF
    
    
    final_array = np.zeros(256)
    final_array = (CDF_matrix * 255)
    for i in range (1,256):
        final_array[i] = math.ceil(final_array[i])
        if(final_array[i] > 255):
            final_array[i] = 255
    

    new_img = np.zeros(img.shape)
    for i in range(0, x_axis):
        for j in range(0, y_axis):
            for value in range(0, 255):
                if (image[i,j] == value):
                    new_img[i,j] = final_array[value]
                    break
    return new_img
    

input_image = cv2.imread('207056.jpg', 0)
out_image = histogram_equalize(input_image)
cv2.imwrite('new_goats.jpg', out_image)
