2#librerias utilizadas
import numpy as np #para vectores y matrices
import matplotlib.pyplot as plt #para graficar

x = np.linspace(0, 0.25)#comienza en cero y termina en 0.25 y si le agrego otro numero indica cuantos valores voy a tomar 
 #np.arange(0, 8, 0.4)

#empieza grafica de de la funcion de la bomba
print("Este algoritmo le da la gráfica de la bomba; si conoce los parámetros escriba 1,  si deben ser calculados escriba 2")

opcion = float (input())#permite escoger entre conocer los coheficientes o calcularlos

if opcion == 1:#al conocer los coheficientes
    print("Introcuzca los parámetros de la bomba: A , B y C en ese orden.")
    A= float (input())
    B= float (input())
    C= float (input())
    y1 = (A*x*x + B*x + C)
  
    plt.plot(x, y1, 'r+')
    #plt.plot(x, y2, 'yo')
    
    print("La curva de la bomba es la siguiente:")
    plt.show()
    
    print("Si desea conocer la cabeza hidráulica para un caudal específico escriba 0, sino escriba otro número para finalizar")
    eva = float (input())
    
    if eva == 0:#permite hacer una evaluacion en la funciom para que la revision no sea al ojo
        def funcion(t):
            f= (A*t*t + B*t + C)
            return(f)
    
        print ("Digite el caudal que dsea evaluar")
        m = float (input())
        print(funcion(m))
    else:
         print("Es todo por hoy mi querido Whatson")


if opcion == 2:#no se conocen los coheficientes
    print("Introcuzca Q1 , H1 , Q2 , H2 , Q3 , H3 , en ese orden.")
    #se deben introducir al menos tres puntos caudal y cabeza total
    
    Q1= float (input())
    H1= float (input())
    Q2= float (input())
    H2= float (input())
    Q3= float (input())
    H3= float (input())
    
    Q12 = pow(Q1,2) #la funcion pow eleva al cuadrado
    Q22 = pow(Q2,2)
    Q32 = pow(Q3,2)
    
    am = Q2 - (Q22/Q1)
    
    ac = Q2*Q1 - Q22
    
    u = (H3 - ((H1*Q32)/(Q12)) + ((H2*Q32)/(ac)) - ((H1*Q22*Q32)/(Q12*ac)) - ((H2*Q3)/(am)) + ((H1*Q22*Q3)/(Q1*Q1*am)))
    
    uu = ( -((Q32)/(Q12)) - ((Q22*Q32)/(Q12*ac)) + ((Q32)/(ac)) + ((Q22*Q3)/(Q12*am)) - (Q3/am) + 1)
    
    C = (u/uu)
    
    B = ((H2 - ((H1*Q22)/Q12) + ((C*Q22)/Q12) - C )/( Q2 - (Q22/Q1) ))
    
    A = ( (H1/Q12) - (B/Q1) - (C/Q12) )
    
    print ( "Los coeficientes de la ecuación de la bomba son:" )
    
    print("A:")
    print( A )
    print("B:")
    print( B )
    print("C:")
    print( C )
    
    y1 = (A*x*x + B*x + C)
  
    plt.plot(x, y1, 'r+')
    #plt.plot(x, y2, 'yo')
    
    print("La curva de la bomba es la siguiente:")
    plt.show()
    
    print("Si desea conocer la cabeza hidráulica para un caudal específico escriba 0, sino escriba otro número para finalizar")
    eva = float (input())
    
    if eva == 0:
        def funcion(t):
            f= (A*t*t + B*t + C)
            return(f)
    
        print ("Digite el caudal que desea evaluar")
        m = float (input())
        print(funcion(m))
    else:
         print("Bye")
         
print("-----------------------------------------")
#empieza calculo curva del sistema
print("Curva del sistema")
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
         


print("intersección de curvas(bomba y sistema):")
    
y1 = (A*x*x + B*x + C)

plt.plot(x, y1, 'r+')

yhp = Z + (x*x*( ((f*L)/(2*9.81*A*A*D)) + (skm/(2*9.81*A*A) )))

plt.plot(x, yhp, 'b+')

plt.show()


