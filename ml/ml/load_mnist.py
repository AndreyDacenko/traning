#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import numpy as np
import struct


MNIST_PATH = Path.cwd() / 'data'

def load_mnist(kind='train'):
    labels_path = MNIST_PATH / f'{kind}-labels-idx1-ubyte'
    images_path = MNIST_PATH / f'{kind}-images-idx3-ubyte'
    
    with labels_path.open('rb') as lbl:
        magic, n = struct.unpack('>II', lbl.read(8))
        labels = np.fromfile(lbl,dtype=np.uint8)
        
    with images_path.open('rb') as img:
        magic, num, rows, cols = struct.unpack('>IIII', img.read(16))
        images = np.fromfile(img, dtype=np.uint8)
        images = images.reshape(len(labels), 784)

    return images, labels