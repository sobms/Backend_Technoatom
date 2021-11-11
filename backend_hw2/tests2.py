from backend_hw2_2 import CustomClass
import unittest

class MetaClassTest(unittest.TestCase):      

    def testMetaClass(self):
        inst = CustomClass()
        print(inst)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_line(), 100)
        with self.assertRaises(AttributeError):
            x = inst.x

        with self.assertRaises(AttributeError):
            inst.line()
    
if __name__ == '__main__':
    unittest.main()
