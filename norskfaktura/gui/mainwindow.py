#!/usr/bin/python


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QWidget,
)
from PySide2.QtGui import QPalette, QColor

from PySide2.QtUiTools import QUiLoader


from generated import mainframe
class MainView(QWidget, mainframe.Ui_Form):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)


from generated import customerframe
class CustomerView(QWidget, customerframe.Ui_Form):
    def __init__(self, mainwindow):
        super(CustomerView, self).__init__()
        self.setupUi(self)
        self.parent = mainwindow

        self.backButton.clicked.connect(self.on_back_clicked)

    def on_back_clicked(self):
        self.parent.to_main_view()

from generated import settingsframe
class SettingsView(QWidget, settingsframe.Ui_Form):
    def __init__(self, mainwindow):
        super(SettingsView, self).__init__()
        self.setupUi(self)
        self.parent = mainwindow

        self.cancelButton.clicked.connect(self.on_cancel_clicked)

    def on_cancel_clicked(self):
        self.parent.to_main_view()

from generated import invoiceframe
class InvoiceView(QWidget, invoiceframe.Ui_Form):
    def __init__(self, mainwindow):
        super(InvoiceView, self).__init__()
        self.setupUi(self)
        self.parent = mainwindow

        self.cancelButton.clicked.connect(self.on_cancel_clicked)

    def on_cancel_clicked(self):
        self.parent.to_main_view()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.layout = QStackedLayout()

        self.mainView = MainView()
        self.layout.addWidget(self.mainView)

        self.customerView = CustomerView(self)
        self.layout.addWidget(self.customerView)

        self.settingsView = SettingsView(self)
        self.layout.addWidget(self.settingsView)

        self.invoiceView = InvoiceView(self)
        self.layout.addWidget(self.invoiceView)

        self.layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


        # main window signals
        self.mainView.newCustomerButton.clicked.connect(self.to_customer_view)
        self.mainView.settingsButton.clicked.connect(self.to_settings_view)

        # temporary
        self.mainView.searchInvoiceButton.clicked.connect(self.to_invoice_view)


    def to_main_view(self):
        self.layout.setCurrentIndex(0)

    def to_customer_view(self):
        self.layout.setCurrentIndex(1)

    def to_settings_view(self):
        self.layout.setCurrentIndex(2)

    def to_invoice_view(self):
        self.layout.setCurrentIndex(3)

def show_main_window():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__=="__main__":
    show_main_window()


