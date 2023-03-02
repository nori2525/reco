import os
import glob
from posixpath import basename
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#img_paths = []
#for file in glob.glob("./sys/try10/*"):
#    img_paths.append(file)

#for i in img_paths:
#    img = Image.open(i)


def img_array(img):
    img_ar = np.asarray(img)
    return img_ar

def flatten_img(img_ar):
    #s = img_ar.shape[0] * img_ar.shape[1] * img_ar.shape[2]
    img_width = img_ar.reshape(1, -1)
    return img_width

def get_center(img_path):
    img_paths = []
    for img in img_path:
        name = os.path.basename(img)
        img_name = 'C:/Users/norimasa/recom/web/mysite/reco/back/examples/mattes/' + name
        img_paths.append(img_name)

    dataset = []
    for i in img_paths:
        img = Image.open(i)
        img = img.resize((int(225),int(190)), Image.BICUBIC)
        img = img_array(img)
        img = flatten_img(img)
        dataset.append(img)

    dataset = np.array(dataset)
    dataset = dataset.reshape(len(dataset), -1).astype(np.float64)

    N_CLUSTER = 1
    cls = KMeans(n_clusters = N_CLUSTER).fit(dataset)

    center = cls.cluster_centers_
    return center

def get_single(target):
    name = os.path.basename(target)
    img_name = 'C:/Users/norimasa/recom/web/mysite/reco/back/examples/mattes/' + name
    img = Image.open(img_name)
    img = img.resize((int(225),int(190)), Image.BICUBIC)
    img = img_array(img)
    img = flatten_img(img)
    return img
    
#get_center(img_paths)