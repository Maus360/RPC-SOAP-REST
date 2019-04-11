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

    # Make socket
    transport = TSocket.TSocket(config["rpc"]["host"], config["rpc"]["port"])

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client_rpc = Client(protocol)
    client_soap = SClient(config["soap"]["url"])
    client_rest = RESTClient(config["rest"]["url"])

    App(transport, client_rpc, client_soap, client_rest)
    # Connect!
    # transport.open()

    # product = client.get_type_all()
    # print("4*5=%s" % (product))

    # # Close!
    # transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))
