# -*- coding: utf-8 -*-
"""
This is a perceptron. 
"""
import numpy as np 
import matplotlib.pyplot as plt

weights = np.array([0,0])
#some data
#data_train = np.array([[ 5  ,1 ,-1  ,5 ,-5 ,-1  ,1, -5],
 #                      [ 5  ,1  ,5 ,-1 ,-5 ,-1 ,-5  ,1]])
#new data
data_train = np.array([[-2,2,1,-1,  -2,-1 ,1,2],
                       [2,2,1,1,  -2,-1,-1,-2]])
#some labels
data_label = np.array([1,1,1,1,-1,-1,-1,-1])
label=0 
for i in range(len(data_label)):
    value=np.dot(data_train[:,i],weights)
    if value < 0:
        label = -1 
    elif value > 0:
        label = 1
    if data_label[i] > label:
        weights=weights+data_train[:,i]
    elif data_label[i] < label:
        weights=weights-data_train[:,i]
     
plt.scatter(data_train[0][0:4],data_train[1][0:4],c='g') 
plt.scatter(data_train[0][4:],data_train[1][4:],c='r') 
"""
The weight matrix is perpendicular to the decision boundary. 
"""
plt.plot(np.linspace(-weights[1],weights[1],11),np.linspace(weights[0],-weights[0],11))
plt.grid()
