"""
Lista de Tareas
PROGRAMACION FUNCIONAL
INTERFACES TKINTER
"""
import tkinter as tk
from tkinter import messagebox

def agregar_tarea(entrada,lista):
    tarea=entrada.get()
    if tarea:
        lista.insert(tk.END,tarea)
        entrada.delete(0,tk.END)

def eliminar_tarea(lista):
    tareas_seleccionada=lista.curselection()
    if tareas_seleccionada:
        lista.delete(tareas_seleccionada)    

def salir(ventana):
    if messagebox.askokcancel("Salir","¿Estas seguro que quieres salir"):
        ventana.destroy()             

def principal():
    #Crear la ventana principal
    ventana=tk.Tk() #creando la ventana
    ventana.title("Lista de Tareas")


    #Creando los Widgets
    marco_lista=tk.Frame(ventana)
    marco_lista.pack(pady=10)

    #Widget de lista de Tareas
    lista_tareas=tk.Listbox(marco_lista,width=50,height=10)
    lista_tareas.pack(side=tk.LEFT,fill=tk.BOTH)

    #Widget de scrollbar
    scrollbar=tk.Scrollbar(marco_lista,orient=tk.VERTICAL)
    scrollbar.config(command=lista_tareas.yview)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    lista_tareas.config(yscrollcommand=scrollbar.set)

    #Marco de entrada para la nueva Tarea
    marco_entrada=tk.Frame(ventana)
    marco_entrada.pack(pady=5)

    #Creamos la etiqueta y la entrada
    etiqueta_tarea=tk.Label(marco_entrada,text="Nueva Tarea")
    etiqueta_tarea.pack(side=tk.LEFT)
    entrada_tarea=tk.Entry(marco_entrada,width=40)
    entrada_tarea.pack(side=tk.LEFT)

    #Creamos el Boton
    boton_agregar=tk.Button(ventana,text="Agregar Tarea",command=lambda :agregar_tarea(entrada_tarea,lista_tareas))
    boton_agregar.pack(pady=5)

    #Creamos un Boton para eliminar la tarea
    boton_eliminar=tk.Button(ventana,text="Eliminar Tarea" ,command=lambda:eliminar_tarea(lista_tareas))
    boton_eliminar.pack(pady=5)

    #Creamos un Boton para cerrar la interfaz(GUI)
    boton_salir=tk.Button(ventana,text="Salir",command=lambda:salir(ventana))
    boton_salir.pack(pady=5)
    ventana.mainloop()

if __name__=="__main__":
    principal()

