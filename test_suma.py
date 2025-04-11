import unittest
from suma import Suma



class TestSuma(unittest.TestCase):
    def test_suma_dosNumeeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma = Suma(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado,resultadoActual, "Falló la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = Suma(3, "a")
        with self.assertRaises(TypeError):
                objSuma.calcularSuma()


if __name__ == '__main__':
    unittest.main()
