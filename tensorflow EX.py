import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Define the neural network model
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

# Compile the model with RMSprop optimizer and categorical crossentropy loss
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

# Train the model on the training data
history = model.fit(x_train, y_train,
                    batch_size=128,
                    epochs=20,
                    verbose=1,
                    validation_data=(x_test, y_test))

# Evaluate the model on the testing data
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

#This code loads the MNIST dataset from TensorFlow, preprocesses the data by
# reshaping and normalizing it, defines a neural network model 
# with two dense layers and a dropout layer, compiles the model with
#RMSprop optimizer and categorical crossentropy loss, trains the
#model on the training data, evaluates the model on the testing data,
#  and prints the test loss and accuracy.
#You can modify this code to use other datasets,
#  neural network architectures, optimizers, loss functions, and 
#training parameters depending on your task and data. TensorFlow
#  provides many other tools and functionalities for deep learning
#and machine learning.