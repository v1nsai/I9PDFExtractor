# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:51:22 2018

@author: Brandon Croarkin
"""

import numpy as np
#import sys
import io
import PIL
import pytesseract
import os
import matplotlib.pyplot as plt

#make array with social security images
folder = 'C:\\Users\\Brandon Croarkin\\Documents\\GreenZone\\OCR\\NiFiTesting\\PythonPNGs\\CroppedImages\\Social Security'
images = []
os.chdir(folder)
for image in os.listdir(folder):
    if image.endswith(".png"):
        images.append(image)
        
byte_images = []
for image in images:
    im = PIL.Image.open(image)
    swap = io.BytesIO()
    im.save(swap, 'png')
    byte_images.append(im)
        
####make a function to display an image from its filename
def showImage(image):
    data = plt.imread(image)
    plt.imshow(data)
    
###make a function to put an array on a 0 to 1 scale
def scale(array):
    max = array.max()
    return(array/max)
    
###some image inverted the black and white pixels, function to tranform back
def invert(array):
    return(abs(1-array))
    
###resize images to same dimensions
def resize(item, width, height):
    im = item.resize((width,height), PIL.Image.ANTIALIAS)
    swap = io.BytesIO()
    im.save(swap, 'png')
    return swap
    
def SStesseract(image):
    #resize    
    swap = resize(image, 300, 60)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #scale image
    data = scale(data)
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
    
def SStesseract2(image):
    #resize    
    swap = resize(image, 300, 60)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #scale image
    data = scale(data)
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
                max_val = max(col_counts)
                col_counts = []
                max_col_counts.append(max_val)
            else:
                if (val < .95):
                    count = count + 1
                    col_counts.append(count)
                else:
                    count = 0
                    col_counts.append(0)
            
    for i in range(len(max_col_counts)):
        if max_col_counts[i] > (.4 * height):
            data[:,i] = 1
            
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))

    #test tesseract output
    text = pytesseract.image_to_string(im) 
    return(text)
    
image = byte_images[9]
threshold = 0.95
leeway = 5
window = 3

def SStesseract4(image, threshold = 0.95, leeway = 5, window = 3):
    #resize    
    swap = resize(image, 300, 60)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #scale image
    data = scale(data)
    #if color scheme is inverted, convert it back
    if np.mean(data) < 0.5:
        data = invert(data)
    #convert to 2-dimensions if it is a 3-dimensional image
    if len(data.shape) > 2:
        data = data[:,:,2]
    height, width = data.shape
    
    #iterate over the rows and get the max number of consecutive dark pixels
    row_counts= []
    max_row_counts = []
    for i in range(height):
        count = 0
        miss = 0
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
                    miss = 0
                    row_counts.append(count)
                elif (val >= threshold) & (miss < leeway):
                    count = count + 1
                    miss = miss + 1
                    row_counts.append(0)
                else:
                    count = 0
                    miss = miss + 1
                    row_counts.append(0)
    
    for i in range(len(max_row_counts)):
        if max_row_counts[i] > (.4 * height):
            data[:,i] = 1
    
    #iterate over the columns and get the max number of consecutive dark pixels
    col_counts= []
    max_col_counts = []
    for i in range(width):
        count = 0
        miss = 0
        for j in range(height):
            val = min(data[j,i:i+window])
            if (j + 1 == height):
                max_val = max(col_counts)
                col_counts = []
                max_col_counts.append(max_val)
            else:
                if (val < threshold):
                    count = count + 1
                    miss = 0
                    col_counts.append(count)
                elif (val >= threshold) & (miss < leeway):
                    count = count + 1
                    miss = miss + 1
                    col_counts.append(0)
                else:
                    count = 0
                    miss = miss + 1
                    col_counts.append(0)
            
    for i in range(len(max_col_counts)):
        if max_col_counts[i] > (.4 * height):
            data[:,i] = 1
    
    #try to clean up the data output for random pixels 
    #ROWS -- loop with 3 window, if only middle column has pixels, convert to 1
    for i in range(width-2):
        data_crop = data[:,i:i+3]
        col_1 = sum(data_crop[:,0] < 1)
        col_2 = sum(data_crop[:,1] < 1)
        col_3 = sum(data_crop[:,2] < 1)
        if (col_2 > 0) & (col_1 < 3) & (col_3 < 3):
            data[:,i+1] = 1
    
    #COLS -- loop with 3 window, if only middle column has pixels, convert to 1
    for i in range(height-2):
        data_crop = data[i:i+3]
        col_1 = sum(data_crop[0] < 1)
        col_2 = sum(data_crop[1] < 1)
        col_3 = sum(data_crop[2] < 1)
        if (col_2 > 0) & (col_1 < 2) & (col_3 < 2):
            data[i+1] = 1
                
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))
    
    #test tesseract output
    text = pytesseract.image_to_string(im).replace('\n','')
    if sum(c.isdigit() for c in text) < 9:
        text = SStesseract(image).replace('\n','')
        if sum(c.isdigit() for c in text) < 9:
            return(SStesseract2(image).replace('\n',''))
        else:
            return(text)
    elif sum(c.isdigit() for c in text) > 9:
        return(SStesseract2(image).replace('\n',''))
    else:
        return(text)
        
#Test SStesseract4
SStesseract4(byte_images[10])
    
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

text_output4 = []
for image in byte_images:
    text_output4.append(SStesseract4(image))