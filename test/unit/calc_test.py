import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_add_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)   
    def test_add_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())  

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True) 
    def test_divide_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)    
    def test_divide_method_fails_with_division_by_zero(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)         
    def test_divide_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    ######Se agregan más pruebas de las funciones creadas y de las que faltan##########

    #CASOS DE RAÍZ CUADRADA
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_sqrt_method_returns_correct_result(self, _validate_permissions):
        # Casos con números positivos
        self.assertEqual(self.calc.sqrt(4), 2)         # sqrt(4) = 2
        self.assertEqual(self.calc.sqrt(9), 3)         # sqrt(9) = 3
        self.assertEqual(self.calc.sqrt(16), 4)        # sqrt(16) = 4
        # Casos con número 0
        self.assertEqual(self.calc.sqrt(0), 0)         # sqrt(0) = 0
        # Casos con número decimal
        self.assertAlmostEqual(self.calc.sqrt(2), 1.41421356237, places=8)  # Aproximado para sqrt(2)
        self.assertAlmostEqual(self.calc.sqrt(0.25), 0.5, places=8)  # sqrt(0.25) = 0.5
        # Casos con números muy grandes y pequeños
        self.assertEqual(self.calc.sqrt(1e10), 100000)  # sqrt(1e10) = 100000
        self.assertEqual(self.calc.sqrt(1e-10), 1e-5)  # sqrt(1e-10) = 1e-5 

        # Casos de fallos
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)    
    def test_sqrt_method_fails_with_non_numeric_input(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.sqrt, "text")  # Texto no es válido
        self.assertRaises(TypeError, self.calc.sqrt, None)  # None no es válido
        self.assertRaises(TypeError, self.calc.sqrt, object())  # Objeto no es válido

    #CASOS LOGARITMO DE 10
    # Casos correctos
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True) 
    def test_log10_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(self.calc.log10(1), 0)  # log10(1) = 0
        self.assertEqual(self.calc.log10(10), 1)  # log10(10) = 1
        self.assertEqual(self.calc.log10(100), 2)  # log10(100) = 2
    # Casos incorrectos (parámetros no numéricos) 
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)   
    def test_log10_method_fails_with_non_numeric_input(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.log10, "text")  # Texto no es válido
        self.assertRaises(TypeError, self.calc.log10, None)  # None no es válido
        self.assertRaises(TypeError, self.calc.log10, object())  # Objeto no es válido
    # Casos incorrectos (valores no positivos para logaritmo)
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)     
    def test_log10_method_fails_with_non_positive_input(self, _validate_permissions):
        self.assertRaises(ValueError, self.calc.log10, 0)  # log(0) no está definido
        self.assertRaises(ValueError, self.calc.log10, -10)  # log(negativo) no está definido
        self.assertRaises(ValueError, self.calc.log10, -1)  # log(negativo) no está definido

    #CASOS PARA RESTAS
    # Casos correctos
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_substract_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(self.calc.substract(5, 3), 2)        # 5 - 3 = 2
        self.assertEqual(self.calc.substract(2, 2), 0)        # 2 - 2 = 0
        self.assertEqual(self.calc.substract(0, 3), -3)       # 0 - 3 = -3
        self.assertEqual(self.calc.substract(1, 5), -4)       # 1 - 5 = -4
        self.assertEqual(self.calc.substract(-3, -3), 0)      # -3 - (-3) = 0
        self.assertEqual(self.calc.substract(-5, 3), -8)      # -5 - 3 = -8
        self.assertEqual(self.calc.substract(0, 0), 0)        # 0 - 0 = 0
    # Casos incorrectos (entradas no numéricas)
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_substract_method_fails_with_non_numeric_input(self, _validate_permissions):
        # Comprobamos que se lanza un TypeError cuando los parámetros no son números
        self.assertRaises(TypeError, self.calc.substract, "text", 2)  # El primer parámetro es un texto
        self.assertRaises(TypeError, self.calc.substract, 2, "text")  # El segundo parámetro es un texto
        self.assertRaises(TypeError, self.calc.substract, "text", "text")  # Ambos parámetros son texto
        self.assertRaises(TypeError, self.calc.substract, None, 2)  # None no es válido
        self.assertRaises(TypeError, self.calc.substract, 2, None)  # None no es válido
        self.assertRaises(TypeError, self.calc.substract, object(), 2)  # Un objeto no es un número
        self.assertRaises(TypeError, self.calc.substract, 2, object())  # Un objeto no es un número
    # Otros casos de pruebas adicionales podrían ser:
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_substract_method_fails_with_missing_parameters(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.substract)  # No pasa ningún parámetro




if __name__ == "__main__":  # pragma: no cover
    unittest.main()
