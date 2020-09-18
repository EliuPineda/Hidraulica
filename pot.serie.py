import math
Q=[]
V=[]
d=[]
l=[]
ks=[]
km=[]
Ql=[]
n=float(input("Ingrese el número de tuberías: "))
po=float(input("Ingrese la densidad del fluido: "))
v=float(input("Ingrese la viscocidad del fluido m^2/s"))
Qn=float(input("Ingrese el caudal en la tubería n: "))
HT=float(input("Ingrese la diferencia de alturas: "))
i=0
print("----------------------------------------")
while i<n:
    print("para la tuberia", i)
    d.append(float(input("Ingrese el diametro en la tubería i: ")))
    l.append(float(input("Ingrese la longitud en la tubería i: ")))
    ks.append(float(input("Ingrese la rugosidad en la tubería i: ")))
    km.append(float(input("Ingrese el coeficiente perdidas menores en la tubería i: ")))
    Ql.append(float(input("Ingrese el caudal lateral en la tubería i: ")))
    print("-------------------------------------------")
    i+=1
SQl=0
i=0
while i<n-1:
	SQl=SQl+Ql[i]
	i+=1
Q1=Qn+SQl
Q.insert(0,Q1)
i=1
while i<n:
	k=0
	SQL=0
	while k<i:
		SQL=SQL+Ql[k]
		k+=1
	Q.insert(i,Q1-SQL)
	i+=1
print(Q)
i=0
sumahf=0
sumahm=0
while i<n:
	Vi=4*Q[i]/(math.pi*d[i]**2)
	V.append(Vi)
	fi=0.001
	Re=(Vi*d[i])/v
	Eii=0.08
	Ee=0.00000001
	while Eii>Ee:
		f=((-2)*(math.log10((ks[i]/(3.7*d[i]))+(2.51/(Re*math.sqrt(fi))))))**(-2)
		Eii=abs(f-fi)
		fi=f
	hf=f*(l[i]/d[i])*(Vi**2)/(2*9.81)
	hm=km[i]*(Vi**2)/(2*9.81)
	sumahf=sumahf+hf
	sumahm=sumahm+hm
	i+=1

H=sumahf+sumahm
Ht=HT+H
print("----------------------------------")
P=po*Q1*9.81*Ht
P=P/1000
print("La potencia de la bomba es: ", P, "kW")