#importacion de las librerias utilizadas
import math

#variables requeridas
Qd=float(input('Ingrese el caudal de diseño en m^3/s: '))
Ks=float(input('Ingrese la rugosidad absoluta de la tuberi­a en m: '))
DelD=float(input('Ingrese el valor del delta de diametro en m: '))
H=float(input('Ingrese el valor de H en m: '))
z2=float(input('Ingrese el valor de la cota 2 en m: '))
v=float(input('Ingrese el valor de la viscocidad en m^2/s: '))
L=float(input('Ingrese la longitud de la tuberÃ­a en m: '))
Km= float(input('Ingrese la sumatoria de los km para accesorios: '))
ro=float(input('Ingrese la densidad del fluido kg/m^3: '))
u=float(input('Ingrese el valor de la viscosidad dinamica en Pa*s : '))

#variables calculadas a partor de las requeridas
hf=H-z2#suposicion hf  
if u>0:
    v=u/ro
di=0.15#suponer un diametro pequeño
E=0.000000001#error esperado
Ei=0.9#error supuesto para las iteraciones 
Qi=0.005#caudal semilla para la iteracion del calculo de la velocidad


while Qi<Qd:
	while Qi<Qd:#calculo de la velocidad
		V=((-2*(2*9.81*di*hf)**0.5)/L**0.5)*math.log10((Ks/(3.7*di))+((2.51*v*L**0.5)/(di*(2*9.81*di*hf)**0.5)))
		Qi=(math.pi/4)*di**2*V
		if Qi<Qd: #si no se cumple la condicion el codigo no pasa por aquí
			di=di+DelD#varia el diametro en deltas (PROGARAMAR QUE INCLUYA EL DIAMETREO COMERCIAL)
	
	while Ei>E:#calculo de perdidas por friccion
		hfi=H-z2-Km*((V**2)/(2*9.81))
		Ei=abs(hfi-hf)
		if Ei>E:#si no se cumple la condicion el codigo no pasa por aquí
			V=((-2*(2*9.81*di*hfi)**0.5)/L**0.5)*math.log10((Ks/(3.7*di))+((2.51*v*L**0.5)/(di*(2*9.81*di*hfi)**0.5)))
			Qi=(math.pi/4)*di**2*V
			hf=hfi
            
	if Qi>=Qd:
		di=di/0.0254#En este punto se pueden meter el complemento del codigo para altas perdidas
		print ('El diametro de la tuberi­a es: ', di, 'en pulg')
		print ('El caudal final que presentara la tuberi­a es : ', Qi, 'm^3/s')
	else:
		di=di+DelD
		hf=H-z2#si pasamos por aca significa que la suposicion primera de hf es incorrecta
        
if (Km*((V**2)/(2*9.81)))>=(0.3*hf):
    print ('se debe calcular con altas perdidas porque las hm superan el 30% de hf')