#  Importing contents to be used in the project
from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import os
from PIL import Image

# This part of the code goes through the folder and then creates ol' matrix of each image and appends it in the image_list.
images_list=[]
for fileName in os.listdir("./"):
    if fileName.endswith(".jpg"):
        image=Image.open(fileName)
        image=np.float32(image)
        images_list.append(image)
        

# Asks user to input the thresold value which determines the concentration of the changes in the captured images.
th=np.float32(input("Enter the thresold limit: "))

# This part of code sums all thee images matrices together for further calculations of mean:
image_average=[0,0,0]
for index in range(0, len(images_list)):
    image_average+=images_list[index]

# Calculating the mean image of the images:
mean_image=image_average/len(images_list)

# Using Standard Deviation rule to calculate the S.D
difference=(images_list[0]-mean_image)**2
for j in range (1,len(images_list)):
    difference+=(images_list[j]-mean_image)**2
difference=difference/(len(images_list)-1)
image_SD=difference**(1/2)

#Condition if the S.D is greated than threshold value, change the pixel value to red i.e. (255.0,0.0,0.0)
for x in range(0,len(mean_image)):
    for y in range(0,len(mean_image[x])):
        if (image_SD[x][y]>[th,th,th]).any():
            mean_image[x][y]=[255.0,0.0,0.0]
            
# Display the final image.
mean_image_display2=np.clip(mean_image,0,255)
mean_image_display2=np.uint8(mean_image)
mplot.imshow(mean_image_display2)
mplot.show()
