#!/usr/bin/python3
"""unittest"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """BaseModel testcase"""

    def test_uuid(self):
        """testing uuid"""
        base1 = BaseModel()
        base2 = BaseModel()
        # Ensure that the uuid are unique
        self.assertNotEqual(base1.id, base2.id)
        self.assertIsInstance(base1, BaseModel)
        self.assertTrue(base1.id)
        self.assertIsNotNone(base2.id)

    def test_created_at(self):
        """testing created_at"""
        base1 = BaseModel()
        self.assertIsInstance(base1.created_at, datetime)

    def test_updated_at(self):
        """testing updated_at"""
        base1 = BaseModel()
        self.assertIsInstance(base1.updated_at, datetime)

    def test_save(self):
        """testing save"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsNotNone(base1.save)
        self.assertNotEqual(base1.save, base2.save)

    def test_to_dict(self):
        """testing to_dict"""
        base1 = BaseModel()
        self.assertIsNotNone(base1.to_dict)


if __name__ == "__main__":
    unittest.main()
