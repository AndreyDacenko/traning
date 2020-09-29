#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
    
    markers = ( 's', 'x', 'o', '^', 'v' )
    colors = ( 'red', 'blue', 'lightgreen', 'gray', 'cyan' )
    cmap = ListedColormap( colors[:len(np.unique(y))] )
    
    x1_min, x2_min = X.min(0) - 1
    x1_max, x2_max = X.max(0) + 1
    x1r = np.arange(x1_min, x1_max, resolution)
    x2r = np.arange(x2_min, x2_max, resolution)
    xx1, xx2 = np.meshgrid(x1r, x2r)
    ar = np.array([xx1.ravel(), xx2.ravel()]).T
    Z = classifier.predict(ar).reshape(xx1.shape)
    
    plt.contourf( xx1, xx2, Z, alpha=0.3, cmap=cmap )
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0], y=X[y==cl,1],
                    alpha=0.8, c=colors[idx], marker=markers[idx], label=cl, edgecolor='black')
