# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 13:19:04 2025

@author: PKONDJOYAN1
"""

# 1 - Dichotomie

import matplotlib.pyplot as plt

def dichotomie(f, a, b, epsilon):
    iteration = 0
    m = (a+b)/2
    while abs(a-b) > epsilon:
        iteration += 1
        if f(m) == 0:
            return m
        elif f(a)*f(m) > 0:
            a = m
        else:
            b = m
        m = (a+b)/2
    return m, iteration

def f(x):
    return 5*x**2+2*x-34

X = []
Y = []
for i in range(-4, 5, 1):
    Y.append(f(i))
    X.append(i)


plt.clf()
plt.figure('Représentation de f(x)')
plt.plot(X,Y)
plt.show()

print(dichotomie(f, -3, -2, 0.01))

print(dichotomie(f, 2, 3, 0.01))

# 2 - Méthode de Newton

def derivf(x):
    return 10*x + 2

def newton(a, e):
    delta = 1
    iteration = 0
    while delta > e:
        iteration += 1
        x = -f(a)/derivf(a) + a
        delta = abs(x - a)
        a = x
    return a, iteration

print(newton(-3, 0.01))
print(newton(2, 0.01))

# 3 - Méthode d'Euler

def fy(t, y):
    return 1200 - 1000*y

T = 0.1
N = 100
pas = 0.01
listeT = [0.0 + i*pas for i in range(N+1)]

def Euler(fy, y0, listeT) :
    listeY = [y0]
    for k in range(1, len(listeT)):
        pas = listeT[k] - listeT[k-1]
        yk = listeT[k-1] + fy(listeY[k-1], listeT[k-1]) * pas
        listeY.append(yk)
    return listeY

listeY = Euler(fy, 12, listeT)

plt.clf()
plt.figure('Représentation de Uc(t)')
plt.plot(listeT,listeY)
plt.show()