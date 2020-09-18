
import math

den=float(input('Ingrese la densidad del fluido: '))
v=float(input('Ingrese la viscosidad cinemática: '))
n=int(input('Ingrese número de tuberías: '))
Ht=float(input('Ingrese la diferencia de alturas: '))
presi=0.0001
i=0
sumd5=0
g=9.81
d=[0.55,0.4,0,25,0.2]
l=[500,200,400,150]
ks=0.0000015
km=[4.5,4,5,8]
Ql=[0.055,0.07,0.06,0]
sumql=0


while i<n:
    #print ('Tuberia',i,': ')
    #d.append(float(input('Diametro: ')))
    #l.append(float(input('Longitud: ')))
    #ks=(float(input('ks: ')))
    #km.append(float(input('km: ')))
    #Ql.append(float(input('Q: ')))
    sumd5=sumd5+l[i]/((d[i])**5)
    i+=1

H=0
hf1=Ht*((l[0]/((d[0])**5)/(sumd5)))
print (hf1)
cont=0
while abs(H-Ht)>presi:
    sumhf=0
    sumhm=0
    vel1=((-2*(2*g*d[0]*hf1)**0.5)/(l[0]**0.5))*math.log10((ks[0]/(3.7*d[0]))+((2.51*v*l[0]**0.5)/(d[0]*(2*g*d[0]*hf1)**0.5)))
    #((-2*math.sqrt(2*g*d[0]*hf1)/math.sqrt(l[0]))*math.log10((ks[0]/(d[0]*3.7))+((2.51*v*math.sqrt(l[0]))/(d[0]*math.sqrt(2*g*d[0]*hf1)))))
    hm1=(km[0]*(vel1**2)/(2*g))
    Q1=(math.pi*vel1*(d[0]**2))/4
    i=1
    sumql=0
    #print ('Hf1: ',hf1,'V1: ',vel1,'Q1: ',Q1,'Hm1: ',hm1)
    while i<n:
        sumql=sumql+Ql[i-1]
        Q=Q1-sumql
        vel=(4*Q/(math.pi*d[i]**2))
        hm=(km[i]*(vel**2)/(2*g))
        fi=0.001
        a=math.pi*(d[i]**2)/4
        re=vel*d[i]/v
        presi=0.00000001
        error=1
        while error>presi:
            f=((-2)*(math.log10((ks[i]/(d[i]*3.7))+(2.51/(re*math.sqrt(fi))))))**(-2)
            error=abs(f-fi)
            fi=f
        #print('f: ',fi)
        hf=(fi*(l[i]/d[i])*(vel**2)/(2*g))
        #PARA VER TODAS LAS ITERACIONES#print ('Hf',i+1,': ',hf,'V',i+1,': ',vel,'Q',i+1,': ',Q,'Hm',i+1,': ',hm)
        sumhf=sumhf+hf
        sumhm=sumhm+hm
        i+=1
    H=sumhf+sumhm
    print(H)
    delthf1=(Ht-H)*(l[0]/(d[0]**5))/(sumd5)
    hf1=hf1+delthf1
    print ('_____________iter',cont+1,'______________')
    #print ('     delt hf1: ',delthf1)
    print ('     H',n,': ',H)
    print ('     Q',n,': ',Q)
    cont+=1
print (Q)   

    