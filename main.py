# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:40:09 2020

@author: jmcos
"""
import numpy as np
from graph import*
from matplotlib import*
from fusion import*
from gauge_transfo import*
from automate import*



##########CHOIX DE LA TAILLE#########
    


T=9000 #Nombre de step
nb_fusion=4 #Nombre de fusions à faire (matplotlib se met à ramer à partir de T=250 sans fusion)
#Chaque fusion "divise T par 3" au moment de l'affichage




########INITIALISATION##########
    

#On garantit la divisibilité en cas de fusion
if (nb_fusion>0):
    T = T - (T%(pow(3,nb_fusion)))


#Puis on choisit la configuration de base et la transformation à appliquer
#Les configuration étant stockées dans un vecteur qui contient:
# -la partie gauche de toutes les cellules en 0
# -la partie droite de toutes les cellules en 1

c0 = np.array([np.zeros(int(T*2.5)),np.zeros(int(T*2.5))])
a0 = np.array([np.zeros(int(T*2.5)),np.zeros(int(T*2.5))])
g = np.zeros(int(T*2.5))


c0[0][int(T*1.25)]=1   #int(T*25) correspond à la cellule au milieu du vecteur
c0[1][int(T*1.25)]=1

"""
VERIFICATION DU CALCUL DANS L'ARTICLE:
g[int(T*1.25)]=2
g[int(T*1.25-1)]=1
c0[1][int(T*1.25+1)]=1
c0[1][int(T*1.25+1)]=1
c0[0][int(T*1.25-1)]=1
a0[1][int(T*1.25)]=2
a0[0][int(T*1.25)]=2
a0[1][int(T*1.25+1)]=1
"""


#On applique la transformation de jauge

c,a=gaugeTransfo(g, c0,a=a0)








#############CALCUL############
print("CALCUL")



l=[]
for i in range(T):
    l.append(np.roll(np.transpose(c),-int(T*1.25+T/2-T/4))[:T])
    c,a=nextstep_F(c,a)
    #c=nextstep(c)
    #c = trivialstep(c)





###########FUSION###########
print("FUSION")


for i in range(nb_fusion):
    l=fusion(l)



##########AFFICHAGE########
print("AFFICHAGE")        

 
afficher_liste_config(l,daltonisme=True)
