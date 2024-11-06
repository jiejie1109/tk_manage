# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/29 11:17
# @File    : resourceTypeManage.py
# @Software: PyCharm
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QModelIndex
from PyQt6.QtWidgets import QWidget, QApplication, QAbstractItemView, QSizePolicy, QHeaderView, QTableWidgetItem, \
    QMessageBox

from dao import resourceTypeDao, resourceDao
from entity.resourcesTypeModel import ResourcesType


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        # 只显示最小化和关闭按钮
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.initTable()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(685, 575)
        self.resourceTpyetable = QtWidgets.QTableWidget(parent=Form)
        self.resourceTpyetable.setGeometry(QtCore.QRect(60, 110, 561, 191))
        self.resourceTpyetable.setObjectName("resourceTpyetable")
        self.resourceTpyetable.setColumnCount(0)
        self.resourceTpyetable.setRowCount(0)

        # 绑定行点击事件获取行数据
        self.resourceTpyetable.itemClicked.connect(self.initForm)

        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(60, 20, 561, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 131, 31))
        self.label.setObjectName("label")
        self.s_resourceTpyeNameInpute = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_resourceTpyeNameInpute.setGeometry(QtCore.QRect(140, 30, 191, 31))
        self.s_resourceTpyeNameInpute.setObjectName("s_resourceTpyeNameInpute")
        self.searchBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.searchBtn.setGeometry(QtCore.QRect(400, 30, 81, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/query.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setObjectName("searchBtn")

        # 绑定按钮
        self.searchBtn.clicked.connect(self.initTable)

        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 310, 561, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 25, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(270, 20, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 41, 16))
        self.label_4.setObjectName("label_4")
        self.idinpute = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.idinpute.setGeometry(QtCore.QRect(80, 19, 91, 31))
        self.idinpute.setObjectName("idinpute")
        # 设置id只读
        self.idinpute.setReadOnly(True)
        self.idinpute.setStyleSheet("background-color: rgb(238,238,224)")

        self.resourceNameTypeinput = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.resourceNameTypeinput.setGeometry(QtCore.QRect(360, 19, 131, 31))
        self.resourceNameTypeinput.setObjectName("resourceNameTypeinput")
        self.resourceTypeNameDesc = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.resourceTypeNameDesc.setGeometry(QtCore.QRect(80, 70, 411, 91))
        self.resourceTypeNameDesc.setObjectName("resourceTypeNameDesc")
        self.updatebtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.updatebtn.setGeometry(QtCore.QRect(120, 190, 75, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/update.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.updatebtn.setIcon(icon1)
        self.updatebtn.setObjectName("updatebtn")

        # 绑定修改
        self.updatebtn.clicked.connect(self.update)

        self.delbtn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.delbtn.setGeometry(QtCore.QRect(350, 190, 75, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/del.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delbtn.setIcon(icon2)
        self.delbtn.setObjectName("delbtn")

        # 绑定删除
        self.delbtn.clicked.connect(self.delete)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "资源类别信息管理"))
        self.groupBox.setTitle(_translate("Form", "查询操作"))
        self.label.setText(_translate("Form", "资源类别名称："))
        self.searchBtn.setText(_translate("Form", "查询"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.label_2.setText(_translate("Form", "编号："))
        self.label_3.setText(_translate("Form", "资源类别名称："))
        self.label_4.setText(_translate("Form", "描述："))
        self.updatebtn.setText(_translate("Form", "修改"))
        self.delbtn.setText(_translate("Form", "删除"))

    def initTable(self):
        """
        根据条件初始化表格
        :return:
        """
        s_reTpyeName = self.s_resourceTpyeNameInpute.text()  # 获取条件
        result = resourceTypeDao.list(s_reTpyeName)
        row = 0
        if result:
            row = len(result)
        self.resourceTpyetable.setColumnCount(3)
        self.resourceTpyetable.setRowCount(row)
        self.resourceTpyetable.verticalHeader().setVisible(False)  # 影藏行号
        self.resourceTpyetable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.resourceTpyetable.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.resourceTpyetable.setHorizontalHeaderLabels(['编号', '资源类别名称', '资源类别描述'])
        self.resourceTpyetable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.resourceTpyetable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        for i in range(row):
            for j in range(3):
                data = QTableWidgetItem(str(result[i][j]))
                self.resourceTpyetable.setItem(i, j, data)

    def initForm(self, index: QModelIndex):
        """
        初始化Form
        :param index:
        :return:
        """
        rowIndex = index.row()  # 获取行索引
        self.idinpute.setText(str(self.resourceTpyetable.item(rowIndex, 0).text()))  # 设置id编号
        self.resourceNameTypeinput.setText(self.resourceTpyetable.item(rowIndex, 1).text())  # 设置图书类别名称
        self.resourceTypeNameDesc.setPlainText(self.resourceTpyetable.item(rowIndex, 2).text())  # 设置图书类别描述

    def update(self):
        """
        修改资源类别信息
        :return:
        """
        id = self.idinpute.text()
        if id.strip() == "":
            QMessageBox.warning(self, "警告", "请选中你需要修改的行！")
            return
        else:
            resourceType = ResourcesType.my_constructor(id, self.resourceNameTypeinput.text(),
                                                        self.resourceTypeNameDesc.toPlainText())
            result = resourceTypeDao.update(resourceType)
            if result > 0:
                QMessageBox.information(self, "提示", "修改成功！")
            else:
                QMessageBox.warning(self, "警告", "修改失败！")
            self.initTable()
            self.resetfrom()

    def delete(self):
        """
        删除资源类别信息
        :return:
        """
        id = self.idinpute.text()
        if id.strip() == "":
            QMessageBox.warning(self, "警告", "请选中你需要删除的行！")
            return
        reply = QMessageBox.question(self, "确认", "你确定要删除吗？",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # 判断该图书类别下面是否有图书
            if resourceDao.countByTypeOd(id)[0] > 0:
                QMessageBox.warning(self, "警告", "该类别下有资源不能删除！")
                self.resetfrom()
            else:
                if resourceTypeDao.delete(int(id)) > 0:
                    QMessageBox.information(self, "提示", "删除成功！")
                    self.initTable()
                    self.resetfrom()
                else:
                    QMessageBox.warning(self, "警告", "删除失败！")

    def resetfrom(self):
        """
        重置表单
        :return:
        """
        self.idinpute.clear()
        self.resourceNameTypeinput.clear()
        self.resourceTypeNameDesc.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
