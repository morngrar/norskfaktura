# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
        Form.resize(913, 654)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nameEdit = QLineEdit(Form)
        self.nameEdit.setObjectName(u"nameEdit")

        self.verticalLayout_3.addWidget(self.nameEdit)

        self.orgNoEdit = QLineEdit(Form)
        self.orgNoEdit.setObjectName(u"orgNoEdit")

        self.verticalLayout_3.addWidget(self.orgNoEdit)

        self.phoneEdit = QLineEdit(Form)
        self.phoneEdit.setObjectName(u"phoneEdit")

        self.verticalLayout_3.addWidget(self.phoneEdit)

        self.emailEdit = QLineEdit(Form)
        self.emailEdit.setObjectName(u"emailEdit")

        self.verticalLayout_3.addWidget(self.emailEdit)

        self.websideEdit = QLineEdit(Form)
        self.websideEdit.setObjectName(u"websideEdit")

        self.verticalLayout_3.addWidget(self.websideEdit)

        self.addressEdit1 = QLineEdit(Form)
        self.addressEdit1.setObjectName(u"addressEdit1")

        self.verticalLayout_3.addWidget(self.addressEdit1)

        self.addressEdit2 = QLineEdit(Form)
        self.addressEdit2.setObjectName(u"addressEdit2")

        self.verticalLayout_3.addWidget(self.addressEdit2)

        self.addressEdit3 = QLineEdit(Form)
        self.addressEdit3.setObjectName(u"addressEdit3")

        self.verticalLayout_3.addWidget(self.addressEdit3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, -1, -1, -1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.vatRegisteredCheckBox = QCheckBox(Form)
        self.vatRegisteredCheckBox.setObjectName(u"vatRegisteredCheckBox")

        self.gridLayout.addWidget(self.vatRegisteredCheckBox, 2, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dueInDaysEdit = QLineEdit(Form)
        self.dueInDaysEdit.setObjectName(u"dueInDaysEdit")

        self.gridLayout.addWidget(self.dueInDaysEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.firstInvoiceNoEdit = QLineEdit(Form)
        self.firstInvoiceNoEdit.setObjectName(u"firstInvoiceNoEdit")

        self.gridLayout.addWidget(self.firstInvoiceNoEdit, 3, 1, 1, 1)

        self.logoPathEdit = QLineEdit(Form)
        self.logoPathEdit.setObjectName(u"logoPathEdit")

        self.gridLayout.addWidget(self.logoPathEdit, 5, 1, 1, 2)

        self.logoOpenButton = QPushButton(Form)
        self.logoOpenButton.setObjectName(u"logoOpenButton")
        self.logoOpenButton.setFont(font)

        self.gridLayout.addWidget(self.logoOpenButton, 5, 3, 1, 1)

        self.pdfOpenButton = QPushButton(Form)
        self.pdfOpenButton.setObjectName(u"pdfOpenButton")
        self.pdfOpenButton.setFont(font)

        self.gridLayout.addWidget(self.pdfOpenButton, 6, 3, 1, 1)

        self.pdfDirEdit = QLineEdit(Form)
        self.pdfDirEdit.setObjectName(u"pdfDirEdit")

        self.gridLayout.addWidget(self.pdfDirEdit, 6, 1, 1, 2)

        self.accountNoEdit = QLineEdit(Form)
        self.accountNoEdit.setObjectName(u"accountNoEdit")

        self.gridLayout.addWidget(self.accountNoEdit, 0, 1, 1, 3)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 15, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        font1 = QFont()
        font1.setPointSize(11)
        self.saveButton.setFont(font1)

        self.horizontalLayout_9.addWidget(self.saveButton)

        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setFont(font1)

        self.horizontalLayout_9.addWidget(self.cancelButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Navn:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Org. nr. (om aktuelt):", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Telefon:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Epost:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Nettside:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Adresse:", None))
        self.label_14.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Postnr. og sted:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Betalingsfrist:", None))
        self.vatRegisteredCheckBox.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Mva-registrert:", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Logo:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"PDF-mappe:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"dager", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kontonummer:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"F\u00f8rste fakturanr:", None))
        self.logoOpenButton.setText(QCoreApplication.translate("Form", u"\u00c5pne", None))
        self.pdfOpenButton.setText(QCoreApplication.translate("Form", u"\u00c5pne", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Lagre", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Avbryt", None))
    # retranslateUi

