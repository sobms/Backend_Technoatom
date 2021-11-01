from backend_hw2_2 import CustomMeta, CustomClass
import unittest

class MetaClassTest(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def testMetaClass(self):
        self.assertEqual(self.inst.custom_x,50)
        self.assertEqual(self.inst.custom_line(),100)
        
        with self.assertRaises(AttributeError):
            x = self.inst.x

        with self.assertRaises(AttributeError):
            self.inst.line()
    
if __name__ == '__main__':
    unittest.main()
