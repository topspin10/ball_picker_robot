import numpy as np
# import matplotlib.pyplot as plt
# import os
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
# import cv2
# from random import shuffle


def image_generator(files, batch_size=32, sz=(256, 256)):
    while True:

        # extract a random batch
        batch = np.random.choice(files, size=batch_size)

        # variables for collecting batches of inputs and outputs
        batch_x = []
        batch_y = []

        for f in batch:

            # get the masks. Note that masks are png files
            mask = Image.open(f'annotations/trimaps/{f[:-4]}.png')
            mask = np.array(mask.resize(sz))

            # preprocess the mask
            mask[mask >= 2] = 0
            mask[mask != 0] = 1

            batch_y.append(mask)

            # preprocess the raw images
            raw = Image.open(f'images/{f}')
            raw = raw.resize(sz)
            raw = np.array(raw)

            # check the number of channels because some of the images are RGBA or GRAY
            if len(raw.shape) == 2:
                raw = np.stack((raw,) * 3, axis=-1)

            else:
                raw = raw[:, :, 0:3]

            batch_x.append(raw)

        # preprocess a batch of images and masks
        batch_x = np.array(batch_x) / 255.
        batch_y = np.array(batch_y)
        batch_y = np.expand_dims(batch_y, 3)

        yield (batch_x, batch_y)
# TODO:
#  finish transporting code from
#  "https://colab.research.google.com/github/zaidalyafeai/Notebooks/blob/master/unet.ipynb#scrollTo=PvwbmS-YTHEZ"
