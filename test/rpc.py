import sys

sys.path.append("../tutorial")
import unittest
from unittest.mock import MagicMock
from MyService import Iface
from ttypes import *
from db import DB
from sqlalchemy.orm import sessionmaker
import logging


class RPCTest(unittest.TestCase):
    def test_test(self):
        assert "4" == str(4)

    def test_get_type_all(self):
        database = DB()
        database.get_type_all = MagicMock(
            return_value=[
                {
                    "name": "Byte",
                    "min_value": "0",
                    "max_value": "255",
                    "format_of_value": "unsigned",
                    "size": 1,
                    "description": "",
                    "id": 1,
                },
                {
                    "name": "Integer",
                    "min_value": "-32676",
                    "max_value": "32676",
                    "format_of_value": "signed",
                    "size": 4,
                    "description": "",
                    "id": 2,
                },
            ]
        )
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.get_type_all() == [
            ThType("Byte", "0", "255", "unsigned", 1, "", 1),
            ThType("Integer", "-32676", "32676", "signed", 4, "", 2),
        ]

    def test_get_type(self):
        database = DB()
        database.get_type = MagicMock(
            return_value={
                "name": "Byte",
                "min_value": "0",
                "max_value": "255",
                "format_of_value": "unsigned",
                "size": 1,
                "description": "",
                "id": 1,
            }
        )
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.get_type(1) == ThType("Byte", "0", "255", "unsigned", 1, "", 1)

    def test_set_type(self):
        database = DB()
        database.set_type = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.set_type("Byte", "0", "255", "unsigned", 1, "") == None

    def test_reset_type(self):
        database = DB()
        database.reset_type = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.reset_type(1, "Byte", "0", "255", "unsigned", 1, "") == None

    def test_delete_type(self):
        database = DB()
        database.delete_type = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.delete_type(1) == None

    def test_get_math_operations_all(self):
        database = DB()
        database.get_math_operations_all = MagicMock(
            return_value=[
                {
                    "name": "test1",
                    "type_of_argument": "test2",
                    "type_of_value": "test3",
                    "description": "test4",
                    "id": 1,
                }
            ]
        )
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.get_math_operations_all() == [
            ThMathOperation("test1", "test2", "test3", "test4", 1)
        ]

    def test_get_math_operation(self):
        database = DB()
        database.get_math_operation = MagicMock(
            return_value={
                "name": "test1",
                "type_of_argument": "test2",
                "type_of_value": "test3",
                "description": "test4",
                "id": 1,
            }
        )
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.get_math_operation(1) == ThMathOperation(
            "test1", "test2", "test3", "test4", 1
        )

    def test_set_math_operation(self):
        database = DB()
        database.set_math_operation = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.set_math_operation("test1", "test2", "test3", "test4") == None

    def test_reset_math_operation(self):
        database = DB()
        database.reset_math_operation = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.reset_math_operation(1, "test1", "test2", "test3", "test4") == None

    def test_delete_math_operation(self):
        database = DB()
        database.delete_math_operation = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.delete_math_operation(1) == None

    def test_get_class_all(self):
        database = DB()
        database.get_class_all = MagicMock(
            return_value=[
                {
                    "name": "MyClass22",
                    "number_of_methods": 12,
                    "number_of_properties": 56,
                    "id": 1,
                },
                {
                    "name": "MyClass23",
                    "number_of_methods": 2,
                    "number_of_properties": 7,
                    "id": 2,
                },
                {
                    "name": "MyClass24",
                    "number_of_methods": 24,
                    "number_of_properties": 36,
                    "id": 3,
                },
            ]
        )
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.get_class_all() == [
            ThClass("MyClass22", 12, 56, 1),
            ThClass("MyClass23", 2, 7, 2),
            ThClass("MyClass24", 24, 36, 3),
        ]

    def test_get_class(self):
        database = DB()
        database.get_class = MagicMock(
            return_value={
                "name": "MyClass24",
                "number_of_methods": 24,
                "number_of_properties": 36,
                "id": 3,
            }
        )
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.get_class(1) == ThClass("MyClass24", 24, 36, 3)

    def test_set_class(self):
        database = DB()
        database.set_class = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.set_class("MyClass24", 24, 36) == None

    def test_reset_class(self):
        database = DB()
        database.reset_class = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.reset_class(1, "MyClass24", 24, 36) == None

    def test_delete_class(self):
        database = DB()
        database.delete_class = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        iface = Iface(database, logger)
        assert iface.delete_class(1) == None


if __name__ == "__main__":
    unittest.main()
