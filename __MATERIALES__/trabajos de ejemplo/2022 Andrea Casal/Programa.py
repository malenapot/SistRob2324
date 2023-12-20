# LIBRERÍAS
from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
from tkinter import *
import threading
import random

# Para ser compatible con versiones antiguas de RoboDK:
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox

# ************************* FUNCIONES **********************************
# Función para cerrar la ventana
def onClose():
    ventana.destroy()
    RDK.Item('objeto').Delete()
    quit(0)

# Función para clasificar
def clasifica(clasificacion):
    # Posición inicial
    robot.MoveL(punto3)

    # Tarjet del objeto
    
    posObjeto = random.randint(1,3)
    if posObjeto == 1:
        objeto.setPose(transl(-500 ,0,50))
    if posObjeto == 2:
        objeto.setPose(transl(-500 ,200,50))
    if posObjeto == 3:
        objeto.setPose(transl(-500 ,-200,50))
    
    # Coger el objeto
    robot.MoveJ(objeto)
    robot.MoveJ(punto3)
    
    # Posición a la que debe mover el objeto en función de la clasificación:
    #Primera balda:
    if clasificacion == 1 or clasificacion == 2 or clasificacion == 3:
    
        robot.MoveL(punto1)
    
        if clasificacion == 1:
            robot.MoveL(posicion1)
        
        if clasificacion == 2:
            robot.MoveL(posicion2)
        
        if clasificacion == 3:
            robot.MoveL(posicion3)
        
        robot.MoveL(punto1)

    # Segunda balda:
    if clasificacion == 4 or clasificacion == 5 or clasificacion == 6:
    
        robot.MoveL(punto2)
        
        if clasificacion == 4:
            robot.MoveL(posicion4)
        
        if clasificacion == 5:
            robot.MoveL(posicion5)
        
        if clasificacion == 6:
            robot.MoveL(posicion6)
        
        robot.MoveL(punto2)

    # Tercera balda:
    if clasificacion == 7 or clasificacion == 8 or clasificacion == 9:
    
        robot.MoveL(punto3)
    
        if clasificacion == 7:
            robot.MoveL(posicion7)
        
        if clasificacion == 8:
            robot.MoveL(posicion8)
        
        if clasificacion == 9:
            robot.MoveL(posicion9)
        
        robot.MoveL(punto3)


# ************************ PROGRAMA ROBOT *****************************
# Link a RoboDK
RDK = robolink.Robolink()

# Escoger el objeto del robot, de la herramienta y la pieza lego:
robot = RDK.Item('', ITEM_TYPE_ROBOT)
frame = RDK.Item('UR3e Base',ITEM_TYPE_FRAME)
robot.setPoseFrame(frame)
obj = RDK.Item('Pieza lego')
tool = RDK.Item('RGI-35-14-O-B')
objeto = RDK.AddTarget('objeto', frame)


# Se cogen los tarjet 
# Tarjet para los puntos de partida para los movimientos
punto1 = RDK.Item('punto1', ITEM_TYPE_TARGET)
punto2 = RDK.Item('punto2', ITEM_TYPE_TARGET)
punto3 = RDK.Item('punto3', ITEM_TYPE_TARGET)

# Tarjet para la colocación en las posiciones 1, 2 y 3 (primera balda)
posicion1 = RDK.Item('posicion1', ITEM_TYPE_TARGET)
posicion2 = RDK.Item('posicion2', ITEM_TYPE_TARGET)
posicion3 = RDK.Item('posicion3', ITEM_TYPE_TARGET)

# Tarjet para la colocación en las posiciones 4, 5 y 6 (segunda balda)
posicion4 = RDK.Item('posicion4', ITEM_TYPE_TARGET)
posicion5 = RDK.Item('posicion5', ITEM_TYPE_TARGET)
posicion6 = RDK.Item('posicion6', ITEM_TYPE_TARGET)

# Tarjet para la colocación en las posiciones 7, 8 y 9 (tercera balda)
posicion7 = RDK.Item('posicion7', ITEM_TYPE_TARGET)
posicion8 = RDK.Item('posicion8', ITEM_TYPE_TARGET)
posicion9 = RDK.Item('posicion9', ITEM_TYPE_TARGET)



# Create a new window
ventana = tkinter.Tk()
ventana.geometry("400x300")

# Fijar titulo de la ventana
ventanaTitulo = 'Clasificador'
ventana.title(ventanaTitulo)

# Se elimina la ventana al cerrarla
ventana.protocol("WM_DELETE_WINDOW", onClose)


# Se incrusta la ventana
#EmbedWindow(ventanaTitulo)
clasificacion = tkinter.IntVar()
opciones = [("1",1),
            ("2",2),
            ("3",3),
            ("4",4),
            ("5",5),
            ("6",6),
            ("7",7),
            ("8",8),
            ("9",9)]

for texto,valor in opciones:
    tkinter.Radiobutton(ventana,text=texto, variable=clasificacion, value=valor).pack()

# Se añade un boton (clasifica al pulsarlo)
botonClasifica = Button(ventana, text='Clasificar', height=5, width=8, command= lambda: clasifica(clasificacion.get()))
botonClasifica.pack(fill=X)

# Se lanza la ventana en bucle
ventana.mainloop()


# Terminar al acabar el movimiento
robot.RunInstruction('Program_Done')





