# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:24:09 2020

@author: DALab
"""
import numpy as np

from copy import copy, deepcopy
from abc import ABC



class Particle():
    #利用Particle初始化產生初始解，初始解的更改從這裡調整
    def __init__(self, values, fitness):
        self.values = values
        self.F = fitness
    def set_F(self,F):
        self.F = F
        
    def append(self, value):
        self.values.append(value)
    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value
        
    def __iter__(self):
        return iter(self.values)

    def getFit(self):
        return self.F
    
    def __str__(self):
        return str(self.values)
    def __repr__(self):
        return str(self)


    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
