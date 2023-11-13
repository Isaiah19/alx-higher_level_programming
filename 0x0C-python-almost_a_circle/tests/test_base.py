import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_incrementation(self):
        # Test if the id attribute is incremented correctly
        instance1 = Base()
        instance2 = Base()

        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)

    def test_custom_id(self):
        # Test if the id attribute is set to a custom value when provided
        instance = Base(id=100)

        self.assertEqual(instance.id, 100)

if __name__ == '__main__':
    unittest.main()

