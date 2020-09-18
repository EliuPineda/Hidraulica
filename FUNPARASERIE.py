
def diseno (l,densi,v,ks,qd,h,km,g,hf1):
    import math
    #Suposiciones
    deltd=0.0508
    d=0.15
    q=0
    presi=0.00000001
    cont=0
    cont1=0
    cont2=0
    z2=0
    #Calcular Velocidad hasta que Q>=Qd
    sw='false'
    #print('CONDICIÓN: Q>=Qd')
    while sw=='false':
        #print ('i: ',cont)
        #print('	CONDICIÓN: Q>=Qd')
        while q<qd:
            #prueba=' NO CUMPLE'
            vel=((-2*math.sqrt(2*g*d*hf1))/math.sqrt(l))*math.log10((ks/(3.7*d))+(2.51*v*math.sqrt(l))/(d*math.sqrt(2*g*d*hf1)))
            q=vel*(math.pi*d**2)/4
            if q<qd:
                #from FUNCIONES import sig_diam_com
                d=d+deltd
                pass
            cont1+=1
            if q>=qd:
                prueba='CUMPLE'
                #print ('	i: ',cont1,' hf: ',hf1,' D: ',d,' V: ',vel,' Q: ',q,'PRUEBA: ',prueba)
    #Calcular hf hasta que error >=resta hf-hf-1
        error=1
        hf1=0
        #print (' ')
        #print('	CONDICIÓN: |hf1-hf2|<=E')
        while presi<error:
            prueba='NO CUMPLE'
            hf2=h-z2-km*(vel**2)/(2*g)
            vel=((-2*math.sqrt(2*g*d*hf2))/math.sqrt(l))*math.log10((ks/(3.7*d))+(2.51*v*math.sqrt(l))/(d*math.sqrt(2*g*d*hf2)))
            q=vel*math.pi*(d**2)/4
            error=abs(hf1-hf2)
            hf1=hf2
            cont2+=1
            if error<=presi:
                prueba='CUMPLE'
            print ('	i: ',cont2,' hf: ',hf1,' |hf1-hf2|: ',error,' E: ',presi,' V: ',vel,' Q: ',q,'PRUEBA: ',prueba)
        if q>=qd:
            sw='true'
        else:
            #from FUNCIONES import sig_diam_com
            d=d+deltd
            sw='false'
            hf1=h-z2
        cont+=1
    return d

def newton (d,ks,q,v):
    import math
    fi=0.001
    d=d
    ksd=(ks)/d
    a=math.pi*(d**2)/4
    vel=q/a
    re=vel*d/v
    presi=0.00000001
    error=1
    cont=0
    while error>presi:
        f=((-2)*(math.log10((ksd/(3.7))+(2.51/(re*math.sqrt(fi))))))**(-2)
        error=abs(f-fi)
        fi=f
        cont+=1
    return fi
