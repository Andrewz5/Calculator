import unittest
from Calculator import *
class CalculatorTest(unittest.TestCase):    
    def setUp(self):
        self.calcTest = Calculator()
    #test 
    def testAdd(self):
        self.assertEqual(self.calcTest.add(5,5), 10)
        self.assertNotEqual(self.calcTest.add(2,2), 5)
    
    def testSub(self):
        self.assertEqual(self.calcTest.sub(5,5), 0)
        self.assertNotEqual(self.calcTest.sub(2,2), 1)
        



test=CalculatorTest()
test.setUp()
test.testAdd()
test.testSub()
