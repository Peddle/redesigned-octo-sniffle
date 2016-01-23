import unittest
from main import evaluate

class TestStringMethods(unittest.TestCase):

  def test1(self):
    self.assertEqual(evaluate("5+4"), 9)

  def test2(self):
    self.assertEqual(evaluate("5+4+3"), 12)

  def test3(self):
    self.assertEqual(evaluate("5"), 5)

  def test4(self):
    self.assertEqual(evaluate("5+4-3"), 6)

  def test4(self):
    self.assertEqual(evaluate("5+(4-3)"), 6)

  def test4(self):
    self.assertEqual(evaluate("5-(4-3)"), 4)
  

if __name__ == '__main__':
    unittest.main()