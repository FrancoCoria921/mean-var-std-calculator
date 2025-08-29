import unittest
from mean_var_std import calculate

class TestCalculateFunction(unittest.TestCase):
    
    def test_lista_9_elementos(self):
        input_list = [0,1,2,3,4,5,6,7,8]
        result = calculate(input_list)
        
        # Verificar estructura del diccionario
        self.assertIn('mean', result)
        self.assertIn('variance', result)
        self.assertIn('standard deviation', result)
        self.assertIn('max', result)
        self.assertIn('min', result)
        self.assertIn('sum', result)
        
        # Verificar algunos valores específicos
        self.assertEqual(result['mean'][2], 4.0)
        self.assertEqual(result['sum'][2], 36)
    
    def test_lista_8_elementos(self):
        with self.assertRaises(ValueError) as context:
            calculate([0,1,2,3,4,5,6,7])
        
        self.assertEqual(str(context.exception), "La lista debe contener nueve números")

if __name__ == '__main__':
    unittest.main()