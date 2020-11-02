# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:28:52 2020

@author: jmcos
"""

import numpy as np

#FIRST ATTEMPT, VERY SUB-OPTIMAL
def fusion_h(c):
    L=[]
    vec_0_r = c[1]==0
    vec_0_l = c[0]==0
    vec_1_r = c[1]==1
    vec_1_l = c[0]==1
    vec_2_r = c[1]==2
    vec_2_l = c[0]==2
    for i in range((c[0].shape[0])//3):
        value_mx_l=0
        value_mx_r=0
        mx_l = np.sum(vec_0_l[i*3:i*3+3:1])
        mx_r = np.sum(vec_0_r[i*3:i*3+3:1])
        
        
        """
        nb_1_l = np.sum(vec_1_l[i:i+3:1])
        nb_1_r = np.sum(vec_1_r[i:i+3:1])
        nb_2_l = np.sum(vec_2_l[i:i+3:1]) 
        nb_2_r = np.sum(vec_2_r[i:i+3:1])
        if(nb_1_l>mx_l):
            mx_l=nb_1_l
            value_mx_l=1
        if(nb_2_l>mx_l):
            mx_l=nb_2_l
            value_mx_l=2
        if(nb_1_r>mx_r):
            mx_r=nb_1_r
            value_mx_r=1
        if(nb_2_r>mx_r):
            mx_r=nb_2_r
            value_mx_r=2
        """
        
        #SI ON CONSIDERE LES 1 COMME DES 2
        
        nb_1_l = np.sum(vec_1_l[i*3:i*3+3:1]) + np.sum(vec_2_l[i*3:i*3+3:1]) 
        nb_1_r = np.sum(vec_1_r[i*3:i*3+3:1]) + np.sum(vec_2_r[i*3:i*3+3:1])
        if(nb_1_l>mx_l):
            mx_l=nb_1_l
            value_mx_l=1
        if(nb_1_r>mx_r):
            mx_r=nb_1_r
            value_mx_r=1
        
        
        L.append(np.array([value_mx_l,value_mx_r]))
        
    return np.array(L)


"""
print("FUSION")
#FUSION
for i in range(fusion):
    print(l.shape)
    print(i)
    #FUSION HORIZONTALE
    fusion_h_l=[]
    for c in l:
        fusion_h_l.append(fusion_h(np.transpose(c)))
    
    #FUSION VERTICALE
    new_l=[]
    fusion_h_l = np.transpose(np.array(fusion_h_l),(1,0,2))
    for j in range(T//3):
        new_l.append(fusion_h(np.transpose(fusion_h_l[j])))
    l = np.transpose(np.array(new_l),(1,0,2))
    T=T//3
"""

#USING NUMPY FOR EFFICIENTY
def fusion(l):
    T=len(l)
    l=np.array(np.array(l)!=0,dtype='uint16')
    buffer = l+np.roll(l,1,axis=0)
    buffer = buffer + np.roll(l,-1,axis=0)
    
    l = buffer + np.roll(buffer,1,axis=1)
    l = l + np.roll(buffer,-1,axis=1)
    l= l>4
    l=l[1:T-1:3,1:T-1:3,:]
    return l