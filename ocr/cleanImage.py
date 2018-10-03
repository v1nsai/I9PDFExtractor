# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:19:11 2018

@author: Brandon Croarkin
"""

import numpy as np
import pandas as pd
#import sys
import io
import PIL
import pytesseract
import os
import matplotlib.pyplot as plt
        
####make a function to display an image from its filename
def showImage(image):
    data = plt.imread(image)
    plt.imshow(data)
    
###make a function to put an array on a 0 to 1 scale
def scale(array):
    max = array.max()
    return(array/max)

def findFileName(file):
    """
    Removes all .* endings from a file to get just the filename
    """
    (name, ext) = os.path.splitext(file)
    return(name)
    
###resize images to same dimensions
def resize(image, width, height):
    im = image.resize((width,height), PIL.Image.ANTIALIAS)
    swap = io.BytesIO()
    im.save(swap, 'png')
    return swap

def removeBorderLines(data, threshold = 0.5, border = 5):
    data = scale(data)
    if len(data.shape) > 2:
        data = data[:,:,2]
    height, width = data.shape
    
    ###find filled lines
    border_columns = np.where(data.mean(axis=0)<threshold)[0]
    border_rows = np.where(data.mean(axis=1)<threshold)[0]
    
    ###create borders
    #right border
    if len(border_columns[border_columns > width - border]) == 0:
        right_border = width
    else:
        right_border = min(border_columns[border_columns > width - border]) 
    #left border
    if len(border_columns[border_columns < border - 5]) == 0:
        left_border = 0
    else:
        left_border = max(border_columns[border_columns < border]) + 1
    #top border
    if len(border_rows[border_rows < border]) == 0:
        top_border = 0
    else:
        top_border = max(border_rows[border_rows < border]) + 1
    #bottom border
    if len(border_rows[border_rows > height - border]) == 0:
        bottom_border = height
    else:
        bottom_border = min(border_rows[border_rows > height - border]) - 1
        
    #crop away lines
    data = data[top_border:bottom_border, left_border:right_border]

    return(data)

def removeRandomPixels(data):
    #scale data
    data = scale(data)
    #convert to 2D
    if len(data.shape) > 2:
        data = data[:,:,2]
    #get height and width
    height, width = data.shape
    
    #try to clean up the data output for random pixels on side of image
    pixel_cols = data.sum(axis = 0)
    side_pixel_count = 0
    gap = 0
    main_pixel_count = 0
    for i in range(width):
        if (side_pixel_count == 0) & (gap == 0):
            if pixel_cols[i] < height:
                side_pixel_count += 1 
            else:
                break
        elif (side_pixel_count > 0) & (gap == 0):
            if pixel_cols[i] < height:
                side_pixel_count += 1
            else:
                gap += 1
        elif (gap > 0) & (main_pixel_count == 0):
            if pixel_cols[i] == height:
                gap += 1
            else:
                main_pixel_count += 1
        elif (main_pixel_count > 0):
            if pixel_cols[i] < height:
                main_pixel_count += 1
            else:
                break

    if (side_pixel_count > 0) & (side_pixel_count < 10) & (gap > 5) & (main_pixel_count > 16):
        data[:,0:side_pixel_count] = 1
            
    #clean up any remaining random pixels (columns with a pixel with none in
    #columns next to it)
    for i in range(width-3):
        pixels = pixel_cols[i:i+3]
        pixel1 = pixels[0]
        pixel2 = pixels[1]
        pixel3 = pixels[2]
        if (pixel2 < height) & (pixel1 == height) & (pixel3 == height):
            data[:,i+1] = 1
        
    #try to clean up the data output for random pixels in top of image
    pixel_rows = data.sum(axis = 1)
    top_pixel_count = 0
    gap = 0
    main_pixel_count = 0
    for i in range(height):
        if (top_pixel_count == 0) & (gap == 0):
            if pixel_rows[i] < width:
                top_pixel_count += 1 
            else:
                break
        elif (top_pixel_count > 0) & (gap == 0):
            if pixel_rows[i] < width:
                top_pixel_count += 1
            else:
                gap += 1
        elif (gap > 0) & (main_pixel_count == 0):
            if pixel_rows[i] == width:
                gap += 1
            else:
                main_pixel_count += 1
        elif (main_pixel_count > 0):
            if pixel_rows[i] < width:
                main_pixel_count += 1
            else:
                break
    
    if (top_pixel_count > 0) & (top_pixel_count < 10) & (gap > 5) & (main_pixel_count > 16):
        data[0:top_pixel_count] = 1
    
    return(data)
        
def autoCropImage(data):
    '''
    @@data data array of image after the borders have been removed
    Takes in an image and crops parts of the image that do not include the main text
    '''  
    col_threshold = 0.1

    #remove a line that takes up whole column
    full_columns = np.where(data.mean(axis=0)<col_threshold)[0]
    data = np.delete(data, full_columns, axis = 1)
    
    row_threshold = 0.2
    #remove a line that takes up whole row
    full_rows = np.where(data.mean(axis=1)<row_threshold)[0]
    data = np.delete(data, full_rows, axis = 0)
    
    if np.mean(data) < .995:  
        ###Remove empty rows/columns
        non_empty_columns = np.where(data.min(axis=0)==0)[0]
        non_empty_rows = np.where(data.min(axis=1)==0)[0]
        try:
            cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
            image_data_new = data[cropBox[0]:cropBox[1]+5, cropBox[2]:cropBox[3]+5]
            return(image_data_new)
        except ValueError:
            return(data)      
    else:
        return(data)

def autoCropImage2(data):
    '''
    @@data data array of image after the borders have been removed
    Takes in an image and crops parts of the image that do not include the main text
    '''      
    threshold = 0.1
    
    #remove a line that takes up whole row
    full_rows = np.where(data.mean(axis=1)<threshold)[0]
    data = np.delete(data, full_rows, axis = 0)
    
    if np.mean(data) < .995:  
        ###Remove empty rows/columns
        non_empty_columns = np.where(data.min(axis=0)==0)[0]
        non_empty_rows = np.where(data.min(axis=1)==0)[0]
        try:
            cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
            image_data_new = data[cropBox[0]:cropBox[1]+5, cropBox[2]:cropBox[3]+5]
            return(image_data_new)
        except ValueError:
            return(data)      
    else:
        return(data)
        
##############################
##########TESTING#############
##############################

#make array of cropped images to clean
folder = 'C:\\Users\\Brandon Croarkin\\Documents\\GreenZone\\OCR\\NiFiTesting\\PythonPNGs\\CroppedImages\\CleanTest'
images = []
output = []
filenames = []
fields = []
os.chdir(folder)
for image in os.listdir(folder):
    if image.endswith(".png"):
        images.append(image)
        
for image in images:
    filename = findFileName(image)
    filenames.append(filename)
    field = str.split((str.split(image, sep = '_')[1]),sep = '.')[0]
    fields.append(field)
    data = plt.imread(image)
    data = removeBorderLines(data)
    data = removeRandomPixels(data)
    data = removeBorderLines(data)
    data = autoCropImage(data)
    data = removeRandomPixels(data)
    data = autoCropImage2(data)
    im = PIL.Image.fromarray(np.uint8(data*255))
    output.append(pytesseract.image_to_string(im))
    #im.save('Cleaned/' + filename + '.png')
    
df = pd.DataFrame({'file': filenames, 'text': output})
