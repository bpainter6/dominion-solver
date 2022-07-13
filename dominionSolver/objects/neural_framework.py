# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:52:13 2022

@author: 17066
"""

import numpy as np

def activation(dataIn,actFunc,**actParams):
    """activates an array of data by applying a nonlinear function
    
    parameters
    ----------
    dataIn - ndarray
        numpy array containing a linearly transformed input
    actFunc - str
        string describing the activation function to be applied
    actParams - dict/kwargs
        kwargs detailing how the activation function should be applied
    
    """
    
    if actFunc == "linear":
        return dataIn 
    elif actFunc == "relu":
        return np.max(0,dataIn)
    elif actFunc == "sigmoid":
        return 1/(1+np.exp(-dataIn))
    elif actFunc == "softmax":
        return np.exp(dataIn)/np.sum(np.exp(dataIn))

def dActivation(dataIn,actFunc,**actParams):
    """Calculates the derivative of the activation function for an array of 
    data
    
    parameters
    ----------
    dataIn - ndarray
        numpy array containing a linearly transformed input
    actFunc - str
        string describing the activation function to be applied
    actParams - dict/kwargs
        kwargs detailing how the activation function should be applied
    
    """
    
    if actFunc == "linear":
        return 1
    elif actFunc == "relu":
        return 1*(dataIn>0)
    elif actFunc == "sigmoid":
        sig = 1/(1+np.exp(-dataIn))
        return sig*(1-sig)
    elif actFunc == "softmax":
        return np.exp(dataIn)/np.sum(np.exp(dataIn))

def cost(dataOut,dataExp,costFunc):
    """Applies the cost function to the data"""
    if costFunc == "mse":
        return (dataOut-dataExp)**2
    elif costFunc == "err":
        return (dataOut-dataExp)

def dCost(dataOut,dataExp,costFunc):
    """returns the derivative of the cost function for the data"""
    if costFunc == "mse":
        return dataOut
    elif costFunc == "err":
        return 1

class neural_network():
    """Object storing a neural network 
    """
    
    def __init__(self,nIn,layerSizes,actFuncs,actParams):
        """ Initializes the neural network
        
        parameters
        ----------
        nIn - integer
            number of inputs to the network
        layerSizes - list of integers
            list describing the number of neurons in the nth hidden layer
        actFuncs - list of str
            list describing the activation fuction used in the nth layer
        actParams - list of dict/kwargs
            list describing the activation function parameters in the nth layer
        
        """
        
        # Initialize all the layers in the network
        self.layers = []
        for ndx,layerSize in enumerate(layerSizes):
            # determine the number of inputs to the layer
            if ndx == 0:
                nInputs = nIn
            else:
                nInputs = layerSize[ndx-1]
            
            # initialize and store the layer
            layer = neural_layer(nInputs,layerSize,
                                 actFuncs[ndx],actParams[ndx])
            self.layers.append(layer)
        
    def forward(self,dataIn,testing=True):
        """Calculates an output using the network's current set of weights 
        and biases
        
        parameters
        ----------
        dataIn - ndArray
            an array of data to be propogated through the network
        testing - bool
            determines whether propogated data should be saved to be later 
            back propogated
        
        """
        
        # forward propagate through each layer
        for layer in self.layers:
            dataIn = layer.forward(dataIn,testing)
        
        return dataIn
    
    def backward(self,learningRate,dataExp,costFunc="mse"):
        """backpropagates the weights and baises based on an array of target 
        values"""
        
        # propgate through each layer in reverse
        layersRev = self.layers.reverse()
        
        for ndx,layer in enumerate(layersRev[:-1]):
            # calculate/update the gradient function
            if ndx == 0:
                dataOut = layer.activated
                grad    = cost(dataOut,dataExp,costFunc)
            else:
                weights     = layersRev[ndx-1]
                transformed = layer.transformed
                actFunc     = layer.actFunc
                actParams   = layer.actParams
                grad = weights.T.dot(grad)*dActivation(transformed,actFunc,
                                                       **actParams)
            
            # extract the output from the input layer
            dataIn = layersRev[ndx+1].activated
            
            # back propogate through the layer
            layer.backward(learningRate,grad,dataIn)
            
        # cleanup and finalize propogation
        
class neural_layer():
    """Object storing a neural layer in a neural network
    """
    
    def __init__(self,nInputs,layerSize,actFunc,actParam):
        """Initializes the neural layer
        
        parameters
        ----------
        nInputs - integer
            number of inputs to the neuron layer
        layerSize - integer
            number of neurons in the layer
        actFunc - str
            activation function to be used in the layer
        actParams - dict
            dictionary of the addi
        
        """
        
        # Initial guess for weights and biases
        self.weights  = np.random.rand(layerSize,nInputs) - 0.5
        self.biases   = np.random.rand(layerSize,1) - 0.5
        
        # Other params
        self.actFunc  = actFunc
        self.actParam = actParam
        
        # no tests yet recorded in the initialized layer
        self.nTests = 0
    
    def forward(self,dataIn,testing):
        """forward propagates ``dataIn`` through the layer and stores the 
        transformed and activated data"""
        
        # update number of stored tests
        self.nTests += np.size(dataIn)[1]
        
        # linearly transform dataIn
        dataTransformed = self.weights.dot(dataIn)+self.biases
        
        # activate dataIn
        dataActivated = activation(dataTransformed, 
                                   self.actFunc,**self.actParams)  
        
        # store results if testing data
        if testing:
            try:
                self.transformed = np.hstack((self.transformed,
                                              dataTransformed))
                self.activated = np.hstack((self.activated,
                                            dataActivated))
            except:
                self.transformed = dataTransformed
                self.activated = dataActivated
        
        return  dataActivated
    
    def backward(self,learningRate,grad,dataIn):
        """back propogates ``expVals`` through the layer"""
        
        # calculate weight change
        dWeights = grad.dot(dataIn.T)/self.nTests
        
        # calculate biases change
        dBiases = np.sum(grad,2)/self.nTests
        
        # Update the layer
        self.weights = self.weights + learningRate*dWeights
        self.biases  = self.biases  + learningRate*dBiases
        self.transformed = None
        self.activated   = None