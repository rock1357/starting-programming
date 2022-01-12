#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 00:09:50 2022

@author: riccardosciarra
"""
import math
def area_circle(a): 
    area=math.pi*a*a
    return print("here is your area:", area)


#%%

def test_1():
    assert area_circle(1)==None
    
def test_2():
    assert area_circle(2)==1