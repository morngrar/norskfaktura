# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer.ui'
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
        Form.resize(767, 684)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameEdit = QLineEdit(Form)
        self.nameEdit.setObjectName(u"nameEdit")

        self.verticalLayout_2.addWidget(self.nameEdit)

        self.orgNoEdit = QLineEdit(Form)
        self.orgNoEdit.setObjectName(u"orgNoEdit")

        self.verticalLayout_2.addWidget(self.orgNoEdit)

        self.addressEdit1 = QLineEdit(Form)
        self.addressEdit1.setObjectName(u"addressEdit1")

        self.verticalLayout_2.addWidget(self.addressEdit1)

        self.addressEdit2 = QLineEdit(Form)
        self.addressEdit2.setObjectName(u"addressEdit2")

        self.verticalLayout_2.addWidget(self.addressEdit2)

        self.addressEdit3 = QLineEdit(Form)
        self.addressEdit3.setObjectName(u"addressEdit3")

        self.verticalLayout_2.addWidget(self.addressEdit3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 3, -1, 3)
        self.newInvoiceButton = QPushButton(Form)
        self.newInvoiceButton.setObjectName(u"newInvoiceButton")
        self.newInvoiceButton.setEnabled(False)

        self.verticalLayout_3.addWidget(self.newInvoiceButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_7.addWidget(self.saveButton)

        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout_7.addWidget(self.backButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 7)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Navn:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Org. nr. (om aktuelt):", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Adresse:", None))
        self.label_9.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Postnr. og sted:", None))
        self.newInvoiceButton.setText(QCoreApplication.translate("Form", u"Ny Faktura", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Lagre", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"Tilbake", None))
    # retranslateUi

