# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/24 15:17
# @File    : login.py
# @Software: PyCharm
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox

import main
from dao import userDao
from entity.UserModel import User


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 100, 251, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.username_input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.username_input.setObjectName("username_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.username_input)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.password_input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password_input)
        self.logbtn = QtWidgets.QPushButton(parent=Form)
        self.logbtn.setGeometry(QtCore.QRect(90, 230, 75, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/login.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logbtn.setIcon(icon)
        self.logbtn.setObjectName("logbtn")

        # 登录按钮绑定点击事件
        self.logbtn.clicked.connect(self.login)

        self.resetbtn = QtWidgets.QPushButton(parent=Form)
        self.resetbtn.setGeometry(QtCore.QRect(210, 230, 75, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/re.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.resetbtn.setIcon(icon1)
        self.resetbtn.setObjectName("resetbtn")
        # 重置按钮绑定方法
        self.resetbtn.clicked.connect(self.restFrom)

        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(140, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(60, 10, 81, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员登录"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密    码："))
        self.logbtn.setText(_translate("Form", "登录"))
        self.resetbtn.setText(_translate("Form", "重置"))
        self.label_3.setText(_translate("Form", "资源管理系统"))

    def restFrom(self):
        self.username_input.clear()
        self.password_input.clear()

    def login(self):
        """
        用户登录判断 数据库判断成功则打开主窗体，否则提示报错信息
        :return:
        """
        username = self.username_input.text()
        password = self.password_input.text()
        print(username, password)
        if username.strip() == "" or password.strip() == "":
            QMessageBox.warning(None, "提示", "用户名或密码不能为空！")
        else:
            user = User(username, password)
            resultUser = userDao.login(user)  # resultUser 这里返回的是元组类型 不能作为指定username 返回 要报错
            if resultUser:
                print("登录成功")
                userDao.current_user = user
                # 实例化主窗体
                self.m = main.Ui_MainWindow()
                self.m.show()
                self.hide()  # 影藏主窗体
            else:
                QMessageBox.warning(None, "提示", "用户名密码错误！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
