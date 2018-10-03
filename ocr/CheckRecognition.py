# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:29:38 2018

@author: Brandon Croarkin
"""

import numpy as np
import pandas as pd
import PIL
import matplotlib.pyplot as plt
import os

##########READ IN DATA#####################
path = 'C:/Users/Brandon Croarkin/Documents/GreenZone/OCR/NiFiTesting/PythonPNGs/CroppedImages/attestation/4 boxes/All'

####Retrieve filenames of all images in image_path
path = 'C:/Users/Brandon Croarkin/Documents/GreenZone/OCR/NiFiTesting/PythonPNGs/CroppedImages/attestation/4 boxes/All'
os.chdir(path)
dirs = os.listdir(path)
images = []
for item in dirs:
    if item.endswith(".png") and os.path.isfile(path+ '/' +item):
        images.append(item)
images = np.asarray(images)

####make a function to display an image from its filename
def showImage(image):
    data = plt.imread(image)
    plt.imshow(data)

#############DATA PREPROCESSING#########################

def renameFiles(folder_path):
    os.chdir(folder_path)
    files = []
    for item in os.listdir(folder_path):
        if item.endswith(".png"):
            files.append(item) 
    box_no = folder_path[-1]
    for i in range(len(files)):
        filename = files[i]
        new_filename = box_no + "_file" + str(i) + ".png"
        os.rename(filename, new_filename)

folder_path1 = 'C:/Users/Brandon Croarkin/Documents/GreenZone/OCR/NiFiTesting/PythonPNGs/CroppedImages/attestation/4 boxes/Box 1'
folder_path2 = folder_path1.replace("Box 1", "Box 2")  
folder_path3 = folder_path1.replace("Box 1", "Box 3") 
folder_path4 = folder_path1.replace("Box 1", "Box 4") 
folder_path5 = folder_path1.replace("Box 1", "No Box")  
folders = [folder_path1, folder_path2, folder_path3, folder_path4, folder_path5]    

for folder in folders:
    renameFiles(folder)
    
#resize them all to same dimensions
def resize(item, width, height):
    im = PIL.Image.open(path+"/"+item)
    im = im.resize((width,height), PIL.Image.ANTIALIAS)
    #im.save(item)
    return(im)
    
for item in images:
    resize(item)
    
image_width = 50
image_height = 200

def findCheckBox(image):
    #convert image to data array
    data = plt.imread(image)
    #find the height of the image to divide it
    width = data.shape[0]
    #create empty dicts to store values
    crops = {}
    means = {}
    #add the crop arrays and their means
    for i in range(4):
        crops["box" + str(i + 1)] = data[int(width/4)*i:int(width/4)*(i+1),:]
        means["box" + str(i + 1)] = crops["box" + str(i + 1)].mean()
    #find the maximum and minimum value from the dict and the range
    key_max = max(means.keys(), key=(lambda k: means[k]))
    key_min = min(means.keys(), key=(lambda k: means[k]))
    value_max = means[key_max]
    value_min = means[key_min]
    #value_mean = sum(means.values())/len(means)
    #value_sd = np.std(list(means.values()))
    #std_devs = (list(means.values())-value_mean)/value_sd
    value_range = value_max - value_min 
    if value_range > 0.01:
        return(min(means, key = means.get))
    else:
        return("no box")
    #biggest_dev = 1
    #box_checked = "no box"
    #for box, mean in means.items():
    #    std_dev = abs(mean-value_mean)/value_sd
    #    if std_dev > biggest_dev:
    #        biggest_dev = std_dev
    #        box_checked = box
    #return(box_checked)

findCheckBox(images[2])
findCheckBox(images[40])

#############TEST FUNCTION###############
box_actual = []
box_preds = []
i = 0
for image in images:
    box_actual.append(images[i][0])
    box_preds.append(findCheckBox(image))
    i += 1

df = pd.DataFrame({'Actual': box_actual, 'Predictions': box_preds})

