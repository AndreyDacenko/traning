import numpy
import cv2
from keras.models import load_model
import argparse
import pickle


mapimg = imread("map.jpg")
image = imread("MEDIUM1")


maxWidth = mapimg.shape[1]
maxHeight = mapimg.shape[0]


i = 0
j = 0

def crop(x,y):
    crop_image = mapimg[y:13 + y, x:13 + x]



for j in range(maxHeight - 13):
    x = 0
    for i in range(maxWidth - 13):
        crop(x,y)
        x += 10
    y += 10