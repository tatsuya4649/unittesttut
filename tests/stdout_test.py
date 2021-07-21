import sys
import unittest
from tools.stdout import hoge
from io import StringIO
from contextlib import redirect_stdout


class StdoutTest(unittest.TestCase):
	def test_stdout(self):
		io = StringIO()
		with redirect_stdout(io):
			hoge("hello world")
		self.assertEqual(io.getvalue(),"hello world\n")

if __name__ == "__main__":
	unittest.main()

