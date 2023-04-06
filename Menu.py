import tkinter as tk
from tkinter import *

class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Mi primer menú")
        self.configure(bg="#F0F0F0")

        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)


        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir archivo", command=self.open_file)
        self.file_menu.add_command(label="Crear archivo", command=self.create_file)
        self.file_menu.add_command(label="Guardar archivo", command=self.save_file)
        self.file_menu.add_command(label="Importar", command=self.import_file)
        self.file_menu.add_command(label="Exportar", command=self.export_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Lupa", command=self.lupa)
        self.menu_bar.add_cascade(label="Herramientas", menu=self.edit_menu)

        # Agregamos algunos widgets a la pantalla
        self.label = tk.Label(self, text="¡Hola, mundo!")
        self.label.pack(pady=20)
        self.label.configure(bg="#F0F0F0", fg="#000")
        self.button = tk.Button(self, text="Presionar", command=self.press_button)
        self.button.pack()

        self.pack()

    def open_file(self):
        print("Abrir archivo")

    def create_file(self):
        print("Crear archivo")

    def save_file(self):
        print("Guardar archivo")

    def import_file(self):
        print("Importar archivo")

    def export_file(self):
        print("Exportar archivo")

    def quit_program(self):
        self.master.quit()

    def copy(self):
        print("Copiar")

    def paste(self):
        print("Pegar")

    def press_button(self):
        print("Botón presionado")

    def lupa(self):
        print("Lupa presionado")


root = tk.Tk()
root.geometry("420x380")
root.configure(bg="#F0F0F0")
root.configure(padx=0, pady=0)
root.geometry("500x200") #ajustar tamaño
imagen = PhotoImage(file="Imagen2.png") #llamar imagen en su ruta
fondo = Label(root, image=imagen).place(x=0, y=0)
app = MenuScreen(root)
app.mainloop()

