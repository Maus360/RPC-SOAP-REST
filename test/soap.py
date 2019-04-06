import sys

sys.path.append("../soap")
import unittest
from unittest.mock import MagicMock
from main import HelloWorldService
from stypes import *
from db import DB
from sqlalchemy.orm import sessionmaker
import logging


class SOAPTest(unittest.TestCase):
    def test_test(self):
        assert "4" == str(4)

    def test_set_type(self):
        database = DB()
        database.set_type = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert (
            HelloWorldService.set_type(None, "Byte", "0", "255", "unsigned", 1, "")
            == None
        )

    def test_reset_type(self):
        database = DB()
        database.reset_type = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert (
            HelloWorldService.reset_type(None, 1, "Byte", "0", "255", "unsigned", 1, "")
            == None
        )

    def test_delete_type(self):
        database = DB()
        database.delete_type = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert HelloWorldService.delete_type(None, 1) == None

    def test_set_math_operation(self):
        database = DB()
        database.set_math_operation = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert (
            HelloWorldService.set_math_operation(
                None, "test1", "test2", "test3", "test4"
            )
            == None
        )

    def test_reset_math_operation(self):
        database = DB()
        database.reset_math_operation = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert (
            HelloWorldService.reset_math_operation(
                None, 1, "test1", "test2", "test3", "test4"
            )
            == None
        )

    def test_delete_math_operation(self):
        database = DB()
        database.delete_math_operation = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert HelloWorldService.delete_math_operation(None, 1) == None

    def test_set_class(self):
        database = DB()
        database.set_class = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert HelloWorldService.set_class(None, "MyClass24", 24, 36) == None

    def test_reset_class(self):
        database = DB()
        database.reset_class = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert HelloWorldService.reset_class(None, 1, "MyClass24", 24, 36) == None

    def test_delete_class(self):
        database = DB()
        database.delete_class = MagicMock(return_value=None)
        logger = logging.getLogger("RPC")
        logger.info = MagicMock(return_value=None)
        # iface = Iface(database, logger)
        assert HelloWorldService.delete_class(None, 1) == None


if __name__ == "__main__":
    unittest.main()
