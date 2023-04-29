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

WINDOW_TITLE = "Norsk Faktura"


if __name__=="__main__": # fix local import path when running *this* file
    from generated import mainframe
else:
    from gui.generated import mainframe
class MainView(QWidget, mainframe.Ui_Form):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)


if __name__=="__main__": # fix local import path when running *this* file
    from generated import customerframe
else:
    from gui.generated import customerframe
class CustomerView(QWidget, customerframe.Ui_Form):
    def __init__(self, mainwindow):
        super(CustomerView, self).__init__()
        self.setupUi(self)
        self.parent = mainwindow

        self.backButton.clicked.connect(self.on_back_clicked)

    def on_back_clicked(self):
        self.parent.to_main_view()

if __name__=="__main__": # fix local import path when running *this* file
    from generated import settingsframe
else:
    from gui.generated import settingsframe
class SettingsView(QWidget, settingsframe.Ui_Form):
    def __init__(self, mainwindow):
        super(SettingsView, self).__init__()
        self.setupUi(self)
        self.parent = mainwindow

        self.cancelButton.clicked.connect(self.on_cancel_clicked)

    def on_cancel_clicked(self):
        self.parent.to_main_view()

if __name__=="__main__": # fix local import path when running *this* file
    from generated import invoiceframe
else:
    from gui.generated import invoiceframe
class InvoiceView(QWidget, invoiceframe.Ui_Form):
    def __init__(self, mainwindow):
        super(InvoiceView, self).__init__()
        self.setupUi(self)
        self.parent = mainwindow

        self.cancelButton.clicked.connect(self.on_cancel_clicked)

    def on_cancel_clicked(self):
        self.parent.to_main_view()


# MAIN CONTROLLER

class MainWindow(QMainWindow):
    """Main window of the application.

    This is the window which holds most of the applications 'views', which
    are simply boxes which contain widgets and layouts and functionality.
    The main window remains the same, and the child views are switched out
    as the user navigates between them.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)

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


