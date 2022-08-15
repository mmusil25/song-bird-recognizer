'''
Mark robert Musil
musilmark25@gmail.com
August 13 2022

inputs: path to a model.h5, path to a directory with camera inputs
outputs: Classification of bird species

'''

# Imports

from configparser import Interpolation
from queue import Full
import numpy as np, os, keras as keras, cv2
from keras.layers import Normalization
from keras.models import load_model
import tensorflow as tf

# Test variables

PATHTOMODEL = r'../premade.h5'
PATHTOSNAPSHOTS = r'../snapshot_input_dir/'
WAIT = True

class bird_finder:
    def __init__(self,path_to_model = PATHTOMODEL, path_to_snapshots = PATHTOSNAPSHOTS):
       
        self.bird_model = load_model(path_to_model)
        self.relative_imgNames = []; self.imgz = []; self.image_tensors = []
        return None

    def render_network(self):
        return self.bird_model

    def check_for_images(self):
        os.chdir(path_to_snapshots)
        full_dir = os.listdir()

        for fName in full_dir:
            if fName[-4:] == '.jpg':
                    self.relative_imgNames.append(fName)

                    _tmpimg = cv2.imread(fName)

                    self.imgz.append(_tmpimg)

                    inp = cv2.resize(_tmpimg, (112, 112))

                    rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)

                    tnsrRgb = tf.convert_to_tensor(rgb, dtype=tf.float32)

                    rgb_tensor = tf.expand_dims(rgb, 0)

                    self.image_tensors.append(rgb_tensor)

    def predict(self):
        answers = []
        for tnsr, img in zip(self.image_tensors, self.imgz):
            ans = np.argmax(self.bird_model(tnsr))
            answers.append(ans)
        return answers, self.imgz
        
        

if __name__ == '__main__':
    brdfndr = bird_finder(PATHTOMODEL, PATHTOSNAPSHOTS)
    brdfndr.predict()