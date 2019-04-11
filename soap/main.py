import os
import sys
import logging
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Array
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

sys.path.append("../tutorial")
from db import Class as DBClass, MathOperations as DBMathOperations, Type as DBType, DB
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.config import server_config
from stypes import *


class HelloWorldService(ServiceBase):
    @rpc(_returns=Array(ThClass))
    def get_class_all(ctx):
        logger.info("Called method get_class_all")
        match = database.get_class_all()
        logger.info(f"Match {len(match)} records")
        result = [
            ThClass(
                record["name"],
                record["num_of_methods"],
                record["num_of_fields"],
                record["id"],
            )
            for record in match
        ]
        return result

    @rpc(Integer, _returns=ThClass)
    def get_class(ctx, iid):
        """
        Parameters:
        - iid
        """
        logger.info(f"Called method get_class with parameters: iid={iid}")
        result = database.get_class(iid)
        if result is None:
            # return InvalidID(iid, "There are no match result for requested id")
            return None
        return ThClass(
            result["name"],
            result["num_of_methods"],
            result["num_of_fields"],
            result["id"],
        )

    @rpc(Unicode, Integer, Integer)
    def set_class(ctx, name, num_of_methods, num_of_fields):
        """
        Parameters:
        - name
        - num_of_methods
        - num_of_properties
        """
        logger.info(
            f"Called method set_class with parameters: name={name},"
            + f"num_of_methods={num_of_methods}, num_of_fields={num_of_fields}"
        )
        database.set_class(name, num_of_methods, num_of_fields)

    @rpc(Integer, Unicode, Integer, Integer)
    def reset_class(ctx, iid, name, num_of_methods, num_of_fields):
        """
        Parameters:
        - iid
        - name
        - num_of_methods
        - num_of_properties
        """
        logger.info(
            f"Called method reset_class with parameters: iid={iid}, name={name},"
            + f"num_of_methods={num_of_methods}, num_of_fields={num_of_fields}"
        )
        database.reset_class(iid, name, num_of_methods, num_of_fields)

    @rpc(Integer)
    def delete_class(ctx, iid):
        """
        Parameters:
        - iid
        """
        logger.info(f"Called method delete_class with parameters: iid={iid}")
        database.delete_class(iid)

    @rpc(_returns=Array(ThMathOperation))
    def get_math_operations_all(ctx):
        logger.info("Called method get_math_operation_all")
        match = database.get_math_operations_all()
        logger.info(f"Match {len(match)} records")
        result = [
            ThMathOperation(
                record["name"],
                record["type_of_argument"],
                record["type_of_value"],
                record["description"],
                record["id"],
            )
            for record in match
        ]
        return result

    @rpc(Integer, _returns=ThMathOperation)
    def get_math_operation(ctx, iid):
        """
        Parameters:
        - iid
        """
        logger.info(f"Called method get_math_operation with parameters: iid={iid}")
        result = database.get_math_operation(iid)
        if result is None:
            # return InvalidID(iid, "There are no match result for requested id")
            return None
        return ThMathOperation(
            result["name"],
            result["type_of_argument"],
            result["type_of_value"],
            result["description"],
            result["id"],
        )

    @rpc(Unicode, Unicode, Unicode, Unicode)
    def set_math_operation(ctx, name, type_of_argument, type_of_value, description):
        """
        Parameters:
        - name
        - type_of_argument
        - type_of_value
        - description
        """
        logger.info(
            f"Called method set_math_operation with parameters: name={name},"
            + f"type_of_argument={type_of_argument}, type_of_value={type_of_value}, description={description}"
        )
        database.set_math_operation(name, type_of_argument, type_of_value, description)

    @rpc(Integer, Unicode, Unicode, Unicode, Unicode)
    def reset_math_operation(
        ctx, iid, name, type_of_argument, type_of_value, description
    ):
        """
        Parameters:
        - iid
        - name
        - type_of_argument
        - type_of_value
        - description
        """
        logger.info(
            f"Called method reset_math_operation with parameters: iid={iid}, name={name},"
            + f"type_of_argument={type_of_argument}, type_of_value={type_of_value}, description={description}"
        )
        database.reset_math_operation(
            iid, name, type_of_argument, type_of_value, description
        )

    @rpc(Integer)
    def delete_math_operation(ctx, iid):
        """
        Parameters:
        - iid
        """
        logger.info(f"Called method delete_math_operation with parameters: iid={iid}")
        database.delete_math_operation(iid)

    @rpc(_returns=Array(ThType))
    def get_type_all(ctx):
        logger.info("Called method get_type_all")
        match = database.get_type_all()
        logger.info(f"Match {len(match)} records")
        result = [
            ThType(
                record["name"],
                record["min_value"],
                record["max_value"],
                record["format_of_value"],
                record["size"],
                record["description"],
                record["id"],
            )
            for record in match
        ]
        return result

    @rpc(Integer, _returns=ThType)
    def get_type(ctx, iid):
        """
        Parameters:
        - iid
        """
        result = database.get_type(iid)
        logger.info(f"Called method get_type with parameters: iid={iid}")
        database.get_type(iid)
        if result is None:
            # return InvalidID(iid, "There are no match result for requested id")
            return None
        else:
            return ThType(
                result["name"],
                result["min_value"],
                result["max_value"],
                result["format_of_value"],
                result["size"],
                result["description"],
                result["id"],
            )

    @rpc(Unicode, Unicode, Unicode, Unicode, Integer, Unicode)
    def set_type(ctx, name, min_value, max_value, format_of_value, size, description):
        """
        Parameters:
        - name
        - min_value
        - max_value
        - format
        - size
        - description
        """
        logger.info(
            f"Called method set_type with parameters: name={name}, min_value={min_value},"
            + f" max_value={max_value}, format_of_value={format_of_value}, description={description}"
        )
        database.set_type(
            name, min_value, max_value, format_of_value, size, description
        )

    @rpc(Integer, Unicode, Unicode, Unicode, Unicode, Integer, Unicode)
    def reset_type(
        ctx, iid, name, min_value, max_value, format_of_value, size, description
    ):
        """
        Parameters:
        - iid
        - name
        - min_value
        - max_value
        - format
        - size
        - description
        """
        logger.info(
            f"Called method reset_type with parameters: iid={iid}, name={name}, min_value={min_value},"
            + f" max_value={max_value}, format_of_value={format_of_value}, description={description}"
        )
        database.reset_type(
            iid, name, min_value, max_value, format_of_value, size, description
        )

    @rpc(Integer)
    def delete_type(ctx, iid):
        """
        Parameters:
        - iid
        """
        logger.info(f"Called method delete_type with parameters: iid={iid}")
        database.delete_type(iid)


application = Application(
    [HelloWorldService],
    tns="spyne.examples.hello",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)


wsgi_app = WsgiApplication(application)


# You can use any Wsgi server. Here, we chose
# Python's built-in wsgi server but you're not
# supposed to use it in production.
# from wsgiref.simple_server import make_server

sys.path.append(os.getcwd())

database = DB()

logger = logging.getLogger("SOAP")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

if not os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), "log")):
    os.makedirs(os.path.join(os.path.dirname(os.path.realpath(__file__)), "log"))
handler = logging.FileHandler(
    os.path.join(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "log"), "out.log"
    )
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info(f"Start SOAP server")
print(f"Start SOAP server")
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server(
        server_config["soap"]["host"], server_config["soap"]["port"], wsgi_app
    )
    server.serve_forever()
