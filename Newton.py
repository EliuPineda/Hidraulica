import math
D=0.15 #float(input('Ingrese el diametro de la tubería en m: '))
Ks=0.043#float(input('Ingrese la rugosidad absoluta en mm: '))
Q=127#float(input('Ingrese el caudal en m^3/s: '))
v=1.858e-5 #float(input('Ingrese la viscosidad cinematica del fluido m^2/s): '))
#V=#1.53#float(input('Ingrese la velocidad en m/s: '))
print('_______________________________________________________________________')
print('')
fi=0.001
Ks=Ks/1000
A=math.pi*(D**2)/4
#print('Área (m^2): ', A)
V=Q/A

print('Velocidad (m/s): ', V)
Re=V*D/v
print('Reynolds: ', Re)
E=0.00000001
Ei=0.8
Iter=0
while Ei>E:
	f=((-2)*(math.log10((Ks/(3.7*D))+(2.51/(Re*math.sqrt(fi))))))**(-2)
	Ei=abs(f-fi)
	fi=f; print(f)
	Iter=Iter+1
print ('_______________________________________________________________________')
print('')
print ('El factor de fricción f es: ',f)
print('El número de iteraciones realizadas es igual a: ', Iter)