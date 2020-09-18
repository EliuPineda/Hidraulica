#importacion d librerias utilizadas
import math

#variables requeridas
l=float(input("Longitud de la tubería: "))
v=float(input("Viscosidad cinematica del fluido: "))
ks=float(input("Rugosidad de la tubería en m: "))
qd=float(input("Caudal de Diseño"))
h=float(input("Cabeza total: "))
km=float(input("Sumatoria de Km de accesorios: "))
z2=float(input("Ingrese la cota 2: "))
densi=float(input("Densidad del fluido: "))

#constantes
g=9.81

#Suposiciones
hf1=h-z2#se supone hf
deltd=0.0508#se escoge un delta de diametro para subir si es necesario
delth=0.1#se suponer para ser usado en el codigo subcodigo A
d=0.15#suposicion de un diametro pequeño

#inicializacion de variables
q=0#se inicializa la variable del caudal
cont=0#contador para iteraciones q>=qd
cont1=0#contador para las  iteraciones de Velocidad hasta que caudal sea mayor o igual al caudal de diseño
cont2=0#contador para las iteraciones dela  CONDICIÓN: |hf1-hf2|<=E

#presiciones
presi=0.00000001#presision del calculo



sw='false'#llave para calculo de caudal
swv='false'#llave para el calculo de hf
print('CONDICIÓN: Q>=Qd')
while sw=='false':
	print ('i: ',cont)
	print('	CONDICIÓN: Q>=Qd')
	while q<qd:#Calcular Velocidad hasta que caudal sea mayor o igual al caudal de diseño
		prueba=' NO CUMPLE'
		vel=((-2*math.sqrt(2*g*d*hf1))/math.sqrt(l))*math.log10((ks/(3.7*d))+(2.51*v*math.sqrt(l))/(d*math.sqrt(2*g*d*hf1)))
		q=vel*(math.pi*d**2)/4
		if q<qd:
			d=d+deltd
		#pass
		cont1+=1
		if q>=qd:
			prueba='CUMPLE'
		hm=km*(vel**2)/(2*g)
		vp=math.sqrt(2*g*h/km)#calculo Vp en la ecuacion 2.5
		print ('	i: ',cont1,' hf: ',hf1,' D: ',d,' V: ',vel,' Q: ',q,'PRUEBA Q>=Qd: ',prueba,'hm: ',hm,'Vp: ',vp)
#Calcular hf hasta que error >=resta hf-hf-1
	error=1

	print (' ')
	print ('	CONDICIÓN: V<Vp') # para altas perdidas menores
	vp=math.sqrt(2*g*h/km) #km=sumatoria km
	if vel>=vp:#me vota al procedimiento de altas perdidas menores
		hf1=0.5#asignacion de un hf pequeño
		while swv=='false':
			swv='false'
			sw='false'
			cont=0
			while sw=='false':
				sw='false'
				prueba='NO CUMPLE'
				vel=((-2*math.sqrt(2*g*d*hf1))/math.sqrt(l))*math.log10((ks/(3.7*d))+(2.51*v*math.sqrt(l))/(d*math.sqrt(2*g*d*hf1)))
				q=vel*math.pi*(d**2)/4
				d=d+deltd
				cont+=1
				if q>qd:
					prueba='CUMPLE'
					sw='true'
				hm=km*(vel**2)/(2*g)
				print ('	i: ',cont,' hf: ',hf1,' D: ',d,' V: ',vel,' Q: ',q,'PRUEBA Q>=Qd: ',prueba,'hm: ',hm,'Vp: ',vp)
			
			vp=math.sqrt(2*g*(h-hf1)/km)
			if vel<vp:
				swv='true'	
			
			error=abs(vel-vp)
			if error>=presi:
				if vel<vp:
					hf1=hf1+delth
				else:
					hf1=hf1-delth
				d=0.15#suponer un diametro pequeño
			else:
				swv='true'#si todo cumple, puedo salir del ciclo de perdidas menores y continuo con el diagrama de flujo
	else:#si se cumple que vi <vp (esto es la continuacion del codigo luego del subcodigo)
		print (' ')
		print('	CONDICIÓN: |hf1-hf2|<=E') #se continua evaluando la condicion comparando lo supuesto con lo calculado
		while presi<error:#mientras que esto suceda, se recalcula calcula la velocidad y el caudal
			prueba='NO CUMPLE'
			hm=km*(vel**2)/(2*g)#para poder calcular hf2
			hf2=h-z2-hm#para poder calcular la velocidad
			vel=((-2*math.sqrt(2*g*d*hf2))/math.sqrt(l))*math.log10((ks/(3.7*d))+(2.51*v*math.sqrt(l))/(d*math.sqrt(2*g*d*hf2)))
			q=vel*math.pi*(d**2)/4
			error=abs(hf1-hf2)
			hf1=hf2
			cont2+=1
			if error<=presi:
				prueba='CUMPLE'
			print ('	i: ',cont2,' hf: ',hf1,' |hf1-hf2|: ',error,' E: ',presi,' V: ',vel,' Q: ',q,'PRUEBA Q>=Qd: ',prueba,'hm: ',hm,'Vp: - ')
		if q>=qd:
			sw='true' #permite que el ciclo principal finalice
		else:
			d=d+deltd
			sw='false'
			hf1=h-z2
		cont+=1