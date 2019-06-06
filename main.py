#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:06:10 2019

@author: bajpaiarjun0333
"""
#import statements

from model_creation import *
#next line only once

#from data_prep import *
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(rescale=1./255)
test_datagen=ImageDataGenerator(rescale=1./255)

train_dir='/home/bajpaiarjun0333/Artificial Intelligence/GitHub/Cats-Vs-Dogs/cats_and_dogs_small/train'
validation_dir='/home/bajpaiarjun0333/Artificial Intelligence/GitHub/Cats-Vs-Dogs/cats_and_dogs_small/validation'
#creating the actual train and test generator along with the validation set
train_generator=train_datagen.flow_from_directory(train_dir,
                                                  target_size=(150,150),
                                                  batch_size=20,
                                                  class_mode='binary')

validation_generator=test_datagen.flow_from_directory(validation_dir,
                                                      target_size=(150,150),
                                                      batch_size=20,
                                                      class_mode='binary')
model=take_model()

history=model.fit_generator(train_generator,
                            steps_per_epoch=100,
                            epochs=30,
                            validation_data=validation_generator,
                            validation_steps=50)
