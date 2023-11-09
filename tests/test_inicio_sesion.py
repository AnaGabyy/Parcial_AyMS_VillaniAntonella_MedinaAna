import unittest
from unittest.mock import patch
from clases.inicio_sesion import Inicio_Sesion


class Test_Inicio_Sesion(unittest.TestCase):
    def test_verificar_usuario(self):
        inicio_sesion = Inicio_Sesion()

        # Simulación de la entrada de usuario
        nombre_usuario_input = 'SilviaFlores'
        contrasena_input = '12345'

        with patch('tkinter.messagebox.showerror') as mock_showerror:
            inicio_sesion.verificar_usuario(nombre_usuario_input, contrasena_input)

            # Verifico si el usuario fue verificado
            self.assertTrue(inicio_sesion.usuario_verificado)
            print("La prueba fue exitosa.")

            # Verifico que el messagebox no fue llamado
            mock_showerror.assert_not_called()
