# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:58:45 2018

@author: Brandon Croarkin
"""

from keras.models import Sequential
from keras.layers import Activation, Dropout, Dense, Conv2D, Flatten, MaxPooling2D
from keras.callbacks import EarlyStopping, TensorBoard
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
import numpy as np
import PIL
import matplotlib.pyplot as plt
import os

#list which forms have the page number on their data page
four_box_forms = ['11-21-91(R)', '05/31/05', '07/17/17', '08/07/09',
                       '11/14/2016', '02/02/09', '03/08/13']

#list which forms do not have the page number on their data page
three_box_forms = ['05/07/87', '11-21-91(L)', '06/05/07']

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

#############DATA PREPROCESSING#########################

#resize them all to same dimensions
def resize(item):
    im = PIL.Image.open(path+"/"+item)
    im = im.resize((50,200), PIL.Image.ANTIALIAS)
    im.save(item)
   
#create function to convert all images to black and white JPG
def BW(image):
    im = PIL.Image.open(image)
    bw_im = im.convert('1') #converts to black and white
    bw_im.save(image) #saves as jpg
    
for item in images:
    resize(item)
    BW(item)
    
image_width = 50
image_height = 200

#make an array for the Neural Net
##should be a flattened array of pixel values

dataset = np.ndarray(shape = (len(images), image_width * image_height),
                     dtype = np.float32)

i = 0
for image in images:
    data = plt.imread(image)  # this is a PIL image
    x = data.reshape((10000))
    dataset[i] = x
    i += 1
    
#make an array for the CNN
##should be a 2-dimensional array of pixel values
channels = 3

cnn_dataset = np.ndarray(shape = (len(images), image_height, image_width, channels),
                     dtype = np.float32)

i = 0
for image in images:
    img = load_img(image)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    cnn_dataset[i] = x
    i += 1


#dataset = np.ndarray(shape=(len(images), channels, image_height, image_width),
#                     dtype=np.float32)

#i = 0
#for _file in images:
#    img = load_img(path + "/" + _file)  # this is a PIL image
#    img.thumbnail((image_width, image_height))
#    # Convert to Numpy Array
#    x = img_to_array(img)  
#    x = x.reshape((3, 40, 10))
#    # Normalize
#    x = x / 255.
#    dataset[i] = x
    
# Read the labels from the filenames
n_images = images.shape[0]
labels = np.zeros(n_images)
for i in range(n_images):
    box_no = images[i][0]
    if box_no != 'x':
        labels[i] = int(box_no[0])

#convert the labels to one-hot encoding
categories = np.array([1, 2, 3, 4, 0])
n_categories = 5
ohe_labels = np.zeros((len(labels), n_categories))

for i in range(len(labels)):
    j = np.where(categories == labels[i])
    ohe_labels[i,j] = 1

####Create Training and Test Split
    
#neural net
X_train, X_test, y_train, y_test = train_test_split(dataset, ohe_labels, test_size=0.2, random_state=33)
X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=33)

#cnn
X_train, X_test, y_train, y_test = train_test_split(cnn_dataset, ohe_labels, test_size=0.2, random_state=33)

######CREATE THE MODEL#####

#Neural Net Model
model = Sequential()
model.add(Dense(10, activation = 'relu', input_shape = (10000,)))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(5, activation = 'softmax'))
model.compile(optimizer = 'adam',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

model.summary()

model.fit(dataset, ohe_labels, validation_split = 0.1,
          epochs = 100)

#CNN Model
cnn_model = Sequential()
cnn_model.add(Conv2D(10, kernel_size = 3, activation = 'relu',
                     input_shape=(200,50,3), padding = 'same'))
cnn_model.add(Conv2D(10, kernel_size = 3, activation = 'relu',
                     padding = 'same'))
cnn_model.add(Flatten())
cnn_model.add(Dense(5, activation = 'softmax'))
cnn_model.compile(optimizer = 'adam',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

cnn_model.summary()

cnn_model.fit(X_train, y_train, validation_split = 0.1,
          epochs = 10)

cnn_model.evaluate(X_test, y_test)



