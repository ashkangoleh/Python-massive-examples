import unittest
from app import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1),1)
    
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10),89)
    
    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30),1346269)
    
    
if __name__ == '__main__':
    unittest.main()