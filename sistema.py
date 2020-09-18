# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
print("Introduzca Caudal, Diámetro , Coeficiente de rugosidad , Sumatoria de acesorios , Viscosidad cinématica , Eficiencia , Longitud , Delta z; en ese orden:")

Q = float (input())
D = float (input())
Ks = float (input())
skm = float (input())
v = float (input())
n = float (input())
L = float (input())
Z = float (input())

A= (3.1416*(D*D)/4)
V= (Q/A)
Re=((V*D)/v)


xi=0.001
tolerancia=0.00000001
error=10000000000


while error>tolerancia:
	import math 
	Gx = -2*math.log10((Ks/(3.7*D))+((2.51*xi)/Re))
	gpx = (-2/math.log(10))*((2.51/Re)/((Ks/(3.7*D)+((2.51*xi)/Re)))) 
	xi1 = xi - ((Gx-xi)/(gpx-1))
	error = math.fabs(xi1-xi) 
	f = 1/(xi*xi)
	xi = xi1

print(f)

print("Este algoritmo le da la gráfica del sistema")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 0.25)


yhp = Z + (x*x*( ((f*L)/(2*9.81*A*A*D)) + (skm/(2*9.81*A*A) )))

plt.plot(x, yhp, 'r+')
    #plt.plot(x, y2, 'yo')
    
print("La curva del  sistema es la siguiente:")

plt.show()
