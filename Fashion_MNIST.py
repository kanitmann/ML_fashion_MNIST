# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lw77GYRqmfz473imgNagW5CVN37FmXGK
"""

#Code by Kanit Mann

#Import necessary packages
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Load Dataset__Train-test Split
(x_train,y_train),(x_test,y_test) = keras.datasets.fashion_mnist.load_data()
class_name = ['T-shirt', 'Trousers', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']

#Show the training set

plt.imshow(x_train[5], cmap=plt.cm.binary)
plt.xlabel(class_name[y_train[5]])
plt.show()

#Image Preprocessing
x_train = x_train.reshape(x_train.shape[0], 28,28,1)
x_test = x_test.reshape(x_test.shape[0], 28,28,1)

#Create Neural Network
classifier = Sequential()
classifier.add(Convolution2D(32, (3,3), activation = 'relu', input_shape = (28,28,1)))
classifier.add(MaxPooling2D(2,2))
classifier.add(Flatten())


classifier.add(Dense(128, activation ='relu'))
classifier.add(Dense(10, activation = 'softmax'))
classifier.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics =['accuracy'])


classifier.fit(x_train,y_train, epochs = 10)
loss, accuracy = classifier.evaluate(x_test,y_test, verbose = 2)
print(accuracy)

