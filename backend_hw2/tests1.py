from backend_hw2 import CustomList
import unittest

class CustomListTest(unittest.TestCase):
    def setUp(self):
        self.list1 = CustomList([1,2,3,0,6,4])
    
    def testAdd(self):
        list2 = CustomList([9,8,7,10])
        self.assertEqual(self.list1 + list2, [10,10,10,10,6,4])
        self.assertEqual(list2 + self.list1, [10,10,10,10,6,4])
        with self.assertRaises(TypeError):
            lst = self.list1 + 3

        list2 = [1,1,1]
        self.assertEqual(self.list1 + list2, [2,3,4,0,6,4])
        self.assertEqual(list2 + self.list1, [2,3,4,0,6,4])

        list2 = [1,1,1,0,9,7,3,2]
        self.assertEqual(self.list1 + list2, [2,3,4,0,15,11,3,2])
        self.assertEqual(list2 + self.list1, [2,3,4,0,15,11,3,2])

    def testSubtract(self):
        list2 = CustomList([-1,-3,-7, 10])
        self.assertEqual(self.list1 - list2, [2,5,10,-10,6,4])
        self.assertEqual(list2 - self.list1, [-2,-5,-10,10,-6,-4])

        list2 = [1,1,1]
        self.assertEqual(self.list1 - list2, [0,1,2,0,6,4])
        self.assertEqual(list2 - self.list1, [0,-1,-2,0,-6,-4])

        list2 = [1,1,1,0,9,7,3,2]
        self.assertEqual(self.list1 - list2, [0,1,2,0,-3,-3,-3,-2])
        self.assertEqual(list2 - self.list1, [0,-1,-2,0,3,3,3,2])
        with self.assertRaises(TypeError):
            lst = self.list1 - 3

    def testCompare(self):
        list2 = CustomList([1,3,7, 10])
        self.assertTrue(self.list1<list2)
        list2 = CustomList([1,3,1, 10])
        self.assertTrue(self.list1>list2)
        list2 = CustomList([1,3,2, 10])
        self.assertTrue(self.list1>=list2)
        self.assertTrue(self.list1<=list2)

        list2 = [3,3,3]
        self.assertTrue(self.list1>list2)
        self.assertTrue(list2<self.list1)
        list2 = [6,6,6]
        self.assertTrue(self.list1<=list2)
        self.assertTrue(list2>=self.list1)

if __name__ == '__main__':
    unittest.main()