#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        base1 = BaseModel()
        base2 = BaseModel()
        #Ensure that thei uuid are unique
        self.assertNotEqual(base1.id, base2.id)
        self.assertIsNotNone(base1.created_at)
        self.assertIsNotNone(base2.updated_at)

    def test_save(self):
        pass

    def test_to_dict(self):
        pass

    def test_str(self):
        pass

if __name__ == "__main__":
    unittest.main()
