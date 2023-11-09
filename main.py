from clases.inicio_sesion import Inicio_Sesion
from tests.test_inicio_sesion import Test_Inicio_Sesion

if __name__ == "__main__":
    # Instancia de Inicio_Sesion
    inicio_sesion = Inicio_Sesion()

    # Mostrar la interfaz de inicio de sesión
    inicio_sesion.mostrar_interfaz_inicio_sesion()

# Prueba unitaria de inicio_sesion.py
test = Test_Inicio_Sesion()
test.test_verificar_usuario()
