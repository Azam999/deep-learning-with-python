from keras.datasets import mnist
from keras import models
from keras import layers
from tensorflow.keras.utils import to_categorical
import matplotlib as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
# a layer is like a filter for data that extracts representations--data distillation
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax')) # returns an array of 10 probability scores

# loss function - measures performance
# optimizer - updates itself based on the loss function and data
# metrics - what to monitor
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])


# reshape data
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# categorical encoder
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)

print("Number of Weights:", len(network.layers[0].get_weights()[0])) # there are 784 weights for each image

# Show a digit
digit = train_images[4] # this is called tensor slicing
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

# Tensors
'''
3 Key attributes of a tensor
  1. Number of axes (rank) - ndim
  2. Shape - shape
  3. Data type - dtype

4 Common tensor shapes
  1. Vector data--2D tensors of shape (samples, features)
  2. Timeseries data or sequence data--3D tensors of shape (samples, timesteps, features)
  3. Images--4D tensors of shapes (samples, height, width, channels) or (samples, channels, height, width)
  4. Video--5d tensor of shape (samples, frames, height, width, channels) or (samples, frames, channels, height, width)
'''