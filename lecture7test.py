import lecture7code as code
import unittest

class TestTheArgMaxFunction (unittest.TestCase):
  def testRaiseException(self):
    self.assertRaises(ValueError, code.arg_max)
  def testSingleArgument(self):
    self.assertEqual(code.arg_max(555), 555)
  def testMultipleArguments(self):
    self.assertEqual(code.arg_max(-5, -4, 0, 8, 9), 9)
    self.assertEqual(code.arg_max(-10, -5, 25, 17, 12), 25)

