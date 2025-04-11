import unittest
from division import Division

class TestDivision(unittest.TestCase):
    def test_division_dosNumeros_retornaResultado(self):
        # Arrange
        dividendo = 20
        divisor = 4
        resultadoEsperado = 5

        objDivision = Division(dividendo, divisor)

        # Act
        resultadoActual = objDivision.calcularDivision()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, "Falló la división")

    def test_division_porCero_lanzaExcepcion(self):
        # Arrange
        objDivision = Division(10, 0)

        # Assert
        with self.assertRaises(ZeroDivisionError):
            objDivision.calcularDivision()

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        # Arrange
        objDivision = Division(10, "a")

        # Assert
        with self.assertRaises(TypeError):
            objDivision.calcularDivision()

if __name__ == '__main__':
    unittest.main()
