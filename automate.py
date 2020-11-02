# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:34:08 2020

@author: jmcos
"""
import numpy as np


def trivialstep(c):
    c_roll_right = np.roll(c[0],1)
    c_roll_left = np.roll(c[1],-1)
    c_roll_right_2 = np.roll(c[1],1)
    c_roll_left_2 = np.roll(c[0],-1)
    res = [(c[0]+c_roll_right+c_roll_left_2)%2,(c[1]+c_roll_left+c_roll_right_2)%2]
    return res

def nextstep(c):
    c_roll_right = np.roll(c[0],1)
    c_roll_left = np.roll(c[1],-1)
    res = [(c_roll_right-c[1])%3, (c_roll_left+c[0])%3]
    return res

def nextstep_F(c,a):
    #print("ETAPE")
    c_roll_right = np.roll(c[0],1)
    c_roll_left = np.roll(c[1],-1)
    c_l_roll_left =np.roll(c[0],-1)
    a_l_roll_left = np.roll(a[0],-1)
    #a_r_roll_left = np.roll(a[1],-1)
    #print(c_roll_left)
    #print(c_roll_right)
    #print(c[1])
    #print(a[1])
    #print(c_l_roll_left)
    #print(a_l_roll_left)
    new_c = [(c_roll_right-c[1]+a[1])%3, (c_roll_left+c[0]+a_l_roll_left)%3]
    new_a = [(c_l_roll_left + a[0])%3 , (c[1] + a[0] + a[1])%3 ]
    return (new_c, new_a)