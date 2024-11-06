# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/30 15:45
# @File    : resourceManage.py
# @Software: PyCharm
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QModelIndex
from PyQt6.QtWidgets import QWidget, QApplication, QAbstractItemView, QSizePolicy, QHeaderView, QTableWidgetItem, \
    QMessageBox

from dao import resourceTypeDao, resourceDao
from entity.resourceModel import Resources


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        # 只显示最小化和关闭按钮
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        # 初始化下拉框
        self.initReTypeListCombobox()
        # 初始化表格
        self.initTable()

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
        self.id_input.setReadOnly(True)
        self.id_input.setStyleSheet("background-color: rgb(238,238,224)")

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
        # 默认选中 男
        self.man_radio.setChecked(True)

        self.femail_redio = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.femail_redio.setGeometry(QtCore.QRect(670, 30, 61, 20))
        self.femail_redio.setObjectName("femail_redio")
        self.modify = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.modify.setGeometry(QtCore.QRect(170, 240, 121, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/update.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.modify.setIcon(icon)
        self.modify.setObjectName("modify")
        # 修改按钮点击时间
        self.modify.clicked.connect(self.update)
        self.delbtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.delbtn.setGeometry(QtCore.QRect(450, 240, 131, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/del.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delbtn.setIcon(icon1)
        self.delbtn.setObjectName("delbtn")
        # 绑定删除按钮
        self.delbtn.clicked.connect(self.delete)
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
        icon2.addPixmap(QtGui.QPixmap("./images/query.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.initTable)

        # 设置行点击时间
        self.re_listtable.clicked.connect(self.initForm)

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

    def initReTypeListCombobox(self):
        """
        初始化下拉框数据
        :return:
        """
        # 获取所有资源类别
        reTypelist = resourceTypeDao.list("")
        self.s_re_combox.addItem("请选择资源类别", -1)
        self.typeCombox.addItem("请选择资源类别", -1)
        for reType in reTypelist:
            self.s_re_combox.addItem(reType[1], reType[0])
            self.typeCombox.addItem(reType[1], reType[0])

    def initTable(self):
        # 获取条件
        name = self.name_input.text()
        author = self.author_input.text()
        reTypeId = self.s_re_combox.currentData()
        RE = Resources(name, author, reTypeId)

        result = resourceDao.list_re(RE)
        row = 0
        if result:
            row = len(result)
        self.re_listtable.setColumnCount(7)
        self.re_listtable.setRowCount(row)
        self.re_listtable.verticalHeader().setVisible(False)  # 影藏行号
        self.re_listtable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.re_listtable.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.re_listtable.setHorizontalHeaderLabels(['编号', '资源名称', '主角', '资源类别', '性别', '价格', '描述'])
        self.re_listtable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.re_listtable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        for i in range(row):
            for j in range(7):
                data = QTableWidgetItem(str(result[i][j]))
                self.re_listtable.setItem(i, j, data)

    def initForm(self, index: QModelIndex):
        """
        初始化Form
        :param index:
        :return:
        """
        rowIndex = index.row()  # 获取行索引
        self.id_input.setText(str(self.re_listtable.item(rowIndex, 0).text()))  # 设置id编号
        self.name_input_2.setText(str(self.re_listtable.item(rowIndex, 1).text()))  # 名称
        self.author_input2.setText(str(self.re_listtable.item(rowIndex, 2).text()))  # 作者
        self.typeCombox.setCurrentText(str(self.re_listtable.item(rowIndex, 3).text()))  # 类别
        if self.re_listtable.item(rowIndex, 4).text() == "男":
            self.man_radio.setChecked(True)
        else:
            self.femail_redio.setChecked(True)
        self.price_input.setText(str(self.re_listtable.item(rowIndex, 5).text()))  # 价格
        self.re_desc.setPlainText(str(self.re_listtable.item(rowIndex, 6).text()))  # 描述

    def retFrom(self):
        self.id_input.setText("")
        self.name_input_2.setText("")
        self.author_input2.setText("")
        self.typeCombox.setCurrentIndex(0)
        self.man_radio.setChecked(True)
        self.price_input.setText("")
        self.re_desc.setPlainText("")

    def update(self):
        """
        修改资源类别信息
        :return:
        """
        id = self.id_input.text()
        if id.strip() == "":
            QMessageBox.warning(self, "警告", "请选中你需要修改的行！")
            return
        rename = self.name_input_2.text()
        if rename.strip() == "":
            QMessageBox.warning(self, "警告", "请输入资源名称！")
            return
        sex = '男'
        if self.femail_redio.isChecked():
            sex = '女'
        price = self.price_input.text()
        if price.strip() == "":
            QMessageBox.warning(self, "警告", "请输入价格！")
            return
        author = self.author_input2.text()
        if author.strip() == "":
            QMessageBox.warning(self, "警告", "请输入主角！")
            return
        re_ty_id = self.typeCombox.currentData()
        if re_ty_id == -1:
            QMessageBox.warning(self, "警告", "请选择资源类别！")
            return
        re_desc = self.re_desc.toPlainText()
        all_re = Resources.my_constructor2(id, rename, author, sex, price, re_ty_id, re_desc)
        print(all_re)
        if resourceDao.update(all_re) > 0:
            QMessageBox.information(self, "提示", "修改成功！")
            self.initTable()
            self.retFrom()
        else:
            QMessageBox.warning(self, "警告", "修改失败！")

    def delete(self):
        """
        删除资源类别信息
        :return:
        """
        id = self.id_input.text()
        if id.strip() == "":
            QMessageBox.warning(self, "警告", "请选中你需要删除的行！")
            return
        reply = QMessageBox.question(self, "确认", "你确定要删除吗？",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # 判断该图书类别下面是否有图书
            if resourceDao.delete(int(id)) > 0:
                QMessageBox.information(self, "提示", "删除成功！")
                self.initTable()
                self.retFrom()
            else:
                QMessageBox.warning(self, "警告", "删除失败！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
