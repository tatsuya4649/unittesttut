import unittest
from tools.exc import exception

class Error(unittest.TestCase):
	def test_except(self):
		# 先に発生し得るエラーを記述しておく。
		with self.assertRaises(TypeError):
			exception()

if __name__ == "__main__":
	unittest.main()
