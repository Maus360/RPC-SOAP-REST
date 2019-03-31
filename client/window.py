import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append("../tutorial")
from ttypes import *


class App(QWidget):
    def __init__(self, transport, client_rpc, client_soap):
        super().__init__()
        self.client = client_rpc
        self.client_rpc = client_rpc
        self.client_soap = client_soap.service
        self.transport = transport
        self.title = "Have a nice day!"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.window_layout = QVBoxLayout()
        self.header()
        self.window_layout.addWidget(self.h_box)
        self.setLayout(self.window_layout)

        self.tableWidget = QTableWidget()
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.show()
        sys.exit(app.exec_())

    def header(self):
        self.button_types = QPushButton("Types", self)
        self.button_types.clicked.connect(self.__get_types_all)
        self.button_classes = QPushButton("Classes", self)
        self.button_classes.clicked.connect(self.__get_class_all)
        self.button_mo = QPushButton("Math operations", self)
        self.button_mo.clicked.connect(self.__get_mo_all)
        self.button_protocol = QPushButton("RPC->SOAP", self)
        self.button_protocol.clicked.connect(self.__change_protocol)
        self.h_box = QGroupBox()
        layout = QHBoxLayout()
        layout.addWidget(self.button_classes)
        layout.addWidget(self.button_mo)
        layout.addWidget(self.button_types)
        layout.addWidget(self.button_protocol)
        self.h_box.setLayout(layout)

    def __change_protocol(self):
        if self.client == self.client_rpc:
            self.button_protocol.setText("SOAP->RPC")
            self.client = self.client_soap
        else:
            self.button_protocol.setText("RPC->SOAP")
            self.client = self.client_rpc

    def __get_types_all(self):
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.transport.open()
        result = self.client.get_type_all()
        self.transport.close()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(
            [
                "Name",
                "Min value",
                "Max value",
                "Format",
                "Size",
                "Description",
                # "Edit",
                # "Delete",
            ]
        )
        for index, record in enumerate(result):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(record.name))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(record.min_value))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(record.max_value))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(record.format_of_value))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(record.size)))
            self.tableWidget.setItem(index, 5, QTableWidgetItem(record.description))

            edit_button = QPushButton("Change")
            edit_button.clicked.connect(
                partial(
                    self.__edit_record,
                    "type",
                    record.id,
                    self.tableWidget.item(index, 0),
                    self.tableWidget.item(index, 1),
                    self.tableWidget.item(index, 2),
                    self.tableWidget.item(index, 3),
                    self.tableWidget.item(index, 4),
                    self.tableWidget.item(index, 5),
                )
            )
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(
                partial(self.__delete_record, "type", record.id)
            )
            self.tableWidget.setCellWidget(index, 6, edit_button)
            self.tableWidget.setCellWidget(index, 7, delete_button)

        self.tableWidget.insertRow(len(result))
        self.tableWidget.setItem(len(result), 0, QTableWidgetItem("Enter name"))
        self.tableWidget.setItem(len(result), 1, QTableWidgetItem("Enter min value"))
        self.tableWidget.setItem(len(result), 2, QTableWidgetItem("Enter max value"))
        self.tableWidget.setItem(
            len(result), 3, QTableWidgetItem("Enter format of value")
        )
        self.tableWidget.setItem(len(result), 4, QTableWidgetItem("Enter size"))
        self.tableWidget.setItem(len(result), 5, QTableWidgetItem("Enter decription"))
        new_button = QPushButton("New")
        new_button.clicked.connect(
            partial(
                self.__new_record,
                "type",
                self.tableWidget.item(len(result), 0),
                self.tableWidget.item(len(result), 1),
                self.tableWidget.item(len(result), 2),
                self.tableWidget.item(len(result), 3),
                self.tableWidget.item(len(result), 4),
                self.tableWidget.item(len(result), 5),
            )
        )

        self.tableWidget.setCellWidget(len(result), 6, new_button)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)
        self.window_layout.addWidget(self.tableWidget)

    def __get_class_all(self):
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.transport.open()
        result = self.client.get_class_all()
        self.transport.close()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            [
                "Name",
                "Number of methods",
                "Number of Properties"
                # , "Edit", "Delete"
            ]
        )
        for index, record in enumerate(result):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(record.name))
            self.tableWidget.setItem(
                index, 1, QTableWidgetItem(str(record.num_of_methods))
            )
            self.tableWidget.setItem(
                index, 2, QTableWidgetItem(str(record.num_of_fields))
            )
            edit_button = QPushButton("Change")
            edit_button.clicked.connect(
                partial(
                    self.__edit_record,
                    "class",
                    record.id,
                    self.tableWidget.item(index, 0),
                    self.tableWidget.item(index, 1),
                    self.tableWidget.item(index, 2),
                )
            )
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(
                partial(self.__delete_record, "class", record.id)
            )
            self.tableWidget.setCellWidget(index, 3, edit_button)
            self.tableWidget.setCellWidget(index, 4, delete_button)

        self.tableWidget.insertRow(len(result))
        self.tableWidget.setItem(len(result), 0, QTableWidgetItem("Enter name"))
        self.tableWidget.setItem(
            len(result), 1, QTableWidgetItem("Enter number of methods")
        )
        self.tableWidget.setItem(
            len(result), 2, QTableWidgetItem("Enter number of properties")
        )
        new_button = QPushButton("New")
        new_button.clicked.connect(
            partial(
                self.__new_record,
                "class",
                self.tableWidget.item(len(result), 0),
                self.tableWidget.item(len(result), 1),
                self.tableWidget.item(len(result), 2),
            )
        )

        self.tableWidget.setCellWidget(len(result), 3, new_button)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)
        self.window_layout.addWidget(self.tableWidget)

    def __get_mo_all(self):
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.transport.open()
        result = self.client.get_math_operations_all()
        self.transport.close()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(
            [
                "Name",
                "Type of argument",
                "Type of value",
                "Description",
                # "Edit",
                # "Delete",
            ]
        )
        for index, record in enumerate(result):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(record.name))
            self.tableWidget.setItem(
                index, 1, QTableWidgetItem(record.type_of_argument)
            )
            self.tableWidget.setItem(index, 2, QTableWidgetItem(record.type_of_value))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(record.description))
            edit_button = QPushButton("Change")
            edit_button.clicked.connect(
                partial(
                    self.__edit_record,
                    "mo",
                    record.id,
                    self.tableWidget.item(index, 0),
                    self.tableWidget.item(index, 1),
                    self.tableWidget.item(index, 2),
                    self.tableWidget.item(index, 3),
                )
            )
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(
                partial(self.__delete_record, "mo", record.id)
            )
            self.tableWidget.setCellWidget(index, 4, edit_button)
            self.tableWidget.setCellWidget(index, 5, delete_button)

        self.tableWidget.insertRow(len(result))
        self.tableWidget.setItem(len(result), 0, QTableWidgetItem("Enter name"))
        self.tableWidget.setItem(
            len(result), 1, QTableWidgetItem("Enter type of argument")
        )
        self.tableWidget.setItem(
            len(result), 2, QTableWidgetItem("Enter type of value")
        )
        self.tableWidget.setItem(len(result), 3, QTableWidgetItem("Enter description"))
        new_button = QPushButton("New")
        new_button.clicked.connect(
            partial(
                self.__new_record,
                "mo",
                self.tableWidget.item(len(result), 0),
                self.tableWidget.item(len(result), 1),
                self.tableWidget.item(len(result), 2),
                self.tableWidget.item(len(result), 3),
            )
        )

        self.tableWidget.setCellWidget(len(result), 4, new_button)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)
        self.window_layout.addWidget(self.tableWidget)

    def __edit_record(self, name, iid, *argv):
        print("edit", name, iid, argv)
        funcs = {
            "type": [
                self.client.reset_type,
                self.__get_types_all,
                [str, str, str, str, int, str],
            ],
            "mo": [
                self.client.reset_math_operation,
                self.__get_mo_all,
                [str, str, str, str],
            ],
            "class": [self.client.reset_class, self.__get_class_all, [str, int, int]],
        }
        print(name)
        try:
            argv = [
                funcs[name][2][index](i.text()) for index, i in enumerate(argv[:-1])
            ]
            self.transport.open()
            print(argv)
            funcs[name][0](iid, *argv)
            self.transport.close()
            funcs[name][1]()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("You enter invalid type of value")
            msg.setWindowTitle("Error!")
            msg.exec_()

    def __delete_record(self, name, iid):
        funcs = {
            "type": [self.client.delete_type, self.__get_types_all],
            "mo": [self.client.delete_math_operation, self.__get_mo_all],
            "class": [self.client.delete_class, self.__get_class_all],
        }
        self.transport.open()
        funcs[name][0](iid)
        print("delete", name, iid)
        self.transport.close()
        funcs[name][1]()

    def __new_record(self, name, *argv):
        funcs = {
            "type": [
                self.client.set_type,
                self.__get_types_all,
                [str, str, str, str, int, str],
            ],
            "mo": [
                self.client.set_math_operation,
                self.__get_mo_all,
                [str, str, str, str],
            ],
            "class": [self.client.set_class, self.__get_class_all, [str, int, int]],
        }
        print(name)
        try:
            argv = [
                funcs[name][2][index](i.text()) for index, i in enumerate(argv[:-1])
            ]
            self.transport.open()
            print(argv)
            funcs[name][0](*argv)
            self.transport.close()
            funcs[name][1]()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("You enter invalid type of value")
            msg.setWindowTitle("Error!")
            msg.exec_()


app = QApplication(sys.argv)
