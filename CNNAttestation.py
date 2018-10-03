# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:03:13 2018

@author: Brandon Croarkin
"""

from keras.models import Sequential
from keras.layers import Activation, Dropout, Dense, Conv2D, Flatten, MaxPooling2D
from keras.callbacks import EarlyStopping, TensorBoard
from sklearn.metrics import accuracy_score, f1_score
import os
import numpy as np
from scipy import misc
import PIL
import matplotlib.pyplot as plt
from datetime import datetime

#list which forms have the page number on their data page
four_box_forms = ['11-21-91(R)', '05/31/05', '07/17/17', '08/07/09',
                       '11/14/2016', '02/02/09', '03/08/13']

#list which forms do not have the page number on their data page
three_box_forms = ['05/07/87', '11-21-91(L)', '06/05/07']

####Resize all images in folder
def resize():
    for item in images:
        im = PIL.Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((50,200), PIL.Image.ANTIALIAS)
        imResize.save(f + '_resized.png', 'PNG', quality=90)
        os.remove(item)
   
resize()
     
####Make a function to rename files to include what Box # it has
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

####Make a function to copy all those files to a new folder

####Retrieve filenames of all images in image_path
path = 'C:/Users/Brandon Croarkin/Documents/GreenZone/OCR/NiFiTesting/PythonPNGs/CroppedImages/attestation/4 boxes/All'
os.chdir(path)
dirs = os.listdir(path)
images = []
for item in dirs:
    if item.endswith(".png") and os.path.isfile(path+ '/' +item):
        images.append(item)
images = np.asarray(images)

# Get image size
image_size = (50, 200)

# Read the labels from the filenames
n_images = images.shape[0]
labels = np.zeros(n_images)
for i in range(n_images):
    box_no = images[i][0]
    if box_no != 'x':
        labels[i] = int(box_no[0])
        
##########CREATE THE MODEL###################
        
####Create Training and Test Split
TRAIN_TEST_SPLIT = 0.8

# Split at the given index
split_index = int(TRAIN_TEST_SPLIT * n_images)
shuffled_indices = np.random.permutation(n_images)
train_indices = shuffled_indices[0:split_index]
test_indices = shuffled_indices[split_index:]

# Split the images and the labels
x_train = images[train_indices]
y_train = labels[train_indices]
x_test = images[test_indices]
y_test = labels[test_indices]

# Hyperparameter
N_Layers = 4

# Build model
def cnn(size, n_layers):
    # INPUTS
    # size     - size of the input images
    # n_layers - number of layers
    # OUTPUTS
    # model    - compiled CNN

    # Define hyperparamters
    MIN_NEURONS = 20
    MAX_NEURONS = 120
    KERNEL = (3, 3)

    # Determine the # of neurons in each convolutional layer
    steps = np.floor(MAX_NEURONS / (n_layers + 1))
    nuerons = np.arange(MIN_NEURONS, MAX_NEURONS, steps)
    nuerons = nuerons.astype(np.int32)

    # Define a model
    model = Sequential()

    # Add convolutional layers
    for i in range(0, n_layers):
        if i == 0:
            shape = (size[0], size[1], size[2])
            model.add(Conv2D(nuerons[i], KERNEL, input_shape=shape))
        else:
            model.add(Conv2D(nuerons[i], KERNEL))

        model.add(Activation('relu'))

    # Add max pooling layer
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(MAX_NEURONS))
    model.add(Activation('relu'))

    # Add output layer
    model.add(Dense(5))
    model.add(Activation('sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Print a summary of the model
    model.summary()

    return model

# Instantiate the model
model = cnn(size=image_size, n_layers=N_Layers)

# Training hyperparamters
EPOCHS = 50
BATCH_SIZE = 20

# Early stopping callback
PATIENCE = 10
early_stopping = EarlyStopping(monitor='loss', min_delta=0, patience=PATIENCE, verbose=0, mode='auto')

# TensorBoard callback
LOG_DIRECTORY_ROOT = ''
now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
log_dir = "{}/run-{}/".format(LOG_DIRECTORY_ROOT, now)
tensorboard = TensorBoard(log_dir=log_dir, write_graph=True, write_images=True)

# Place the callbacks in a list
callbacks = [early_stopping, tensorboard]

# Train the model
model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, callbacks=callbacks, verbose=0)






