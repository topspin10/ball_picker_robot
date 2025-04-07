import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
# import keras
# from keras.models import Model
# from keras.layers import Conv2D, MaxPooling2D, Input, Conv2DTranspose, Concatenate, BatchNormalization, UpSampling2D
# from keras.layers import Dropout, Activation
# from keras.optimizers import Adam, SGD
# from keras.layers.advanced_activations import LeakyReLU
# from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
# from keras import backend as K
# from keras.utils import plot_model
# import tensorflow as tf
# import glob
# import random
import cv2 as cv
from random import shuffle


# this function provides examples for my model, so I can train it.
# my model needs examples to be able to replicate it when it is given new input.
def image_generator(files, batch_size=32, sz=(256, 256)):
    while True:

        # extract a random batch
        batch = np.random.choice(files, size=batch_size)

        # variables for collecting batches of inputs and outputs
        batch_x = []
        batch_y = []

        for f in batch:

            # get the masks. Note that masks are png files
            mask = Image.open(f'data/Masks/{f[:-4]}.png')
            mask = np.array(mask.resize(sz))

            # preprocess the mask
            # mask[mask >= 2] = 0
            # mask[mask != 0] = 1

            batch_y.append(mask)

            # preprocess the raw images
            raw = Image.open(f'data/Images/{f}')
            raw = raw.resize(sz)
            raw = np.array(raw)

            # check the number of channels because some of the images are RGBA or GRAY
            if len(raw.shape) == 2:
                raw = np.stack((raw,) * 3, axis=-1)

            else:
                raw = raw[:, :, 0:3]

            batch_x.append(raw)

        # preprocess a batch of images and masks
        # creates n
        batch_x = np.array(batch_x) / 255.
        batch_y = np.array(batch_y)
        batch_y = np.expand_dims(batch_y, 3)

        yield batch_x, batch_y


batch_size = 2

# TODO: change line below so that 'images' is data/Images #1
all_files = os.listdir('data/Images')
shuffle(all_files)
image = 'image'
cv.namedWindow(image)
mask = 'mask'
cv.namedWindow(mask)

split = int(0.95 * len(all_files))

# split into training and testing
train_files = all_files[0:split]
test_files = all_files[split:]

train_generator = image_generator(train_files, batch_size=batch_size)
test_generator = image_generator(test_files, batch_size=batch_size)
# batch_size = 32
#
# all_files = os.listdir('images')
# shuffle(all_files)
#
# split = int(0.95 * len(all_files))
#
# # split into training and testing
# train_files = all_files[0:split]
# test_files = all_files[split:]
#
# train_generator = image_generator(train_files, batch_size=batch_size)
# test_generator = image_generator(test_files, batch_size=batch_size)
x, y = next(train_generator)
plt.axis('off')
img = x[0]
msk = y[0].squeeze()
# msk = np.stack((msk,)*3, axis=-1)
# msk = msk.sum(axis=-1)

img = img[..., ::-1]
cv.imshow(image, img)
cv.imshow(mask, msk)
key = cv.waitKey(0)
# plt.imshow(np.concatenate([img, msk, img*msk], axis=1))
# TODO:
#  finish transporting code from
#  "https://colab.research.google.com/github/zaidalyafeai/Notebooks/blob/master/unet.ipynb#scrollTo=PvwbmS-YTHEZ"
#  get rid of the np.random.choice
