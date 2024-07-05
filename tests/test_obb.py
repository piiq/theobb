import unittest
from openbb import obb
from openbb_core.app.static.app_factory import BaseApp

class TestOpenBB(unittest.TestCase):
    def test_obb_import(self):
        self.assertIsInstance(obb, BaseApp)

if __name__ == '__main__':
    unittest.main()