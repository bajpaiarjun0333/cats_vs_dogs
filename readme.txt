This Project uses the technique of convolutional nueral network for classifying the images into two categoies namely cat and dog.
The model is built using Tensorflow and Keras and one saved trained instance of the model is saved with name cats_vs_dogs.h5, load 
the model and directly test it on any given images and save the recourses and time required for training the model.
The project can be used as a subsystem of bigger projects as a classifier.

The model may overfit as it is trained on smaller dataset and regularization is not used but in the file model_creation.py, the augmented
model function returns the model which is supposed to crub the overfitting of the problem and make it more efficient.

The Validation accuracy achived was 85.71 without regularization.

