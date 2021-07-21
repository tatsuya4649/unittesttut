import unittest
from tools.ex1 import hoge

class Hoge(unittest.TestCase):
	def test_hoge(self):
		result = hoge(10)
		self.assertEqual(result,100)

		result = hoge(200)
		self.assertEqual(result,2000)

if __name__ == "__main__":
	unittest.main()
