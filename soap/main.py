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

from gunicorn.app.base import Application as GApplication


class HelloWorldService(ServiceBase):
    @rpc(_returns=Array(ThClass))
    def get_class_all(ctx):
        logger.info("Called method get_class_all")
        match = database.get_class_all()
        logger.info(f"Match {len(match)} records")
        result = [
            ThClass(
                record["name"],
                record["number_of_methods"],
                record["number_of_properties"],
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
            result["number_of_methods"],
            result["number_of_properties"],
            result["id"],
        )

    @rpc(Unicode, Integer, Integer)
    def set_class(ctx, name, num_of_methods, num_of_properties):
        """
        Parameters:
        - name
        - num_of_methods
        - num_of_properties
        """
        logger.info(
            f"Called method set_class with parameters: name={name},"
            + f"num_of_methods={num_of_methods}, num_of_properties={num_of_properties}"
        )
        database.set_class(name, num_of_methods, num_of_properties)

    @rpc(Integer, Unicode, Integer, Integer)
    def reset_class(ctx, iid, name, num_of_methods, num_of_properties):
        """
        Parameters:
        - iid
        - name
        - num_of_methods
        - num_of_properties
        """
        logger.info(
            f"Called method reset_class with parameters: iid={iid}, name={name},"
            + f"num_of_methods={num_of_methods}, num_of_properties={num_of_properties}"
        )
        database.reset_class(iid, name, num_of_methods, num_of_properties)

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


class StandaloneApplication(GApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict(
            [
                (key, value)
                for key, value in self.options.items()
                if key in self.cfg.settings and value is not None
            ]
        )
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


wsgi_app = WsgiApplication(application)


# You can use any Wsgi server. Here, we chose
# Python's built-in wsgi server but you're not
# supposed to use it in production.
# from wsgiref.simple_server import make_server

database = DB()

logger = logging.getLogger("SOAP")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/home/maus/bsuir/3/AiPOSiZI/rpc-soap/soap/log/out.log")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info(
    f"Start server at {server_config['soap']['host']}:{server_config['soap']['port']}"
)
# server = make_server("127.0.0.1", 8000, wsgi_app)
# server = make_server(
#     server_config["soap"]["host"], server_config["soap"]["port"], wsgi_app
# )
# Application.run(wsgi_app)
options = {"bind": f'{server_config["soap"]["host"]}:{server_config["soap"]["port"]}'}
# logger.info(
#     f"Start server at {server_config['soap']['host']}:{server_config['soap']['port']}"
# )
# StandaloneApplication(wsgi_app, options).run()

# server.serve_forever()

