#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:16:40 2019

@author: flatironschool
"""

import numpy as np

class Calculator:
    
    def __init__(self, data):
        assert all(isinstance(x, (int, float)) for x in data), "list can only be numbers"
        self.data = data
        self.update_data() 

        
    def update_data(self): 
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_var()
        self.standev = self.__calc_std()
        
        
    def __repr__(self):
        return self
       
    def __calc_mean(self):
        mean = sum(self.data)/len(self.data)
        return mean

    def __calc_median(self):
        sorted_data = sorted(self.data)
        length = int(len(sorted_data))
        half_length = int(len(sorted_data)*0.5) 
        integer = int((half_length)+0.5)
        if length % 2 == 0:
            median = (sorted_data[half_length]+sorted_data[half_length-1])/2
        else:
            median = sorted_data[integer]
        return median
    
    def __calc_var(self):
        variance = np.var(self.data)
        return variance

    def __calc_std(self):
        std = np.std(self.data)
        return std

    def add_data(self, new_data):
        self.data.extend(new_data)
        #Now that data has changed- need to update the statstics using the libe below
        self.update_data()
        
    def remove_data(self, old_data):
        self.data.remove(old_data)
        self.update_data()