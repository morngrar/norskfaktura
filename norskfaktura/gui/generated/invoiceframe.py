# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice.ui'
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
        Form.resize(843, 763)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, 225, -1)
        self.nameLabel = QLabel(Form)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setPointSize(14)
        self.nameLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.nameLabel)

        self.orgNoLabel = QLabel(Form)
        self.orgNoLabel.setObjectName(u"orgNoLabel")
        self.orgNoLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.orgNoLabel)

        self.addressLabel1 = QLabel(Form)
        self.addressLabel1.setObjectName(u"addressLabel1")
        font1 = QFont()
        font1.setPointSize(12)
        self.addressLabel1.setFont(font1)

        self.verticalLayout_3.addWidget(self.addressLabel1)

        self.addressLabel2 = QLabel(Form)
        self.addressLabel2.setObjectName(u"addressLabel2")
        self.addressLabel2.setFont(font1)

        self.verticalLayout_3.addWidget(self.addressLabel2)

        self.addressLabel3 = QLabel(Form)
        self.addressLabel3.setObjectName(u"addressLabel3")
        self.addressLabel3.setFont(font1)

        self.verticalLayout_3.addWidget(self.addressLabel3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        self.groupBox.setFont(font2)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(9)
        self.label.setFont(font3)

        self.verticalLayout_2.addWidget(self.label)

        self.deliveryDateEdit = QLineEdit(self.groupBox)
        self.deliveryDateEdit.setObjectName(u"deliveryDateEdit")
        self.deliveryDateEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.deliveryDateEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_2)

        self.deliveryAddressEdit1 = QLineEdit(self.groupBox)
        self.deliveryAddressEdit1.setObjectName(u"deliveryAddressEdit1")

        self.verticalLayout_2.addWidget(self.deliveryAddressEdit1)

        self.deliveryAddressEdit2 = QLineEdit(self.groupBox)
        self.deliveryAddressEdit2.setObjectName(u"deliveryAddressEdit2")

        self.verticalLayout_2.addWidget(self.deliveryAddressEdit2)

        self.deliveryAddressEdit3 = QLineEdit(self.groupBox)
        self.deliveryAddressEdit3.setObjectName(u"deliveryAddressEdit3")

        self.verticalLayout_2.addWidget(self.deliveryAddressEdit3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.calendarWidget = QCalendarWidget(self.groupBox)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setFont(font3)
        self.calendarWidget.setLocale(QLocale(QLocale.NorwegianBokmal, QLocale.Norway))

        self.horizontalLayout_2.addWidget(self.calendarWidget)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.messageEdit = QLineEdit(Form)
        self.messageEdit.setObjectName(u"messageEdit")

        self.horizontalLayout_4.addWidget(self.messageEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rowView = QTreeView(Form)
        self.rowView.setObjectName(u"rowView")

        self.verticalLayout_6.addWidget(self.rowView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.daysToDueEdit = QLineEdit(Form)
        self.daysToDueEdit.setObjectName(u"daysToDueEdit")

        self.horizontalLayout_6.addWidget(self.daysToDueEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.alreadyPaidByCustomerEdit = QLineEdit(Form)
        self.alreadyPaidByCustomerEdit.setObjectName(u"alreadyPaidByCustomerEdit")

        self.horizontalLayout_7.addWidget(self.alreadyPaidByCustomerEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.vatLabel = QLabel(Form)
        self.vatLabel.setObjectName(u"vatLabel")
        self.vatLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.vatLabel)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.label_14.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_14)

        self.totalLabel = QLabel(Form)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setFont(font4)
        self.totalLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.totalLabel)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_12.addWidget(self.label_15)

        self.descriptionEdit = QLineEdit(Form)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(250)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.descriptionEdit.sizePolicy().hasHeightForWidth())
        self.descriptionEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_12.addWidget(self.descriptionEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_11.addWidget(self.label_16)

        self.priceEdit = QLineEdit(Form)
        self.priceEdit.setObjectName(u"priceEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.priceEdit.sizePolicy().hasHeightForWidth())
        self.priceEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.priceEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_10.addWidget(self.label_17)

        self.amountEdit = QLineEdit(Form)
        self.amountEdit.setObjectName(u"amountEdit")
        sizePolicy2.setHeightForWidth(self.amountEdit.sizePolicy().hasHeightForWidth())
        self.amountEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.amountEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)

        self.discountPercentageEdit = QLineEdit(Form)
        self.discountPercentageEdit.setObjectName(u"discountPercentageEdit")
        sizePolicy2.setHeightForWidth(self.discountPercentageEdit.sizePolicy().hasHeightForWidth())
        self.discountPercentageEdit.setSizePolicy(sizePolicy2)
        self.discountPercentageEdit.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_9.addWidget(self.discountPercentageEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_8.addWidget(self.label_19)

        self.vatPercentageEdit = QLineEdit(Form)
        self.vatPercentageEdit.setObjectName(u"vatPercentageEdit")
        sizePolicy2.setHeightForWidth(self.vatPercentageEdit.sizePolicy().hasHeightForWidth())
        self.vatPercentageEdit.setSizePolicy(sizePolicy2)
        self.vatPercentageEdit.setMaximumSize(QSize(60, 300))

        self.verticalLayout_8.addWidget(self.vatPercentageEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)

        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 3)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.postButton = QPushButton(Form)
        self.postButton.setObjectName(u"postButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.postButton.sizePolicy().hasHeightForWidth())
        self.postButton.setSizePolicy(sizePolicy3)
        self.postButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.postButton)

        self.payButton = QPushButton(Form)
        self.payButton.setObjectName(u"payButton")
        sizePolicy3.setHeightForWidth(self.payButton.sizePolicy().hasHeightForWidth())
        self.payButton.setSizePolicy(sizePolicy3)
        self.payButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.payButton)

        self.createPDFButton = QPushButton(Form)
        self.createPDFButton.setObjectName(u"createPDFButton")
        sizePolicy3.setHeightForWidth(self.createPDFButton.sizePolicy().hasHeightForWidth())
        self.createPDFButton.setSizePolicy(sizePolicy3)
        self.createPDFButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.createPDFButton)

        self.createCreditNoteButton = QPushButton(Form)
        self.createCreditNoteButton.setObjectName(u"createCreditNoteButton")
        sizePolicy3.setHeightForWidth(self.createCreditNoteButton.sizePolicy().hasHeightForWidth())
        self.createCreditNoteButton.setSizePolicy(sizePolicy3)
        self.createCreditNoteButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.createCreditNoteButton)

        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy3.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy3)
        self.cancelButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.cancelButton)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.removeRowButton = QPushButton(Form)
        self.removeRowButton.setObjectName(u"removeRowButton")
        sizePolicy3.setHeightForWidth(self.removeRowButton.sizePolicy().hasHeightForWidth())
        self.removeRowButton.setSizePolicy(sizePolicy3)
        self.removeRowButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.removeRowButton)

        self.addRowButton = QPushButton(Form)
        self.addRowButton.setObjectName(u"addRowButton")
        sizePolicy3.setHeightForWidth(self.addRowButton.sizePolicy().hasHeightForWidth())
        self.addRowButton.setSizePolicy(sizePolicy3)
        self.addRowButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.addRowButton)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"Navn", None))
        self.orgNoLabel.setText(QCoreApplication.translate("Form", u"Org. nr.", None))
        self.addressLabel1.setText(QCoreApplication.translate("Form", u"adresse 1", None))
        self.addressLabel2.setText(QCoreApplication.translate("Form", u"adresse 2", None))
        self.addressLabel3.setText(QCoreApplication.translate("Form", u"adresse 3", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Leveranseinfo", None))
        self.label.setText(QCoreApplication.translate("Form", u"Leveringsdato", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Adresse", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Melding:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Antall dager til forfall:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Allerede betalt av kunde:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Herav Mva:", None))
        self.vatLabel.setText(QCoreApplication.translate("Form", u"0,00", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Totalt:", None))
        self.totalLabel.setText(QCoreApplication.translate("Form", u"0,00", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Beskrivelse", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Pris", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Antall", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Rabatt %", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Mva %", None))
        self.postButton.setText(QCoreApplication.translate("Form", u"Post\u00e9r", None))
        self.payButton.setText(QCoreApplication.translate("Form", u"Betal", None))
        self.createPDFButton.setText(QCoreApplication.translate("Form", u"Lag PDF", None))
        self.createCreditNoteButton.setText(QCoreApplication.translate("Form", u"Lag Kreditnota", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Avbryt", None))
        self.removeRowButton.setText(QCoreApplication.translate("Form", u"Fjern valgt rad", None))
        self.addRowButton.setText(QCoreApplication.translate("Form", u"Legg til", None))
    # retranslateUi

