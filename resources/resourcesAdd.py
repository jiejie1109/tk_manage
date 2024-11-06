# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/30 9:30
# @File    : resourcesAdd.py
# @Software: PyCharm
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox

from dao import resourceDao, resourceTypeDao
from entity.resourceModel import Resources


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        # 只显示最小化和关闭按钮
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 486)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(80, 70, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(330, 70, 54, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(330, 130, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(80, 190, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(80, 130, 61, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(80, 250, 54, 16))
        self.label_6.setObjectName("label_6")
        self.reTypecomboBox = QtWidgets.QComboBox(parent=Form)
        self.reTypecomboBox.setGeometry(QtCore.QRect(140, 180, 161, 31))
        self.reTypecomboBox.setObjectName("reTypecomboBox")

        # 初始化完调用方法
        self.initReTypeListCombobox()

        self.ReNameInpute = QtWidgets.QLineEdit(parent=Form)
        self.ReNameInpute.setGeometry(QtCore.QRect(140, 70, 161, 31))
        self.ReNameInpute.setObjectName("ReNameInpute")
        self.reDescInput = QtWidgets.QPlainTextEdit(parent=Form)
        self.reDescInput.setGeometry(QtCore.QRect(140, 250, 441, 111))
        self.reDescInput.setObjectName("reDescInput")
        self.manradio = QtWidgets.QRadioButton(parent=Form)
        self.manradio.setGeometry(QtCore.QRect(150, 130, 61, 31))
        self.manradio.setObjectName("manradio")

        # 设置默认值
        self.manradio.setChecked(True)

        self.femaleradio = QtWidgets.QRadioButton(parent=Form)
        self.femaleradio.setGeometry(QtCore.QRect(230, 130, 51, 31))
        self.femaleradio.setObjectName("femaleradio")
        self.addbtn = QtWidgets.QPushButton(parent=Form)
        self.addbtn.setGeometry(QtCore.QRect(180, 400, 75, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addbtn.setIcon(icon)
        self.addbtn.setObjectName("addbtn")

        # 绑定事件
        self.addbtn.clicked.connect(self.add)

        self.resetbtn = QtWidgets.QPushButton(parent=Form)
        self.resetbtn.setGeometry(QtCore.QRect(370, 400, 75, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/re.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.resetbtn.setIcon(icon1)
        self.resetbtn.setObjectName("resetbtn")

        self.resetbtn.clicked.connect(self.reset)

        self.AuthorInpute = QtWidgets.QLineEdit(parent=Form)
        self.AuthorInpute.setGeometry(QtCore.QRect(380, 70, 191, 31))
        self.AuthorInpute.setObjectName("AuthorInpute")
        self.priceInput = QtWidgets.QLineEdit(parent=Form)
        self.priceInput.setGeometry(QtCore.QRect(380, 130, 191, 31))
        self.priceInput.setObjectName("priceInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "资源信息添加"))
        self.label.setText(_translate("Form", "资源名称："))
        self.label_2.setText(_translate("Form", "主角："))
        self.label_3.setText(_translate("Form", "价格："))
        self.label_4.setText(_translate("Form", "资源类别："))
        self.label_5.setText(_translate("Form", "性      别："))
        self.label_6.setText(_translate("Form", "资源描述："))
        self.manradio.setText(_translate("Form", "男"))
        self.femaleradio.setText(_translate("Form", "女"))
        self.addbtn.setText(_translate("Form", "添加"))
        self.resetbtn.setText(_translate("Form", "重置"))

    def initReTypeListCombobox(self):
        """
        初始化下拉框数据
        :return:
        """
        # 获取所有资源类别
        reTypelist = resourceTypeDao.list("")
        print(reTypelist)
        self.reTypecomboBox.addItem("请选择资源类别", -1)
        for reType in reTypelist:
            self.reTypecomboBox.addItem(reType[1], reType[0])

    def add(self):
        """
        添加资源信息
        :return:
        """
        ReName = self.ReNameInpute.text()
        if ReName.strip() == "":
            QMessageBox.warning(None, "警告", "资源名称不能为空")
            return
        author = self.AuthorInpute.text()
        if author.strip() == "":
            QMessageBox.warning(None, "警告", "主角不能为空")
            return

        sex = ""
        if self.manradio.isChecked():
            sex = "男"
        else:
            sex = "女"

        price = self.priceInput.text()
        if price.strip() == "":
            QMessageBox.warning(None, "警告", "价格不能为空")
            return

        reTypeId = self.reTypecomboBox.currentData()
        if reTypeId == -1:
            QMessageBox.warning(None, "警告", "请选择资源类别")
            return
        reDesc = self.reDescInput.toPlainText()
        all_re = Resources.my_constructor(ReName, author, sex, price, reTypeId, reDesc)
        if resourceDao.add(all_re) > 0:
            QMessageBox.information(None, "提示", "添加成功")
            self.reset()
        else:
            QMessageBox.warning(None, "警告", "添加失败")

    def reset(self):
        self.ReNameInpute.setText("")
        self.AuthorInpute.setText("")
        self.priceInput.setText("")
        self.reDescInput.setPlainText("")
        self.manradio.setChecked(True)
        self.reTypecomboBox.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
