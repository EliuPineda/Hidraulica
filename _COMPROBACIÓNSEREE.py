#importacion de librerias
import math

D = []
L = []
Ks = []
Km = []
QL = []

Ksd = []
V = []
Q = []
hf = []
hm = []
A = []
Re = []
f = []

n=float(input("Ingrese el número de tuberías: "))
v=float(input("Ingrese la viscocidad del fluido en m/s^2: "))
HT=float(input("Ingrese la diferencia de alturas en m: "))


s = 0.001
tolerancia = 0.00000001
error = 10000000000


i = 0

while i<n:
	D.append(float(input("Ingrese el diametro de la tubería m: ")))
	L.append(float(input("Ingrese la longitud de la tubería en m: ")))
	Ks.append(float(input("Ingrese la rugosidad de la tubería en m: ")))
	Km.append(float(input("Ingrese el coeficiente total de perdidas menores en la tubería: ")))
	QL.append(float(input("Ingrese el caudal lateral en la tubería: ")))
	Ksdi = (Ks[i]/D[i])
	Ksd.insert(i,Ksdi)
	i = i +1
    

#1
i = 0

while i<n:
	Ksdi = (Ks[i]/D[i])
	Ksd.insert(i,Ksdi)
	i+=1


i=0
suma1=0

while i<n:
	suma1 = (suma1 + (L[i]/(D[i]**5)))
	i = i + 1

hf1 = (HT*((L[0])/(D[0]**5)))/(suma1)

HTT = 0

while math.fabs(HT-HTT)>tolerancia:
    V1=(-2*(((2*9.81*D[0]*hf1)**0.5)/(L[0]**0.5))*math.log10((Ksd[0]/3.7)+((2.51*v*L[0]**0.5)/(D[0]*(2*9.81*D[0]*hf1)))))
    Q1=(math.pi*V1*(D[0]**2))/4
    
    hm1 = (Km[0]*V1**2)/(2*9.81)
    
    i = 1
       
    Q.insert( 0,Q1)
    V.insert( 0,V1)
    hm.insert( 0,hm1)
    hf.insert( 0,hf1)
    A.insert(0,0)
    Re.insert(0,0)
    f.insert(0,0)
    
    QLT = 0
    
    suma2 = hf[0]
    
    suma3 = hm[0]
    
    while i<n:
        
        QLT = QLT + QL[i-1]
        qi = Q[0] - QLT
        Q.insert(i,qi)
        
        vi = (4*Q[i])/(math.pi*D[i]**2)
        V.insert(i,vi)
        
        hi = Km[i]*((V[i]**2)/(2*9.81))
        
        hm.insert(i,hi)
        
        suma3 = suma3 + hm[i]
        
        ai = (math.pi*D[i]**2)/4
        
        A.insert(i,ai)
        
        rei = ((V[i]*D[i])/v)
        Re.insert(i,rei)
        
        ree=Re[i]
        kse=Ks[i]
        de = D[i]
        while error>tolerancia:
            import math
            m = (pow(s,0.5))
            f1 = pow(-2*(math.log10(((2.51/(ree*m))+(kse/(3.7*de))))),-2)
            error = math.fabs((f1-s)/s)
            s = f1
        f.insert(i,s)
        s=0.001
        tolerancia = 0.00000001
        error = 10000000000
        
        hfi = f[i]*((L[i])/(D[i]))*((V[i]**2)/(2*9.81))
        hf.insert(i,hfi)
        suma2 = suma2 + hf[i]
        i=i+1   
            #rei = ((V[i]*D[i])/v)
            #Re.insert(i,rei)
            #ree = Re[i]	
            #print(ree) 
    HTT = suma2 + suma3
        
    if  math.fabs(HT-HTT)<tolerancia:           
        print("Ok")
        
    else:
        incrhf = (HT - HTT)*(((L[0])/(D[0]**5))/(suma1))
        hf1 = hf[0] + incrhf
        print("El nuevo Hf1 es:")
        print(hf1)
        Q = []
        V = []
        hm = []
        hf = []
        A = []
        Re = []
        f = [] 
    tolerancia = 0.00000001
    
            
print (Q)
            