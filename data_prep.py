#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:12:01 2019

@author: bajpaiarjun0333
"""

import os,shutil
#preparing the data for the generator object of the tensorflow
original_dataset_dir='/home/bajpaiarjun0333/Downloads/dogs-vs-cats/train'

#this is the folder where the data was uncompressed
base_dir='/home/bajpaiarjun0333/Artificial Intelligence/GitHub/Cats-Vs-Dogs/cats_and_dogs_small'
os.mkdir(base_dir)
#base directory created for the workflow

#formatting the data in a way tensorflow generator describes
train_dir=os.path.join(base_dir,'train')
os.mkdir(train_dir)
#train directory created the data for the training will be kept here

validation_dir=os.path.join(base_dir,'validation')
os.mkdir(validation_dir)
#directory created for loading the validation data

test_dir=os.path.join(base_dir,'test')
os.mkdir(test_dir)
#test directory created for loading the test images

#now creating the sub folders for holding the cat and the dogs data separetely
train_cats_dir=os.path.join(train_dir,'cats')
os.mkdir(train_cats_dir)
train_dogs_dir=os.path.join(train_dir,'dogs')
os.mkdir(train_dogs_dir)

validation_cats_dir=os.path.join(validation_dir,'cats')
os.mkdir(validation_cats_dir)
validation_dogs_dir=os.path.join(validation_dir,'dogs') 
os.mkdir(validation_dogs_dir)

test_cats_dir=os.path.join(test_dir,'cats')
os.mkdir(test_cats_dir)
test_dogs_dir=os.path.join(test_dir,'dogs')
os.mkdir(test_dogs_dir)

#actual copying the files to destination
fnames=['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(train_cats_dir,fname)
    shutil.copyfile(src,dst)

fnames=['cat.{}.jpg'.format(i) for i in range(1000,1500)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(validation_cats_dir,fname)
    shutil.copyfile(src,dst)

fnames=['cat.{}.jpg'.format(i) for i in range(1500,2000)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(test_cats_dir,fname)
    shutil.copyfile(src,dst)

#copying the dog images to their required folders
fnames=['dog.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(train_dogs_dir,fname)
    shutil.copyfile(src,dst)

fnames=['dog.{}.jpg'.format(i) for i in range(1000,1500)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(validation_dogs_dir,fname)
    shutil.copyfile(src,dst)

fnames=['dog.{}.jpg'.format(i) for i in range(1500,2000)]
for fname in fnames:
    src=os.path.join(original_dataset_dir,fname)
    dst=os.path.join(test_dogs_dir,fname)
    shutil.copyfile(src,dst)

#!!data prepration over for the tensorflow generators
    
