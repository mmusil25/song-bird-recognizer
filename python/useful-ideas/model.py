from configparser import Interpolation
import numpy as np, os
import keras as keras
from keras.layers import Normalization
from keras import layers
from keras.models import load_model
import numpy as np


testPath = None

premade_H5 = None


# Machine learning specific constants

BATCHSIZE = 2
IMAGE_SIZE = (200,200)
CROP_WIDTH = 25
CROP_HEIGHT = 25
FILTERS = 2
KERNEL_SIZE = (3,3)
ACTIVATION = 'RELU'
POOL_SIZE = (3,3)



class bird_Model:
    def __init__(path = None):
        #if path:
            #dataset = keras.preprocessing.image_dataset_from_directory(
            #    testPath, batch_size = BATCHSIZE, image_size = IMAGE_SIZE)

            #for data, labels in dataset:
            #    print(data.shape)
            #    print(data.dtype)
            #    print(labels.shape)
             #   print(labels.dtype)
        return
    def load_pretrained(path=None):
        self.premade = load_model(None)
        print(premade.summary())

    def demo(self):
        random_data = np.random.ranint(0, 256, size=(64,200,200,3)).astype("float32")
        prcdt = self.model(random_data)
        print(prcdt.shape)
        print(prcdt)
        
    def build_model(self, premade=True):
        inputs = keras.Input(shape=(None,None,3))

        if premade:

            resize_to_premade = keras.layers.Resizing(112,112, Interpolation="bilinear", crop_to_aspect_ratio=False)(inputs)
            premade_interface = self.premade()





        if not premade:
            
            x = CenterCrop(height = CROP_HEIGHT, width = CROP_WIDTH)(inputs)
            x = layers.Conv2D(filters=FILTERS, kernel_size = KERNEL_SIZE, activatiom = ACTIVATION)(x)
            x = layers.MaxPooling(pool_size = POOL_SIZE)(x)
            x = layers.GlobalAveragePooling2D(x)
            num_classes = 100
            outputs = layers.Dense(num_classes, activation = 'softmax')(x)

        self.model = keras.Model(inputs=inputs, outputs=outputs)

if __name__ == '__main__':

    trnr = bird_Model()
    trnr.load_pretrained()
    