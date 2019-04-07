import sys
import logging
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append("../tutorial")
# from ttypes import *


class App(QWidget):
    def __init__(self, transport, client_rpc, client_soap, client_rest):
        super().__init__()
        self.clients = [client_rpc, client_soap.service, client_rest]
        self.transport = transport
        self.transport.open()
        self.subject = None
        self.title = "Have a nice day!"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.funcs = {
            "type": {
                "fields": [
                    "Name",
                    "Min value",
                    "Max value",
                    "Format",
                    "Size",
                    "Description",
                ],
                "index": client_rpc.get_type_all,
                "get": client_rpc.get_type,
                "set": client_rpc.set_type,
                "reset": client_rpc.reset_type,
                "delete": client_rpc.delete_type,
                "result": lambda record: [
                    record.name,
                    record.min_value,
                    record.max_value,
                    record.format_of_value,
                    str(record.size),
                    record.description,
                ],
            },
            "class": {
                "fields": ["Name", "Number of methods", "Number of Properties"],
                "index": client_rpc.get_class_all,
                "get": client_rpc.get_class,
                "set": client_rpc.set_class,
                "reset": client_rpc.reset_class,
                "delete": client_rpc.delete_class,
                "result": lambda record: [
                    record.name,
                    str(record.num_of_methods),
                    str(record.num_of_fields),
                ],
            },
            "mo": {
                "fields": ["Name", "Type of argument", "Type of value", "Description"],
                "index": client_rpc.get_math_operations_all,
                "get": client_rpc.get_math_operation,
                "set": client_rpc.set_math_operation,
                "reset": client_rpc.reset_math_operation,
                "delete": client_rpc.delete_math_operation,
                "result": lambda record: [
                    record.name,
                    record.type_of_argument,
                    record.type_of_value,
                    record.description,
                ],
            },
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.window_layout = QVBoxLayout()
        self.scroll = QScrollArea()
        self.header()
        self.window_layout.addWidget(self.h_box)
        self.setLayout(self.window_layout)

        self.tableWidget = QTableWidget()
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.show()
        sys.exit(app.exec_())

    def header(self):
        self.button_types = QPushButton("Types", self)
        self.button_types.clicked.connect(partial(self.__get_record_all, "type"))
        self.button_classes = QPushButton("Classes", self)
        self.button_classes.clicked.connect(partial(self.__get_record_all, "class"))
        self.button_mo = QPushButton("Math operations", self)
        self.button_mo.clicked.connect(partial(self.__get_record_all, "mo"))
        # self.button_protocol = QPushButton("RPC->SOAP", self)
        self.button_protocol = QComboBox()
        self.button_protocol.addItems(["RPC", "SOAP", "REST"])
        # self.button_protocol.clicked.connect(self.__change_protocol)
        self.button_protocol.currentIndexChanged.connect(self.__change_protocol)
        self.button_new = QPushButton("New")
        self.button_new.clicked.connect(partial(self.__new_record, False, "type"))
        self.button_search = QPushButton("🔍")
        self.button_search.clicked.connect(self.__search)
        self.textarea_search = QLineEdit()
        self.h_box = QGroupBox()
        layout = QHBoxLayout()
        layout.addWidget(self.button_classes)
        layout.addWidget(self.button_mo)
        layout.addWidget(self.button_types)
        layout.addWidget(self.button_protocol)
        layout.addWidget(self.button_new)
        layout.addWidget(self.textarea_search)
        layout.addWidget(self.button_search)
        self.h_box.setLayout(layout)

    def __search(self):
        funcs = {
            None: partial(self.__get_record_all, "type"),
            "type": partial(self.__get_record_all, "type"),
            "mo": partial(self.__get_record_all, "mo"),
            "class": partial(self.__get_record_all, "class"),
        }
        funcs[self.subject](search=self.textarea_search.text())

    def __change_protocol(self, *args):
        if args[0] == 0:
            self.transport.close()
            self.transport.open()
        else:
            self.transport.close()
        self.funcs = {
            "type": {
                "fields": [
                    "Name",
                    "Min value",
                    "Max value",
                    "Format",
                    "Size",
                    "Description",
                ],
                "index": self.clients[args[0]].get_type_all,
                "get": self.clients[args[0]].get_type,
                "set": self.clients[args[0]].set_type,
                "reset": self.clients[args[0]].reset_type,
                "delete": self.clients[args[0]].delete_type,
                "result": lambda record: [
                    record.name,
                    record.min_value,
                    record.max_value,
                    record.format_of_value,
                    str(record.size),
                    record.description,
                ],
            },
            "class": {
                "fields": ["Name", "Number of methods", "Number of Properties"],
                "index": self.clients[args[0]].get_class_all,
                "get": self.clients[args[0]].get_class,
                "set": self.clients[args[0]].set_class,
                "reset": self.clients[args[0]].reset_class,
                "delete": self.clients[args[0]].delete_class,
                "result": lambda record: [
                    record.name,
                    str(record.num_of_methods),
                    str(record.num_of_fields),
                ],
            },
            "mo": {
                "fields": ["Name", "Type of argument", "Type of value", "Description"],
                "index": self.clients[args[0]].get_math_operations_all,
                "get": self.clients[args[0]].get_math_operation,
                "set": self.clients[args[0]].set_math_operation,
                "reset": self.clients[args[0]].reset_math_operation,
                "delete": self.clients[args[0]].delete_math_operation,
                "result": lambda record: [
                    record.name,
                    record.type_of_argument,
                    record.type_of_value,
                    record.description,
                ],
            },
        }

        self.client = self.clients[args[0]]

    def __get_record_all(self, name: str, search=None):
        self.window_layout.removeWidget(self.scroll)
        self.window_layout.removeWidget(self.tableWidget)
        self.tableWidget = QTableWidget()
        logger.debug(f"get_record_all of {name}")
        self.subject = name
        self.window_layout.removeWidget(self.scroll)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        result = self.funcs[name]["index"]()
        self.tableWidget.setColumnCount(len(self.funcs[name]["fields"]) + 1)
        self.tableWidget.setHorizontalHeaderLabels(
            self.funcs[name]["fields"] + ["View"]
        )
        if search:
            logger.debug(f"Change result query by search {search}")
            result = [
                record
                for record in result
                if any([search in str(string) for string in vars(record).values()])
            ]
        logger.debug("generate table")
        for index, record in enumerate(result):
            logger.debug(f"set {index} record of values {record}")
            result = self.funcs[name]["result"](record)
            self.tableWidget.insertRow(index)
            for i in range(len(self.funcs[name]["fields"])):
                self.tableWidget.setItem(index, i, QTableWidgetItem(result[i]))
            button_view = QPushButton("View")
            button_view.clicked.connect(partial(self.__get_record, name, record.id))
            self.tableWidget.setCellWidget(
                index, len(self.funcs[name]["fields"]), button_view
            )

        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)
        self.window_layout.removeWidget(self.scroll)
        self.window_layout.addWidget(self.tableWidget)

    def __get_record(self, name, iid):
        self.window_layout.removeWidget(self.scroll)
        try:
            result = self.funcs[name]["get"](iid)
            buttons = QHBoxLayout()
            self.button_edit = QPushButton("Edit")
            self.button_edit.clicked.connect(partial(self.__edit_record, name, iid))
            buttons.addWidget(self.button_edit)
            self.button_delete = QPushButton("Delete")
            self.button_delete.clicked.connect(partial(self.__delete_record, name, iid))
            buttons.addWidget(self.button_delete)
            layout = QVBoxLayout()
            self.fields = []

            for index, field in enumerate(self.funcs[name]["fields"]):
                self.fields.append(
                    QTextEdit(str(self.funcs[name]["result"](result)[index]))
                )
                layout.addWidget(QLabel(field))
                self.fields[-1].setReadOnly(True)
                layout.addWidget(self.fields[-1])

            lay = QVBoxLayout()
            lay.addLayout(buttons)
            lay.addLayout(layout)
            record_layout = QGroupBox()
            record_layout.setLayout(lay)
            self.scroll = QScrollArea()
            self.scroll.setWidget(record_layout)
            self.scroll.setWidgetResizable(True)
            self.window_layout.removeWidget(self.tableWidget)
            self.window_layout.addWidget(self.scroll)
        except Exception as e:
            logger.error(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("No such record, may it already deleted")
            msg.setWindowTitle("Error!")
            msg.exec_()
            self.__get_record_all(name)

    def __edit_record(self, name, iid, submit=False):
        funcs = {
            "type": [self.client.reset_type, [str, str, str, str, int, str]],
            "mo": [self.client.reset_math_operation, [str, str, str, str]],
            "class": [self.client.reset_class, [str, int, int]],
        }
        if submit == True:
            [field.setReadOnly(True) for field in self.fields]
            try:
                argv = [
                    funcs[name][1][index](i.toPlainText())
                    for index, i in enumerate(self.fields)
                ]
                funcs[name][0](iid, *argv)
                self.__get_record_all(name)
            except Exception as e:
                logger.error(e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Error")
                msg.setInformativeText("You enter invalid type of value")
                msg.setWindowTitle("Error!")
                msg.exec_()
                self.__get_record(name, iid)
        else:
            [field.setReadOnly(False) for field in self.fields]
            self.button_edit.setText("Submit")
            self.button_edit.clicked.connect(
                partial(self.__edit_record, name, iid, True)
            )

    def __delete_record(self, name, iid):
        funcs = {
            "type": self.client.delete_type,
            "mo": self.client.delete_math_operation,
            "class": self.client.delete_class,
        }
        funcs[name](iid)
        logger.debug(f"delete {name}, {iid}")
        self.__get_record_all(name)

    def __new_record(self, submit, name, *args):
        funcs = {
            "type": [self.client.set_type, [str, str, str, str, int, str]],
            "mo": [self.client.set_math_operation, [str, str, str, str]],
            "class": [self.client.set_class, [str, int, int]],
        }
        self.window_layout.removeWidget(self.scroll)
        self.window_layout.removeWidget(self.tableWidget)
        if submit:
            try:
                argv = [
                    funcs[name][1][index](i.toPlainText())
                    for index, i in enumerate(self.fields)
                ]
                funcs[name][0](*argv)
                self.__get_record_all(name)
            except Exception as e:
                logger.error(e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Error")
                msg.setInformativeText("You enter invalid type of value")
                msg.setWindowTitle("Error!")
                msg.exec_()
        else:
            self.fields = []
            buttons = QHBoxLayout()
            button_submit = QPushButton("Submit")
            button_submit.clicked.connect(lambda *args: self.__new_record(True, name))
            button_tag = QComboBox()
            button_tag.addItems([key.capitalize() for key in self.funcs.keys()])

            button_tag.currentIndexChanged.connect(
                lambda *args: self.__new_record(
                    False, str(button_tag.itemText(args[0])).lower()
                )
            )
            buttons.addWidget(button_tag)
            buttons.addWidget(button_submit)
            layout = QVBoxLayout()
            if name is False:
                name = str(button_tag.currentText()).lower()

            for index, field in enumerate(self.funcs[name]["fields"]):
                self.fields.append(QTextEdit())
                layout.addWidget(QLabel(field))
                layout.addWidget(self.fields[-1])

            lay = QVBoxLayout()
            lay.addLayout(buttons)
            lay.addLayout(layout)
            record_layout = QGroupBox()
            record_layout.setLayout(lay)
            self.scroll = QScrollArea()
            self.scroll.setWidget(record_layout)
            self.scroll.setWidgetResizable(True)
            self.window_layout.removeWidget(self.tableWidget)
            self.window_layout.addWidget(self.scroll)


app = QApplication(sys.argv)

logger = logging.getLogger("CLIENT")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/home/maus/bsuir/3/AiPOSiZI/rpc-soap/client/log/out.log")
handler.setFormatter(formatter)
logger.addHandler(handler)
