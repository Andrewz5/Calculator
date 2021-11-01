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
        
    def testMulti(self):
        self.assertEqual(self.calcTest.Multi(5,5), 25)
        self.assertNotEqual(self.calcTest.Multi(2,2), 5)
    
    def testDiv(self):
        self.assertEqual(self.calcTest.Div(5,5), 1)
        self.assertNotEqual(self.calcTest.Div(2,2), 2)
        



test=CalculatorTest()
test.setUp()
test.testAdd()
test.testSub()
test.testMulti()
test.testDiv()
