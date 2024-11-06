import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget

from dao import userDao
from entity.UserModel import User


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        # 只显示最小化和关闭按钮
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 315)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 251, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.username = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.username.setText(userDao.current_user.username)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.username)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.oldpwd = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.oldpwd.setObjectName("oldpwd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.oldpwd)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.newpwd = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.newpwd.setObjectName("newpwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newpwd)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.newpwd2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.newpwd2.setObjectName("newpwd2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newpwd2)
        self.subbtn = QtWidgets.QPushButton(parent=Form)
        self.subbtn.setGeometry(QtCore.QRect(130, 270, 75, 24))
        self.subbtn.setObjectName("subbtn")
        self.subbtn.clicked.connect(self.modifyPwd)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改密码"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "原密码："))
        self.label_4.setText(_translate("Form", "新密码："))
        self.label_5.setText(_translate("Form", "确认密码："))
        self.subbtn.setText(_translate("Form", "提交"))

    def modifyPwd(self):
        """
        修改密码
        :return:
        """
        userName = self.username.text()
        oldPwd = self.oldpwd.text()
        newPwd = self.newpwd.text()
        newPwd2 = self.newpwd2.text()
        if oldPwd.strip() == "":
            QtWidgets.QMessageBox.information(None, "提示", "请输入原密码")
            return
        # 判断原密码是否正确
        if oldPwd != userDao.current_user.password:
            QtWidgets.QMessageBox.information(None, "提示", "原密码不正确")
            return
        if newPwd.strip() == "":
            QtWidgets.QMessageBox.information(None, "提示", "请输入新密码")
            return
        if newPwd2.strip() == "":
            QtWidgets.QMessageBox.information(None, "提示", "请再次输入新密码")
            return
        if newPwd != newPwd2:
            QtWidgets.QMessageBox.information(None, "提示", "两次输入的密码不一致")
            return
        user = User.my_constructor(userName, oldPwd, newPwd)
        if userDao.modifyPassword(user) > 0:
            QtWidgets.QMessageBox.information(None, "提示", "密码修改成功")
            self.restfrom()
        else:
            QtWidgets.QMessageBox.information(None, "提示", "密码修改失败")

    def restfrom(self):
        self.oldpwd.setText("")
        self.newpwd.setText("")
        self.newpwd2.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
