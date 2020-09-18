#importacion librerias utilizadas
import math

#variables requeridas
Q=float(input('Ingrese el caudal en m^3/s: '))
L=float(input('Ingrese la longitud de la tubería en m: '))
z2=float(input('Ingrese la cota del punto 2 en m: '))
D=float(input('Ingrese el diametro de la tubería en m: '))
Km=float(input('Ingrese el valor del coeficiente de pérdidas menores: '))
v=float(input('Ingrese el valor de la viscosidad m^2/s: '))
Ks=float(input('Ingrese el valor de la rugosidad absoluta en m: '))
n=float(input('Ingrese la eficiencia de la bomba: '))
ro=float(input('Ingrese la densidad del fluido kg/m^3: '))
u=float(input('Ingrese el valor de la viscosidad dinamica en Pa*s : '))

#constantes
g=9.81

#variables calculadad dadas las requeridas
A=math.pi*(D**2)/4
V=Q/A
Hm=Km #*(V**2)/(2*g)#perdidas por accesorios
Re=V*D/v
if u>0:
    v=u/ro

#calculo de f usando metodo Newton
fi=0.0001#suposicion inicial
E=0.00000001#error esperado
Ei=0.9#error supuesto
while Ei>E:
	f=((-2)*(math.log10((Ks/(3.7*D))+(2.51/(Re*math.sqrt(fi))))))**(-2)
	Ei=abs(f-fi)
	fi=f#factor de friccion   
print('El factor sde fricción es: ', fi)

#calculo hf o perdidas por friccion a partir del f calculado por iteracion
Hf=f*((L*V**2)/(D*2*g))
print('Las perdidas por fricción son (m): ', Hf)

#calculo cabeza total
HT=Hf+Hm+z2
print('Las perdidas totales son (m): ', HT)

#calculo potencia requerida (hp)
POT=((1/n)*ro*Q*g*HT)/745.7

#resultados
print('La potencia que necesita la bomba es: ', POT, 'hp')
