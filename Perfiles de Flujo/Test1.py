from matplotlib import pyplot

lenguajes = ("1", "2")
slices = (100, 130)
colores = ("red", "blue")

pyplot.pie(slices, colors=colores)
pyplot.axis("equal")
pyplot.title("Prueba Eliu")
pyplot.show()



import tkinter

def accion1():
    print("presiono 1")
    
def accion2():
    print("presiono 2")
    
mi_ventana = tkinter.Tk()
mi_ventana.geometry("1040x680")

mi_boton1 = tkinter.Button(text="Mi Boton1", command=accion1)
mi_boton1.pack()


mi_label = tkinter.Label(mi_ventana, text="Hello you are intelligtent", )
mi_label.pack(padx=20,pady=20)

mi_boton2 = tkinter.Button(text="Mi Boton2", command=accion2)
mi_boton2.pack()



mi_ventana.mainloop()


