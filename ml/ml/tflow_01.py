#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow.compat.v1 as tf
import numpy as np

# z = w*x + b

g = tf.Graph()
with g.as_default():
    x = tf.placeholder( dtype = tf.float32, shape=(None,2), name='x' )
    w = tf.Variable( 2.0, name='weight' )
    b = tf.Variable( 0.7, name='bias' )
    z = w*x + b
    init = tf.global_variables_initializer()
    
with tf.Session(graph=g) as sess:
    sess.run(init)
    z = sess.run(z, feed_dict={x: np.array([[2.3, 3.1],[1,1],[6,7]])})
    print('>>', z)
