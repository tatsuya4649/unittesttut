import unittest
from tools.ex1 import hoge

class HogeLoop(unittest.TestCase):
	def test_hoge(self):
		patterns = [
		(1,10),
		(2,20),
		(3,30),
		(10,100),
		]

		for x,res in patterns:
			with self.subTest(arg=x,result=res):
				self.assertEqual(hoge(x),res)


if __name__ == "__main__":
	unittest.main()
