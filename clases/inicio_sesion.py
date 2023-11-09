import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
from base_datos.conexion import Conexion

class Inicio_Sesion:
    def mostrar_interfaz_inicio_sesion(self):

        usuario_verificado = False

        # Función para verificar el usuario en la bd
        def verificar_usuario():
            nombre_usuario = entry_nombre_usuario.get()
            contrasena = entry_contrasena.get()

            # Conexión a la bd
            conexion = sql.connect('cleansa.db')
            cursor = conexion.cursor()

            # Verificar si el usuario y la contraseña existen
            cursor.execute('''SELECT * FROM usuario WHERE nombre_usuario=? AND contrasena=?''', (nombre_usuario, contrasena))
            resultado = cursor.fetchone()

            if resultado:
                # Usuario correcto
                usuario_verificado = True
            else:
                # Usuario incorrecto (muestra un mensaje de error)
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

            # Cerrar conexión a la bd
            conexion.cerrar_bd()

        # Ventana de inicio de sesión
        root = tk.Tk()
        root.geometry("400x300")
        root.title("Inicio de Sesión | CleanSA")
        root.config(bg="#5FB6D9")

        # Etiqueta y entrada para el nombre de usuario
        label_nombre_usuario = tk.Label(root, text="Nombre de usuario:", font=("Arial", 12), bg="#2685BF", fg="white")
        label_nombre_usuario.pack(pady=(10,0))
        entry_nombre_usuario = tk.Entry(root, font=("Arial", 12), bg="#BBE8F2", fg="black", borderwidth=2)
        entry_nombre_usuario.pack(pady=(0,10), padx=10, ipadx=50)

        # Etiqueta y entrada para contraseña
        label_contrasena = tk.Label(root, text="Contrasena:", font=("Arial", 12), bg="#2685BF", fg="white")
        label_contrasena.pack(pady=(10,0))
        entry_contrasena = tk.Entry(root, font=("Arial", 12), bg="#BBE8F2", fg="black", borderwidth=2, show="*")
        entry_contrasena.pack(pady=(0,10), padx=10, ipadx=50)

        # Botón para iniciar sesión
        boton_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=verificar_usuario, font=("Arial", 12), bg="#2685BF", fg="white")
        boton_iniciar_sesion.pack(pady=(10,20))

        # Iniciar la aplicación
        root.mainloop()