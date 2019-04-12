import sys

from config_client import config

sys.path.append("../tutorial")

from MyService import Client

# from ttypes import *
from RestClient import RESTClient
from PyQt5.QtWidgets import QApplication
from window import App

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from zeep import Client as SClient

try:
    # Create a client to use the protocol encoder
    try:
        transport = TSocket.TSocket(config["rpc"]["host"], config["rpc"]["port"])

        # Buffering is critical. Raw sockets are very slow
        transport = TTransport.TBufferedTransport(transport)

        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client_rpc = Client(protocol)
        transport.open()
        transport.close()
    except:
        client_rpc = None
    try:
        client_soap = SClient(config["soap"]["url"])
    except:
        client_soap = None
    try:
        client_rest = RESTClient(config["rest"]["url"])
    except:
        client_rest = None

    App(transport, client_rpc, client_soap, client_rest)
    # Connect!
    # transport.open()

    # product = client.get_type_all()
    # print("4*5=%s" % (product))

    # # Close!
    # transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))
