#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:33:11 2018

@author: karlithoss
"""


import numpy as np
import scipy.io as sio
from matplotlib import pyplot as plt

def perceptron_simple(x,w,active):
    y = 0
    for i in range(0, len(x)):
        y = y + (np.dot(x[i],w[i+1]))
    y = y + w[1]
    y = activation(active,y)
    return y


def activation(act,x):
    if(act==0):
        return np.sign(x)
    elif (act==1):
        return np.tanh(x)
    else:
        return (1/(1+np.exp(-x)))
    
def affiche(x,y):
    plt.plot(x,y,'ro')
    plt.show()
    
def apprentissage_simple(x,yd):
    
    
    
if __name__ == "__main__":
    w = [-0.5,1,1]
    x1 = [0,0]
    x2 = [0,1]
    x3 = [1,0]
    x4 = [1,1]
    y = []
    y1 = perceptron_simple(x1,w,0)
    affiche(x1[0],x1[1])
    y2 = perceptron_simple(x2,w,0)
    affiche(x2[0],x2[1])
    y3 = perceptron_simple(x3,w,0)
    affiche(x3[0],x3[1])
    y4 = perceptron_simple(x4,w,0)
    affiche(x4[0],x4[1])
#    for i in range(1,5):
#        y = perceptron_simple(x+i,w,0)
#        affiche(x+i,y)
        