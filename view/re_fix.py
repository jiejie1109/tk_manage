# Form implementation generated from reading ui file 're_fix.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(914, 700)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 400, 801, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(70, 20, 41, 31))
        self.label_7.setObjectName("label_7")
        self.id_input = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.id_input.setGeometry(QtCore.QRect(130, 20, 113, 31))
        self.id_input.setObjectName("id_input")
        self.author_input2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.author_input2.setGeometry(QtCore.QRect(350, 80, 113, 31))
        self.author_input2.setObjectName("author_input2")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(280, 80, 54, 31))
        self.label_8.setObjectName("label_8")
        self.name_input_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.name_input_2.setGeometry(QtCore.QRect(350, 20, 113, 31))
        self.name_input_2.setObjectName("name_input_2")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(280, 20, 54, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(70, 140, 54, 31))
        self.label_10.setObjectName("label_10")
        self.price_input = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.price_input.setGeometry(QtCore.QRect(130, 80, 113, 31))
        self.price_input.setObjectName("price_input")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(70, 80, 54, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(530, 20, 54, 41))
        self.label_12.setObjectName("label_12")
        self.re_desc = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.re_desc.setGeometry(QtCore.QRect(130, 140, 601, 81))
        self.re_desc.setObjectName("re_desc")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(530, 80, 54, 31))
        self.label_13.setObjectName("label_13")
        self.typeCombox = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.typeCombox.setGeometry(QtCore.QRect(590, 80, 141, 31))
        self.typeCombox.setObjectName("typeCombox")
        self.man_radio = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.man_radio.setGeometry(QtCore.QRect(610, 30, 41, 20))
        self.man_radio.setObjectName("man_radio")
        self.femail_redio = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.femail_redio.setGeometry(QtCore.QRect(670, 30, 61, 20))
        self.femail_redio.setObjectName("femail_redio")
        self.modify = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.modify.setGeometry(QtCore.QRect(170, 240, 121, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/update.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.modify.setIcon(icon)
        self.modify.setObjectName("modify")
        self.delbtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.delbtn.setGeometry(QtCore.QRect(450, 240, 131, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/del.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delbtn.setIcon(icon1)
        self.delbtn.setObjectName("delbtn")
        self.re_listtable = QtWidgets.QTableWidget(parent=Form)
        self.re_listtable.setGeometry(QtCore.QRect(50, 120, 801, 271))
        self.re_listtable.setObjectName("re_listtable")
        self.re_listtable.setColumnCount(0)
        self.re_listtable.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 20, 801, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 61, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(270, 30, 41, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(470, 30, 54, 31))
        self.label_6.setObjectName("label_6")
        self.name_input = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.name_input.setGeometry(QtCore.QRect(110, 29, 113, 31))
        self.name_input.setObjectName("name_input")
        self.author_input = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.author_input.setGeometry(QtCore.QRect(320, 29, 113, 31))
        self.author_input.setObjectName("author_input")
        self.s_re_combox = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.s_re_combox.setGeometry(QtCore.QRect(530, 30, 111, 31))
        self.s_re_combox.setObjectName("s_re_combox")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 30, 75, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/query.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "资源信息维护"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.label_7.setText(_translate("Form", "编号："))
        self.label_8.setText(_translate("Form", "主      角："))
        self.label_9.setText(_translate("Form", "资源名称："))
        self.label_10.setText(_translate("Form", "描述："))
        self.label_11.setText(_translate("Form", "价格："))
        self.label_12.setText(_translate("Form", "性     别："))
        self.label_13.setText(_translate("Form", "资源类别："))
        self.man_radio.setText(_translate("Form", "男"))
        self.femail_redio.setText(_translate("Form", "女"))
        self.modify.setText(_translate("Form", "修改"))
        self.delbtn.setText(_translate("Form", "删除"))
        self.groupBox_3.setTitle(_translate("Form", "查询操作"))
        self.label_4.setText(_translate("Form", "资源名称："))
        self.label_5.setText(_translate("Form", "主角："))
        self.label_6.setText(_translate("Form", "资源类别："))
        self.pushButton_2.setText(_translate("Form", "查询"))