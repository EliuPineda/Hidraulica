
import math
from FUNPARASERIE import newton
from FUNPARASERIE import diseno
    
n=3#int(input('Ingrese número de tuberías: '))
den=999.1#float(input('Ingrese la densidad del fluido: '))
v=0.0000015#float(input('Ingrese la viscosidad cinemática: '))
Qn=0.0732#float(input('Ingrese caudal de salida (m3/s): '))
resp='p'#str(input('Para ingresar la potencia escriba (p), para cabeza escriba (h): '))
g=9.81
#if resp=='h':
#    Ht=float(input('Ingrese la altura total (Ht) en m: '))
#if resp=='p':
p=65000#    p=float(input('Ingrese la potencia de la bomba en w: '))
nb=0.85#    nb=float(input('Eficiencia de la bomba en tanto por uno: '))
l=[350,123,174]
ks=[0.0000015,0.0000015,0.0000015]
km=[7.9,3.3,3.5]
teta=[0,0,0]
Qtub=[0.0451,0.039,0.0732]#CAUDALES LATERALES
Q=[]#CAUDALES EN CADA TUBERIA SUMA ANTERIORES (Q1=Q2+Q3+...)
VR=[]
f=[]
hmR=[]
hfR=[]
hf=[]
hmv=[]
dn=[]
d=[]
i=0
sumlteta=0

#PARA CALCULAR LOS ÁNGULOS EN RAD

#CALCULAR EL COEFICIENTE DE LA ECUACION 5.11

#PARA PEDIR DATOS
i=0
#for i in range (n):
 #   print (i)
  #  l.append(float(input('L: ')))
   # ks.append(float(input('ks: ')))
    #km.append(float(input('km: ')))
#    Qtub.append(float(input('Q en cada tubería: ')))#CON CAUDALES TOTALES#Q.append(float(print('Q: ')))
 #   teta.append(float(input('teta: ')))
i=0
for i in range (n):
    tet=teta[i]
    tet=math.pi*tet/180
    teta.append(tet)

i=0
while i<n:
    sumlteta=sumlteta+l[i]*math.cos(teta[i])
    i+=1

print('')
print('_________________________')
#PARA CALCULAR EL HT CON LA POTENCIA
Qt=0
i=0
if resp=='p':
    for i in range(n):
        Qt=Qt+Qtub[i]#Ql[i]
    Ht=nb*p/(den*g*Qt)
    print('Ht: ',Ht) 

#PARA CALCULAR Qi CON CAUDALES TOTALES
Qt=0
for i in range (n):
    j=n-i-1
    Qt=Qt+Qtub[j]
    Q.insert(j,Qt)


#PARA CALCULAR Qi 5.8 Y hfi EC 5.11
#PARA LOS Q CON QLATERALES    
#Q1=Qn+Ql[0]
#Q.insert(0,Q1)
hf1=Ht*(l[0]*math.cos(teta[0])/sumlteta)
hf.insert(0,hf1)
#sumql=Ql[0]
i=1
while i<n:
#    sumql+=Ql[i]
 #   Q.insert(i,Q[0]-sumql)
    hf1=Ht*(l[i]*math.cos(teta[i])/sumlteta)
    hf.append(hf1)
    i+=1

   
    
#PARA CALCULAR d FLUJO 4 (DISEÑO)
print ('Q: ',Q)
print ('hfi: ',hf)
print('')
print('_________________________')
i=0
dni=0
hmvi=Ht
sw='false'
while i<n:
    di=diseno(l[i],den,v,ks[i],Q[i],Ht,km[i],g,hf[i])
    d.insert(i,di)
    VRi=4*Q[i]/(math.pi*d[i]**2)
    VR.insert(i,VRi)
    fi=newton(d[i],ks[i],Qtub[i],v)
    f.insert(i,fi)
    hfRi=fi*(l[i]/d[i])*(VRi**2/(2*g))
    hfR.insert(i,hfRi)
    hmRi=km[i]*(VRi**2/(2*g))
    hmR.insert(i,hmRi)
    print ('TUBERIA',i+1)
    print ('d',i+1,': ',di)
    print ('VR',i+1,': ',VRi)
    print ('f',i+1,': ',fi)
    print ('hfR',i+1,': ',hfRi)
    print ('hmR',i+1,': ',hmRi)
    
    i+=1
i=0
for i in range (n):
    hmvi=hmvi-hfR[i]-hmR[i]
for i in range (n):
    hfi=hfR[i]+hmvi
    hf.insert(i,hfi)

for i in range (n):
    dni=diseno(l[i],den,v,ks[i],Q[i],Ht,km[i],g,hf[i])
    dn.insert(i,dni)
    d[i]=dni
    VRi=4*Q[i]/(math.pi*dn[i]**2)
    VR.insert(i,VRi)
    fi=newton(dn[i],ks[i],Q[i],v)
    f.insert(i,fi)
    hfRi=fi*(l[i]/dn[i])*(VRi**2/(2*g))
    hfR.insert(i,hfRi)
    hmRi=km[i]*(VRi**2/(2*g))
    hmR.insert(i,hmRi)
    hmvi=Ht
    print ('TUBERIA',i+1)
    print ('d',i+1,': ',dni)
    print ('VR',i+1,': ',VRi)
    print ('f',i+1,': ',fi)
    print ('hfR',i+1,': ',hfRi)
    print ('hmR',i+1,': ',hmRi)
for i in range (n):
    hmvi=hmvi-hfR[i]-hmR[i]
for i in range (n):
    hfi=hfR[i]+hmvi
    hf.insert(i,hfi)
for i in range (n):
    
    if dn[i]==d[i]:
        i+=1
        if i>n:
            print (d)
    else:
        d.insert(i,dn[i])
        VRi=4*Q[i]/(math.pi*d[i]**2)
        VR.insert(i,VRi)
        fi=newton(d[i],ks[i],Qtub[i],v)
        f.insert(i,fi)
        f.insert(i,fi)
        hfRi=fi*(l[i]/d[i])*(VRi**2/(2*g))
        hfR.insert(i,hfRi)
        hmRi=km[i]*(VRi**2/(2*g))
        hmR.insert(i,hmRi)
        for i in range (n):
            hmvi=hmvi-hfR[i]-hmR[i]
            for i in range (n):
                hfi=hfR[i]+hmvi
                hf.insert(i,hfi)
        #print ('TUBERIA',i+1)
        #print ('d',i+1,': ',di)
        #print ('VR',i+1,': ',VRi)
        #print ('f',i+1,': ',fi)
        #print ('hfR',i+1,': ',hfRi)
        #print ('hmR',i+1,': ',hmRi)
        
        
print('')
print('_________________________')
