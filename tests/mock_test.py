import unittest
import unittest.mock
import os
from tools.mock import hoge

class Mock(unittest.TestCase):
	def test_mock(self):
		m = unittest.mock.MagicMock()
		os.path.abspath = m

		hoge("hello")

		m.assert_called_with("hello")


if __name__ == "__main__":
	unittest.main()
