import tkinter as Tk
import math
import matplotlib as mlib
mlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Ventana = Tk.Tk()

#pedido de valores iniciales

b=48#float(input('Ingrese el base del canal: '))
z=0#float(input('Ingrese el talud : '))
so=0.000121#float(input('Ingrese la pediente: '))
n=0.016#float(input('Ingrese el coheficiente de manning: '))
Q=273.4#float(input('Ingrese caudal: '))
alfa=1#float(input('Ingrese alfa: '))"

"""
b=float(input('Ingrese el base del canal: '))
z=float(input('Ingrese el talud : '))
so=float(input('Ingrese la pediente: '))
n=float(input('Ingrese el coheficiente de manning: '))
Q=float(input('Ingrese caudal: '))
alfa=float(input('Ingrese alfa: '))
"""
#yc=3.45328#float(input('Ingrese yc: '))
#yn=5.16#float(input('Ingrese yn: '))
#y=3.45#float(input('Ingrese y inicial: '))
#ystep=0.01#float(input('Ingrese el paso: '))
#ystop=5.16#float(input('valores de y hasta: '))

#Esa=0
#sfa=0
#xa=0


def GRAFICA():#aqui se incluyen las ecuuaciones que deseo graficar
    si=1#float(input('Ingrese 0=SistemaIngles  1=SistemaInternacional: '))
    
    
    yc=1.27#float(input('Ingrese yc: '))
    yn=100#infinito pero para que no lo grafique
    if so>0:
        yn=3.77#float(input('Ingrese yn: '))
        
    y=1.27#float(input('Ingrese y inicial: '))
    ystep=0.01#float(input('Ingrese el paso: '))
    ystop=3.7#float(input('valores de y hasta: '))
    """
    
    yc=float(input('Ingrese yc: '))
    yn=100
    if so>0:
        yn=float(input('Ingrese yn: '))
        
    """
    
    if so==0:
        print ('Su perfil es tipo H (horizontal)')
        
    if yn>yc:
        print ('Su perfil es tipo M (Mild)')
        
    if yn==yc:
        print ('Su perfil es tipo C (Critic)')
        
    if yc>yn:
        print ('Su perfil es tipo S (Supercritic)')
        
    print ('Si la pendiente es adversa , no hay yn, su perfil es tipo A (contrapendiente)')
    """
    y=float(input('Ingrese y inicial: '))
    ystep=float(input('Ingrese el paso: '))
    ystop=float(input('valores de y hasta: '))
    """
    
    
    
    ya=y#alterna para eliminar el primer deltaE
    Esa=0
    sfa=0
    xa=0
    x=0
    if si==0:
        g=32
    if si==1:
        g=9.81
        
    cont=0
    
    
    while y<ystop:
        #calculo de tipo de perfil
        cont=cont+1
        
        a=(b+z*y)*y
        rh=b+2*y*math.sqrt(1+z**2)
        rdct=(a/rh)**(4/3)
        rh43=rh**(4/3)
        v=Q/a
        Ev=alfa*((v**2)/(2*g))
        Es=y+Ev
        deltaE=Esa-Es
        
        if y==ya:
            deltaE=0
            
        Esa=Es
        
        if si==0:
            sf=((n**2)*(v**2))/(2.2201*rdct)
        
        if si==1:
            #sf=((n**2)*(v**2))/(rh**(4/3)) # posiblememte malo
            sf=((n**2)*(v**2))/(rdct)
            
        
        
        sfm=(sfa+sf)/2
        
        if y==ya:
            sfm=0
        sfa=sf
        deltax=deltaE/(so-sfm)
        x=xa+deltax
        xa=x
        yn=yn
        yc=yc
        
        print ('iteracion', cont, '--')
        print ('y.......', y, '--')
        print ('A.......', a, '--')
        print ('Rh......', rh, '--')
        if si==0:
            print ('rd^4/3..', rdct, '--')
            
        if si==1:
            print ('rh^4/3..', rh43, '--')
        print ('V.......', v, '--')
        print ('Ev......', Ev, '--')
        print ('DeltaE..',deltaE, '--')
        print ('Sf......',sf, '--')
        print ('Sfm.....',sfm, '--')
        print ('DeltaX..',deltax, '--')
        print ('X.......',x, '--')
        
        print ('-------------')
        yo=0
    
        
        #----
        plt.plot(x,y,".")
        
        if yn<100:
            plt.plot(x,yn,".")
            
        plt.plot(x,yc,".")
        plt.plot(x,yo,".")
        
        
        y=y+ystep
        
        fig1.canvas.draw()
        #inversion del eje x solo en la primera pantalla
        #ax = plt.gca()
        #ax.invert_xaxis()
        #
    plt.close
    
fig1 = plt.figure()#
#inversion del eje x
ax = plt.gca()
ax.invert_xaxis()
        #
FIGURA = FigureCanvasTkAgg( fig1, master=Ventana) #ventana donde está localizada nuestra grafica
FIGURA.get_tk_widget().grid(row=0, column=0)#

Tk.Button(Ventana, text="Graficar", command=GRAFICA).grid(row=1, column=0)#cuando de click en el boton se ejecuta GRAFICA

Ventana.mainloop()



