import unittest
from app import fibo


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibo(1),1)
    
    def test_fibonacci_10(self):
        self.assertEqual(fibo(10),89)
    
    def test_fibonacci_30(self):
        self.assertEqual(fibo(30),1346269)
    
    
if __name__ == '__main__':
    unittest.main()