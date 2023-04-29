# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.9
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(836, 719)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nameEdit = QLineEdit(Form)
        self.nameEdit.setObjectName(u"nameEdit")

        self.horizontalLayout.addWidget(self.nameEdit)

        self.searchCustomerButton = QPushButton(Form)
        self.searchCustomerButton.setObjectName(u"searchCustomerButton")
        font = QFont()
        font.setPointSize(11)
        self.searchCustomerButton.setFont(font)

        self.horizontalLayout.addWidget(self.searchCustomerButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.newCustomerButton = QPushButton(Form)
        self.newCustomerButton.setObjectName(u"newCustomerButton")
        self.newCustomerButton.setFont(font)

        self.horizontalLayout.addWidget(self.newCustomerButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.customerView = QTreeView(Form)
        self.customerView.setObjectName(u"customerView")

        self.verticalLayout.addWidget(self.customerView)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.outstandingInvoicesView = QTreeView(Form)
        self.outstandingInvoicesView.setObjectName(u"outstandingInvoicesView")

        self.verticalLayout.addWidget(self.outstandingInvoicesView)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.invoiceNoEdit = QLineEdit(Form)
        self.invoiceNoEdit.setObjectName(u"invoiceNoEdit")

        self.horizontalLayout_2.addWidget(self.invoiceNoEdit)

        self.searchInvoiceButton = QPushButton(Form)
        self.searchInvoiceButton.setObjectName(u"searchInvoiceButton")
        self.searchInvoiceButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.searchInvoiceButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.settingsButton = QPushButton(Form)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.settingsButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Navn p\u00e5 kunde", None))
        self.searchCustomerButton.setText(QCoreApplication.translate("Form", u"Kundes\u00f8k", None))
        self.newCustomerButton.setText(QCoreApplication.translate("Form", u"Ny kunde", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kundeliste", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Utest\u00e5ende fakturaer", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Hent gammel faktura", None))
        self.invoiceNoEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Fakturanummer", None))
        self.searchInvoiceButton.setText(QCoreApplication.translate("Form", u"Nummers\u00f8k", None))
        self.settingsButton.setText(QCoreApplication.translate("Form", u"Innstillinger", None))
    # retranslateUi

