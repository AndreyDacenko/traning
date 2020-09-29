#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class Perceptron(object):
    
    def __init__(self, eta=0.01, n_iter=100, random_state=1):
        self.__eta = eta
        self.__n_iter = n_iter
        self.__random_state = random_state
        
    @property
    def eta(self):
        return self.__eta
    
    @property
    def n_iter(self):
        return self.__n_iter
    
    @property
    def random_state(self):
        return self.__random_state
    
    def fit(self, X, y):
        '''обучение'''
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=1.0, size=1+X.shape[1])
        self.errors_ = []
        
        for _ in range(0, self.n_iter):
            errors = 0
            for x_k, trg_k in zip(X, y):
                update = self.eta * ( trg_k - self.predict(x_k) )
                self.w_[1:] += update * x_k
                self.w_[0] += update
                if update != 0.0:  # жульничество!!!!
                    errors += 1
            self.errors_.append(errors)
            
        return self
        
    def net_input(self, X):
        '''чистый вход'''
        return np.dot(X, self.w_[1:]) + self.w_[0]
        
    def activate(self, z):
        '''функция активации (в персептроне не используется)'''
        return np.where( z>=0, 1, -1 )
        
    def threshold(self, phi):
        '''пороговая функция'''
        return np.where( phi>=0, 1, -1 )
        
    def predict(self, X):
        '''прогнозные метки'''
        return self.threshold( self.net_input(X) )
        