import tkinter as tk

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "admin" and contrasena == "root":
        resultado.config(text="El inicio de sesión ha sido exitoso")
    else:
        resultado.config(text="Las credenciales no coinciden")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.configure(padx=300, pady=200)
ventana.configure(bg="brown")

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre = tk.Label(ventana, text="Nombre de usuario: ")
nombre.pack(pady=10)
nombre.config(font=('Arial', 12))
nombre.config(bg="yellow")
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack(pady=10)
contrasena = tk.Label(ventana, text="Contraseña: ")
contrasena.pack(pady=10)
contrasena.config(font=('Arial', 12))
contrasena.config(bg="yellow")
contrasena_usuario = tk.Entry(ventana, show="*")
contrasena_usuario.pack(pady=10)

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=10, pady=10)
iniciar_sesion.config(font=('Arial', 12))
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()
salir.config(font=('Arial', 12))

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)
resultado.config(bg="yellow")

ventana.mainloop()
