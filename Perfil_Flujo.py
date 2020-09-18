import tkinter as Tk
import math
import matplotlib as mlib
mlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Ventana = Tk.Tk()

#pedido de valores iniciales
b=18#float(input('Ingrese el base del canal en m: '))
g=32#float(input('Ingrese la gravedad: '))
z=2#float(input('Ingrese el talud en m: '))
so=0.001#float(input('Ingrese ela pediente: '))
n=0.02#float(input('Ingrese el coheficiente de manning: '))
Q=800#float(input('Ingrese caudal: '))
alfa=1#float(input('Ingrese alfa: '))
#yc=3.45328#float(input('Ingrese yc: '))
#yn=5.16#float(input('Ingrese yn: '))
y=3.45#float(input('Ingrese y inicial: '))
ystep=0.01#float(input('Ingrese el paso: '))
ystop=5.16#float(input('valores de y hasta: '))

#Esa=0
#sfa=0
#xa=0


def GRAFICA():#aqui se incluyen las ecuuaciones que deseo graficar
    y=3.45#float(input('Ingrese y inicial: '))
    ya=y#alterna para eliminar el primer deltaE
    yc=3.45328#float(input('Ingrese yc: '))
    yn=5.16#float(input('Ingrese yn: '))
    Esa=0
    sfa=0
    xa=0
    x=0
    cont=0
    
    while y<ystop:
        #calculo de tipo de perfil
        cont=cont+1
        
        a=(b+z*y)*y
        rh=b+2*y*math.sqrt(1+z**2)
        rdct=(a/rh)**(4/3)
        v=Q/a
        Ev=alfa*((v**2)/(2*g))
        Es=y+Ev
        deltaE=Esa-Es
        
        if y==ya:
            deltaE=0
            
        Esa=Es
        sf=((n**2)*(v**2))/(2.2201*rdct)
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
        print ('rd^4/3..', rdct, '--')
        print ('V.......', v, '--')
        print ('Ev......', Ev, '--')
        print ('DeltaE..',deltaE, '--')
        print ('Sf......',sf, '--')
        print ('Sfm.....',sfm, '--')
        print ('DeltaX..',deltax, '--')
        print ('X.......',x, '--')
        
        print ('-------------')
        
        
        #----
        plt.plot(x,y,".")
        plt.plot(x,yn,".")
        plt.plot(x,yc,".")
        
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