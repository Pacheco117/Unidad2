from tkinter import *
import tkinter as tk

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "Nayelly" and contrasena == "12345":
        resultado.config(text="El inicio de sesión ha sido exitoso")
    else:
        resultado.config(text="Las credenciales no coinciden")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.configure(padx=100, pady=100)
ventana.configure(bg="white")
ventana.geometry("1000x500") #ajustar tamaño
imagen = PhotoImage(file="Imagen.png") #llamar imagen en su ruta
fondo = Label(ventana, image=imagen).place(x=0, y=1)

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre = tk.Label(ventana, text="Nombre de usuario: ")
nombre.pack(pady=10)
nombre.config(font=('Arial', 12))
nombre.config(bg="white")
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack(pady=10)
contrasena = tk.Label(ventana, text="Contraseña: ")
contrasena.pack(pady=10)
contrasena.config(font=('Arial', 12))
contrasena.config(bg="white")
contrasena_usuario = tk.Entry(ventana, show="*")
contrasena_usuario.pack(pady=10)

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=10, pady=10)
iniciar_sesion.config(font=('Arial', 12))
iniciar_sesion.config(bg="#5BC70A", fg="white")
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()
salir.config(font=('Arial', 12))
salir.config(bg="#E83A00", fg="white")

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)
resultado.config(bg="white")

ventana.mainloop()
