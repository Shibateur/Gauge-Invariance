# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:36:42 2020

@author: jmcos
"""
import numpy as np


def gaugeTransfo(g,c,a=np.array([])):
    c[0] = (c[0] + g)%3
    c[1] = (c[1] + g)%3
    if(len(a)==0):
        return(c)
    a[0] = (a[0] - g)%3
    a[1] = (a[1] - g -np.roll(g,1))%3
    return(c,a)