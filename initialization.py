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
num_of_environments = 500
g_sd = 9 #standard deviation of genetic component
g_mean= 33 #mean of genetic component
m_sd=15 #standard deviation of measured ability
m_mean=100 #mean of measured ability
learning_scale = 10 # scale for return to ability in sigmoid function
learning_multiplier = .5   #multplier for return to ability
genes =100 #length of the genome

#Definte Person Class
class Person:
    """
    Put in Class details
    """
    def __init__(self,parent1,parent2):
        self.genes=np.zeros(genes)
        self.temp=ss.normal.random() > 0
        self.genes=parent1.genes*self.temp+(1-self.temp)*parent2.genes
        self.age=0
        self.environment_history=[]
        self.parent1=parent1
        self.parent2=parent2
        
#Define Environment Class
class Environment:
    """
    put in Class details
    """
    def __init__(self,demand,utility_slope,income_slope,income_exp_multiplier,income_adjustment):
        self.demand=demand #optimal ability for the environment
        self.utility_slope=utility_slope #b in the utility function
        self.income_slope=income_slope #b in the income function
        self.income_exp_multiplier = income_exp_multiplier #a in the income function
        self.income_adjustment=income_adjustment #c in the income function

#Generate Environments

environments = []
demand_mean= 100 # Mean of the demand of the environments
demand_sd = 15 # standard deviation of the demand of the envrionments
utility_slope_min = 1 #minimum value of the utility slope distribution
utility_slope_max = 10 #maximum value of the utility slope distribution
income_slope_min = 1 #minimum value of the utility slope distribution
income_slope_max = 10 #maximum value of the utility slope distribution
income_exp_multiplier_min = 1 #minimum value of the utility slope distribution
income_exp_multiplier_max = 10 #maximum value of the utility slope distribution
income_adjustment_mean= 0 # Mean of the demand of the environments
income_adjustment_sd = 10 # standard deviation of the demand of the envrionments

for i in range(num_of_environments):
    environments.append(Environment(np.random.normal(demand_mean,demand_sd),np.random.uniform(utility_slope_min,utility_slope_max),np.random.uniform(income_slope_min,income_slope_max),np.random.uniform(income_exp_multiplier_min,income_exp_multiplier_max),np.random.normal(income_adjustment_mean,income_adjustment_sd)))