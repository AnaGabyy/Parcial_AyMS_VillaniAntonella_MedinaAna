import unittest
from unittest.mock import patch
from clases.inicio_sesion import Inicio_Sesion

class Test_Inicio_Sesion(unittest.TestCase):
    def test_verificar_usuario(self):
        # Simulación de la entrada de usuario
        nombre_usuario_input = 'SilviaFlores'
        contraseña_input = '12345'

        with patch('builtins.input', side_effect=[nombre_usuario_input, contraseña_input]):
            resultado = self.verificar_usuario()

        # Verifico si el resultado es true o none
        self.assertTrue(resultado)