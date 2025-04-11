class Division:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def calcularDivision(self):
        if not isinstance(self.dividendo, (int, float)) or not isinstance(self.divisor, (int, float)):
            raise TypeError("Los operandos deben ser numéricos")
        if self.divisor == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return self.dividendo / self.divisor
