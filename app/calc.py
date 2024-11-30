import app
import math
from app import util

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        if not app.util.validate_permissions(f"{x} + {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, y)
        return x + y

    def substract(self, x, y):
        if not app.util.validate_permissions(f"{x} - {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, y)
        return x * y

    def divide(self, x, y):
        if not app.util.validate_permissions(f"{x} / {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        if not app.util.validate_permissions(f"{x} ** {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, y)
        return x ** y

            
    #Función agregada para la raíz cuadrada
    def sqrt(self, x):
        if not app.util.validate_permissions(f"sqrt({x})", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, None)  # Solo validamos 'x' porque solo tiene un parámetro
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

    #Función agregada para logaritmo en base 10
    def log10(self, x):
        if not app.util.validate_permissions(f"log10({x})", "user1"):
            raise InvalidPermissions('User has no permissions')
        app.util.check_types(x, None)  # Solo validamos 'x' porque solo tiene un parámetro
        if x <= 0:
            raise ValueError("Logarithm undefined for zero or negative numbers")   
        return math.log10(x)

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)

    calc2 = Calculator()
    result = calc.divide(2, 0)
    print(result)
