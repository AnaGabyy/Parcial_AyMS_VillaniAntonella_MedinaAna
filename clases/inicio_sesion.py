import tkinter as tk
from tkinter import messagebox
import sqlite3

def mostrar_interfaz_inicio_sesion():

    usuario_verificado = False

    def validar_dni(char):
        return char.isdigit() or char == ""

    # Función para verificar el usuario en la bd
    def verificar_usuario():
        dni = entry_dni.get()
        contraseña = entry_contraseña.get()

        # Conexión a la bd
        conexion = sqlite3.connect('cleanSA_bd.db')
        cursor = conexion.cursor()

        # Verificar si el usuario y la contraseña existen
        cursor.execute('SELECT * FROM usuario JOIN ficha ON usuario.fk_id_ficha = ficha.id WHERE ficha.dni=? AND usuario.contraseña=?', (dni, contraseña))
        resultado = cursor.fetchone()

        if resultado:
            # Usuario correcto
            usuario_verificado = True
        else:
            # Usuario incorrecto (muestra un mensaje de error)
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        # Cerrar conexión a la bd
        conexion.close()

    # Ventana de inicio de sesión
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Inicio de Sesión | CleanSA")
    root.config(bg="#5FB6D9")

    # Etiqueta y entrada para dni
    label_dni = tk.Label(root, text="DNI:", font=("Arial", 12), bg="#2685BF", fg="white")
    label_dni.pack(pady=(10,0))
    validar_comando = (root.register(validar_dni), "%S")
    entry_dni = tk.Entry(root, font=("Arial", 12), bg="#BBE8F2", fg="black", borderwidth=2, validate="key", validatecommand=validar_comando)
    entry_dni.pack(pady=(0,10), padx=10, ipadx=50)

    # Etiqueta y entrada para contraseña
    label_contraseña = tk.Label(root, text="Contraseña:", font=("Arial", 12), bg="#2685BF", fg="white")
    label_contraseña.pack(pady=(10,0))
    entry_contraseña = tk.Entry(root, font=("Arial", 12), bg="#BBE8F2", fg="black", borderwidth=2, show="*")
    entry_contraseña.pack(pady=(0,10), padx=10, ipadx=50)

    # Botón para iniciar sesión
    boton_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=verificar_usuario, font=("Arial", 12), bg="#2685BF", fg="white")
    boton_iniciar_sesion.pack(pady=(10,20))

    # Iniciar la aplicación
    root.mainloop()