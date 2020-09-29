#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
from scipy.special import expit


class MLP(object):
    
    def __init__(self, n_features, n_output, n_hidden=30,
                 epochs=500, eta=0.001, shuffle=True, random_state=None,
                 minibatches=1):
        np.random.seed(random_state)
        self.n_features = n_features
        self.n_output = n_output
        self.n_hidden = n_hidden
        self.epochs = epochs
        self.eta = eta
        self.shuffle = shuffle
        self.minibatches = minibatches
        self.w1, self.w2 = self._initialize_weights()
        
    def _encode_labels(self, y, k):
        '''one-hot'''
        onehot = np.zeros((k, y.shape[0]))
        for idx, val in enumerate(y):
            onehot[val, idx] = 1.0
        return onehot

    def _sigmoid(self, z):
        return expit(z)
    
    def _sigmoid_gradient(self, z):
        s = self._sigmoid(z)
        return s * ( 1 - s )
    
    def _initialize_weights(self):
        w1 = np.random.uniform(-1.0, 1.0, size = self.n_hidden*(self.n_features+1) )
        w1 = w1.reshape(self.n_hidden, self.n_features+1)
        w2 = np.random.uniform(-1.0, 1.0, size = self.n_output*(self.n_hidden+1) )
        w2 = w2.reshape(self.n_output, self.n_hidden+1)
        print( '>', w1.shape, w2.shape )
        return w1, w2
    
    def _add_bias_unit(self, X, *, column=True):
        if column:
            X_new = np.ones(( X.shape[0], X.shape[1]+1 ))
            X_new[:,1:] = X
        else:
            X_new = np.ones(( X.shape[0]+1, X.shape[1] ))
            X_new[1:,:] = X
        return X_new
            
    def _feedforward(self, X, w1, w2):
        a1 = self._add_bias_unit(X, column=True)
        z2 = w1.dot(a1.T)
        a2 = self._sigmoid(z2)
        a2 = self._add_bias_unit(a2, column=False)
        z3 = w2.dot(a2)
        a3 = self._sigmoid(z3)
        return a1, z2, a2, z3, a3
        
    def _get_cost(self, y_enc, output, w1, w2):
        term1 = - y_enc * np.log(output)
        term2 = (1-y_enc) * np.log(1.0-output)
        cost = np.sum(term1 - term2)
        return cost
        
    def _get_gradient(self, a1, a2, a3, z2, y_enc, w1, w2):
        sigma3 = a3 - y_enc
        z2 = self._add_bias_unit(z2, column=False)
        sigma2 = w2.T.dot(sigma3) * self._sigmoid_gradient(z2)
        grad1 = sigma2.dot(a1)
        grad2 = sigma3.dot(a2.T)
        # print('>>', grad1[1:,:].shape, grad2.shape)
        return grad1[1:,:], grad2
    
    def predict(self, X):
        a1, z2, a2, z3, a3 = self._feedforward(X, self.w1, self.w2)
        y_pred = np.argmax(z3, axis=0)
        return y_pred
    
    def fit(self, X, y):
        self.cost_ = []
        X_data, y_data = X.copy(), y.copy()
        y_enc = self._encode_labels(y, self.n_output)
        
        delta_w1_prev = np.zeros(self.w1.shape)
        delta_w2_prev = np.zeros(self.w2.shape)
        
        for i in range(self.epochs):
            
            print(i)
            
            if self.shuffle:
                idx = np.random.permutation(y_data.shape[0])
                X_data = X_data[idx]
                y_enc = y_enc[:,idx]
                
            mini = np.array_split(range(0,y_data.shape[0]), self.minibatches)
            for idx in mini:
                a1, z2, a2, z3, a3 = self._feedforward(X_data[idx], self.w1, self.w2)
                
                cost = self._get_cost(
                    y_enc = y_enc[:,idx],
                    output = a3,
                    w1 = self.w1,
                    w2 = self.w2 )
                self.cost_.append(cost)
                
                grad1, grad2 = self._get_gradient(a1=a1, a2=a2, a3=a3, z2=z2,
                    y_enc=y_enc[:,idx],
                    w1=self.w1,
                    w2=self.w2 )
                    
                delta_w1 = self.eta * grad1
                delta_w2 = self.eta * grad2

                # print(self.w1.shape, delta_w1.shape, delta_w1_prev.shape)
                
                self.w1 -= ( delta_w1 + 0.0*delta_w1_prev )
                self.w2 -= ( delta_w2 + 0.0*delta_w2_prev )
                delta_w1_prev = delta_w1
                delta_w2_prev = delta_w2
                
        return self   
                    
            