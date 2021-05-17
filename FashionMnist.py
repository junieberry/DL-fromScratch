#!/usr/bin/env python
# coding: utf-8


import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

import sys, os
sys.path.append("/home/junyoung44/dl/deep-learning-from-scratch/")
from common.layers import *
from collections import OrderedDict





## 28x28 image
## label : 0-9
## pixel : 0-255

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


print(train_images.shape) ## (60000, 28, 28)
print(len(train_labels)) ## 60000
print(test_images.shape) ## (10000, 28, 28)
print(len(test_labels)) ## 10000


plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images, test_images = train_images / 255.0, test_images / 255.0

num=10
print(test_labels)
test_labels=np.eye(num)[np.array(list(test_labels)).reshape(-1)]
train_labels=np.eye(num)[np.array(list(train_labels)).reshape(-1)]




class Model:
    def __init__(self):
        
        ## initialize weight&bias
        weight_init=0.01
        self.params={}
        self.params['W1']=weight_init*np.random.rand(784, 392)
        self.params['b1']=np.zeros(392)
        self.params['W2']=weight_init*np.random.rand(392, 100)
        self.params['b2']=np.zeros(100)
        self.params['W3']=weight_init*np.random.rand(100,10)
        self.params['b3']=np.zeros(10)
        
        ## initialize layers
        self.layers=OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine3'] = Affine(self.params['W3'], self.params['b3'])
        self.layers['Relu3'] = Relu()
        self.lastLayer = SoftmaxWithLoss()
        
    
    def predict(self, x):
        for layer in self.layers.values():
            x=layer.forward(x)
        return x
    
    def loss(self, x, t):
        y=self.predict(x)
        return self.lastLayer.forward(y,t)
    
    def accuracy(self,x,t):
        y=self.predict(x)
        y=np.argmax(y, axis=1)
        if t.ndim!=1:
            t=np.argmax(t, axis=1)
        accuracy=np.sum(y==t)/float(x.shape[0])
        
        return accuracy
        
        
    def gradient(self, x, t):
        #forward
        loss= self.loss(x,t)
        
        #backward
        dout=1
        dout=self.lastLayer.backward(dout)
        layers=list(self.layers.values())
        layers.reverse()
        
        for layer in layers:
            dout=layer.backward(dout)
        
        
        grads={}
        grads['W1'] = self.layers['Affine1'].dW # self.dW = np.dot(self.x.T, dout)
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db
        grads['W3'] = self.layers['Affine3'].dW
        grads['b3'] = self.layers['Affine3'].db
        
        return grads


iters=10000
train_size=train_images.shape[0]
batch_size=100
lr=0.01
iter_per_epoch = max(train_size / batch_size, 1)

train_loss_list = []
train_acc_list = []
test_acc_list = []



fashionmodel=Model()

for i in range(iters):
    batch_mask=np.random.choice(train_size, batch_size)
    x_batch=train_images[batch_mask]
    t_batch=train_labels[batch_mask]
    
    ## gradient
    grad_backprop=fashionmodel.gradient(x_batch, t_batch)
    
    ## gradient update
    for key in ('W1','b1','W2','b2','W3','b3'):
        fashionmodel.params[key]-=lr*grad_backprop[key]
    
    loss=fashionmodel.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    if i%(iter_per_epoch)==0:
        train_acc=fashionmodel.accuracy(train_images, train_labels)
        test_acc=fashionmodel.accuracy(test_images, test_labels)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        
        print('iters: {:4d}\tTrain acc: {:.5f}\tTest acc: {:.5f}\tLoss: {:f}'.format(i,train_acc,test_acc,loss))
    



print("Train acc : {:.5f}\tTest acc: {:.5f}".format(train_acc, test_acc))




