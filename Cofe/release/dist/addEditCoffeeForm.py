# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAdd(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 401, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 2, 1, 1)
        self.status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 2, 0, 1, 1)
        self.url = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.url.setObjectName("url")
        self.gridLayout.addWidget(self.url, 3, 2, 1, 1)
        self.lable_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lable_2.setObjectName("lable_2")
        self.gridLayout.addWidget(self.lable_2, 3, 0, 1, 1)
        self.deef = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.deef.setObjectName("deef")
        self.gridLayout.addWidget(self.deef, 1, 2, 1, 1)
        self.lable_s = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lable_s.setObjectName("lable_s")
        self.gridLayout.addWidget(self.lable_s, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 1)
        self.lflf = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lflf.setObjectName("lflf")
        self.gridLayout.addWidget(self.lflf, 0, 0, 1, 1)
        self.lable = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lable.setObjectName("lable")
        self.gridLayout.addWidget(self.lable, 4, 0, 1, 1)
        self.price = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 5, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.status.setText(_translate("Form", "В зернах"))
        self.lable_2.setText(_translate("Form", "Описание url"))
        self.lable_s.setText(_translate("Form", "Обжарка"))
        self.comboBox.setItemText(0, _translate("Form", "true"))
        self.comboBox.setItemText(1, _translate("Form", "false"))
        self.lflf.setText(_translate("Form", "Название"))
        self.lable.setText(_translate("Form", "Цена"))
        self.label.setText(_translate("Form", "Объем"))
        self.pushButton.setText(_translate("Form", "Изменть"))
