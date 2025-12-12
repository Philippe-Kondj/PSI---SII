# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 12:55:03 2025

@author: PKONDJOYAN1
"""
import numpy as np

N = 90
nb = 9000
theta = np.linspace(1,N,nb)
print(theta)
theta_rad = [j*np.pi/180 for j in theta]

resultat = [(np.sin(i)-i)/i for i in theta_rad] # calcul des valeurs de l'opération (en rad)

for k in range (len(resultat)):
    if abs(resultat[k]) > 0.01:
        print("theta = " , theta[k])
        break