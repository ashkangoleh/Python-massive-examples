import unittest

def cuboid_volume(l):
    return (l*l*l)

def iter_volume(l:list):
    return l


def bool_volume(l:bool):
    return l

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)
        
        self.assertCountEqual(iter_volume([1,2]),[2,1,3])
        
        
    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume)
        
    def test_bool_input_value(self):
        self.assertFalse(bool_volume(True))
        
