#importacion de las librerias utilizadas
import math

#variables requeridas
D=float(input('Ingrese el diametro de la tubería en m: '))
L=float(input('Ingrese la longitud de la tubería en m: '))
H=float(input('Ingrese la alturas del punto mas alto de agua en m: '))
z2=float(input('Ingrese la cota del punto dos en m: '))
Ks=float(input('Ingrese la rugosidad absoluta en m: '))
Km=float(input('Ingrese el coeficiente de perdidas por accesorios: '))
v=float(input('Ingrese el valor de la viscosidad cinematica en m^2/s : '))
u=float(input('Ingrese el valor de la viscosidad dinamica en Pa*s : '))
ro=float(input('Ingrese el valor de densidad en Kg/m3 : '))

#constantes
g=9.81

#variables calculadas a partir de primarias
Hfi=H-z2 #suposicion inicial de hf para empezar las iteraciones 
Ksd=Ks/D #rogosidad relativa
A=math.pi*(D**2)/4 #Area de la tuberia
if u>0:
    v=u/ro

#error
E=0.00000001 #error aceptable
Ei=0.9 #inicializacion del error

#codigo iterativo para la velocidad
Cont=0
while Ei>E:
	V=((-2*(2*g*D*Hfi)**0.5)/(L**0.5))*math.log10((Ksd/3.7)+((2.51*v*L**0.5)/(D*(2*g*D*Hfi)**0.5)))
	Hf=H-z2-(Km*V**2/(2*g))#nuevo hf a partir de la velocidad calculada con la suposicion
	Ei=abs(Hf-Hfi)#calculo del error
	Hfi=Hf#nuevo asigno el valor calculado para que se proceda a calcular nuevamente la velocidad.
	Cont=Cont+1#contador de iteraciones
    
#resultado    
Q=V*A
print('El caudal es igual a:', Q, 'm^3/s')
print('fue calculado en ', Cont, 'iteraciones')
