
import os
import glob
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import center
from numpy.core.fromnumeric import reshape
from sklearn.cluster import KMeans

def get_center(paths):
    dataset = []
    for file in paths:
        b = np.load(file)
        dataset.append(b)

    dataset = np.array(dataset)
    center = np.mean(dataset, axis=0)
    return center

def get_single(img):
    a = np.load(img)
    return a.reshape(1, -1)