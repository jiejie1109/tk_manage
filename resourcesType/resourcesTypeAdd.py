# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/29 9:17
# @File    : resourcesTypeAdd.py
# @Software: PyCharm
# 资源类别添加模块
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox

from entity.resourcesTypeModel import ResourcesType
from dao import resourceTypeDao


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        # 只显示最小化和关闭按钮
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(475, 275)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 20, 361, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.TypeNameInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.TypeNameInput.setObjectName("TypeNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TypeNameInput)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.TypeNameDesc = QtWidgets.QPlainTextEdit(parent=self.formLayoutWidget)
        self.TypeNameDesc.setObjectName("TypeNameDesc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TypeNameDesc)
        self.addBtn = QtWidgets.QPushButton(parent=Form)
        self.addBtn.setGeometry(QtCore.QRect(100, 220, 75, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setObjectName("addBtn")

        # 添加按钮绑定事件
        self.addBtn.clicked.connect(self.add)

        self.restBtm = QtWidgets.QPushButton(parent=Form)
        self.restBtm.setGeometry(QtCore.QRect(280, 220, 75, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/re.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restBtm.setIcon(icon1)
        self.restBtm.setObjectName("restBtm")

        # 绑定重置按钮
        self.restBtm.clicked.connect(self.reset)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "资源类别添加"))
        self.label.setText(_translate("Form", "资源类别名称："))
        self.label_2.setText(_translate("Form", "资源类别描述："))
        self.addBtn.setText(_translate("Form", "添加"))
        self.restBtm.setText(_translate("Form", "重置"))

    def reset(self):
        """
        重置按钮
        :return:
        """
        self.TypeNameInput.clear()
        self.TypeNameDesc.clear()

    def add(self):
        """
        添加资源类别
        :return:
        """
        TypeName = self.TypeNameInput.text()
        TypeDesc = self.TypeNameDesc.toPlainText()
        if TypeName.strip() == "":
            QMessageBox.warning(None, "警告", "资源类别名称不能为空")
        else:
            resourcesType = ResourcesType(TypeName, TypeDesc)
            if resourceTypeDao.add(resourcesType) > 0:
                QMessageBox.information(None, "提示", "添加成功")
                self.reset()
            else:
                QMessageBox.warning(None, "警告", "添加失败")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
