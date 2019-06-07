# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:23:27 2019

@author: jfal8
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

#Define Parameters
gen_size = 100 # size of each generation
environments = 500
g_sd = 9 #standard deviation of genetic component
g_mean= 33 #mean of genetic component
m_sd=15 #standard deviation of measured ability
m_mean=100 #mean of measured ability
learning_scale = 10 # scale for return to ability in sigmoid function
learning_multiplier = .5   #multplier for return to ability
genes =100 #length of the genome

#Definte Environment Class
def class Person:
    def __init__(self,parent1,parent2):
        self.genes=np.zeros(genes)
        self.temp=ss.normal.random() > 0
        self.genes=parent1.genes*self.temp+(1-self.temp)*parent2.genes
        self.age=0
        self.environment_history=[]
        self.parent1=parent1
        self.parent2=parent2


