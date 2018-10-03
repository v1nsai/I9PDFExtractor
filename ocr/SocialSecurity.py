# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:51:22 2018

@author: Brandon Croarkin
"""

from wand.image import Image
import numpy as np
import pandas as pd
#import sys
import io
import PIL
import pytesseract
import re
import json
import os
import matplotlib.pyplot as plt
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

#make array with social security images
folder = 'C:\\Users\\Brandon Croarkin\\Documents\\GreenZone\\OCR\\NiFiTesting\\PythonPNGs\\CroppedImages\\Social Security'
images = []
os.chdir(folder)
for image in os.listdir(folder):
    if image.endswith(".png"):
        images.append(image)
        
####make a function to display an image from its filename
def showImage(image):
    data = plt.imread(image)
    plt.imshow(data)
    
###make a function to put an array on a 0 to 1 scale
def scale(array):
    max = array.max()
    return(array/max)
    
###resize images to same dimensions
def resize(item, width, height):
    im = PIL.Image.open(item)
    im = im.resize((width,height), PIL.Image.ANTIALIAS)
    return(im)     
    
###take the 3rd dimension of data to get 2 dimensional image

#grabbing an example image to test on
data = plt.imread(images[14])
#just choosing the 3rd dimension of the image, which is a 2 dimensional array
if len(data.shape) > 2:
    data = data[:,:,2]
height, width = data.shape

#####Version 1 - use a threshold to remove boxes 

#get column and row sums and change to 1 if value below threshold
threshold = 0.5
for i in range(height):
    row_average = data[i,].mean()
    if row_average < threshold:
        data[i,] = 1
    
for i in range(width):
    col_average = data[:,i].mean()
    if col_average < threshold:
        data[:,i] = 1

plt.imshow(data)  

#convert back to an array
im = PIL.Image.fromarray(np.uint8(data*255))

#test tesseract output
text = pytesseract.image_to_string(im)

def SStesseract(image):
    #convert image to array
    data = plt.imread(image)
    #if 3 dimensional...
    ##just choosing the 3rd dimension of the image, which is a 2 dimensional array
    if len(data.shape) > 2:
        data = data[:,:,2]
    #getting the height and width
    height, width = data.shape
    
    #set threshold
    threshold = 0.5
    
    #get column and row sums and change to 1 if value below threshold
    for i in range(height):
        row_average = data[i,].mean()
        if row_average < threshold:
            data[i,] = 1
        
    for i in range(width):
        col_average = data[:,i].mean()
        if col_average < threshold:
            data[:,i] = 1
    
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))
    
    #test tesseract output
    text = pytesseract.image_to_string(im)
    return(text)
    

#SUCCESS

#####Version 2 - Look for number of consecutive pixels under threshold 
image = images[27]
im = resize(image, 300, 60)
data = scale(np.array(im))
if len(data.shape) > 2:
    data = data[:,:,2]
height, width = data.shape

threshold = 0.85
#iterate over the rows and get the max number of consecutive dark pixels
row_counts= []
max_row_counts = []
for i in range(height):
    count = 0
    for j in range(width):
        val = data[i,j]
        if (j + 1 == width):
            if len(row_counts) > 0:
                max_no = max(row_counts)
                max_row_counts.append(max_no)
                row_counts = []
                if max_no > 60:
                    data[i,] = 1
            else:
                continue
        else:
            if (val < threshold):
                count = count + 1
            elif (val >= threshold) & (count > 0):
                row_counts.append(count)
                count = 0
            else:
                continue

#iterate over the columns and get the max number of consecutive dark pixels
col_counts= []
max_col_counts = []
for i in range(width):
    count = 0
    for j in range(height):
        val = data[j,i]
        if (j + 1 == height):
            if len(col_counts) > 0:
                max_no = max(col_counts)
                max_col_counts.append(max_no)
                col_counts = []
                if max_no > 30:
                    data[:,i] = 1
            else:
                continue
        else:
            if (val < threshold):
                count = count + 1
            elif (val >= threshold) & (count > 0):
                col_counts.append(count)
                count = 0
            else:
                continue
            
#convert back to an array
im = PIL.Image.fromarray(np.uint8(data*255))

#test tesseract output
text = pytesseract.image_to_string(im)     

def SStesseract2(image):
    im = resize(image, 300, 60)
    data = scale(np.array(im))
    #if 3 dimensional...
    ##just choosing the 3rd dimension of the image, which is a 2 dimensional array
    if len(data.shape) > 2:
        data = data[:,:,2]
    height, width = data.shape
    
    threshold = 0.85
    #iterate over the rows and get the max number of consecutive dark pixels
    row_counts= []
    max_row_counts = []
    for i in range(height):
        count = 0
        for j in range(width):
            val = data[i,j]
            if (j + 1 == width):
                if len(row_counts) > 0:
                    max_no = max(row_counts)
                    max_row_counts.append(max_no)
                    row_counts = []
                    if max_no > 50:
                        data[i,] = 1
                else:
                    continue
            else:
                if (val < threshold):
                    count = count + 1
                elif (val >= threshold) & (count > 0):
                    row_counts.append(count)
                    count = 0
                else:
                    continue
    
    #iterate over the columns and get the max number of consecutive dark pixels
    col_counts= []
    max_col_counts = []
    for i in range(width):
        count = 0
        for j in range(height):
            val = data[j,i]
            if (j + 1 == height):
                if len(col_counts) > 0:
                    max_no = max(col_counts)
                    max_col_counts.append(max_no)
                    col_counts = []
                    if max_no > 20:
                        data[:,i] = 1
                else:
                    continue
            else:
                if (val < threshold):
                    count = count + 1
                elif (val >= threshold) & (count > 0):
                    col_counts.append(count)
                    count = 0
                else:
                    continue
            
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))

    #test tesseract output
    text = pytesseract.image_to_string(im) 
    return(text)

#######################################################
#####################TESTING###########################
#######################################################

text_output = []
for image in images:
    text_output.append(SStesseract(image))
    
text_output2 = []
for image in images:
    text_output2.append(SStesseract2(image))

text_output3 = []
for image in images:
    text_output3.append(pytesseract.image_to_string(image))
