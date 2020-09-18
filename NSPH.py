
#este codigo calcula la limitacion en la cabeza de succion positiva
print("introduce Q , D ,  Ks , skm, v , n , L , Z , NPSH , pv , ro , pat")


tolerancia = 0.00000001
error = 10000000000

Q = float (input())
D = float (input())
Ks = float (input())
skm = float (input())
v = float (input())
n = float (input())
L = float (input())
Z = float (input())
NPSH = float (input())
pv = float (input())
ro = float (input())
pat = float (input())

import math as mt
A  = (mt.pi*(D*D)/4)
V = (Q/A)
Re =((V*D)/v)
Ksd = (Ks/D)
shm = skm*((V*V)/(2*9.81))

#Newton Rhapshon

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

hf = f*(L/D)*((V*V)/(2*9.81))

H = hf + Z + shm


#Hs = hs + hfs + hms + ( (V*V)/(2*9.81) )

#NPSH = ( (pat/ro) - (pv/ro) ) - Hs 


Hs = ( (pat/(ro*9.81)) - (pv/(ro*9.81)) ) - NPSH

hs = Hs - hf - shm - ( (V*V)/(2*9.81) )

Pot = (1/n)*ro*Q*9.81*H 

print ( hs , Pot)




