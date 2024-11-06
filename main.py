import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox

from dao import userDao
from datetime import datetime

from resources import resourcesAdd, resourceManage
from resourcesType import resourcesTypeAdd, resourceTypeManage
from setting import modifyPassword


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # 只显示最小化和关闭按钮
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 665)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 设置背景图片
        self.centralwidget.setStyleSheet(
            "background-image: url(images/bg.jpg); "
            "background-repeat: no-repeat; "
            "background-position: center center; "
            "background-size: contain;"
        )

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        # 设置状态栏
        mylabel = QLabel()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        mylabel.setText(
            "当前用户：" + userDao.current_user.username + "        无限进步 ε=ε=ε=ε=ε” “(/’-‘)/" + "           登录时间:" + current_time)
        self.statusbar.addWidget(mylabel)

        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/fix.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action.setIcon(icon1)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/eixt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_2.setIcon(icon2)
        self.action_2.setObjectName("action_2")
        self.actionWritten_By_DYJ = QtGui.QAction(parent=MainWindow)
        self.actionWritten_By_DYJ.setObjectName("actionWritten_By_DYJ")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_4.setIcon(icon3)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/man.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_5.setIcon(icon4)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/plus2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_6.setIcon(icon5)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/leibie.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_7.setIcon(icon6)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)

        # 资源菜单点击事件
        self.menu.triggered[QAction].connect(self.open_resource)

        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)

        # 资源类别菜单点击事件
        self.menu_2.triggered[QAction].connect(self.open_setting)

        self.menu_3.addAction(self.action)
        self.menu_3.addAction(self.action_2)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionWritten_By_DYJ)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        # 资源类别菜单点击事件
        self.menu_3.triggered[QAction].connect(self.open_setting)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "资源管理系统"))
        self.menu.setTitle(_translate("MainWindow", "资源管理"))
        self.menu_2.setTitle(_translate("MainWindow", "资源类别管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统设置"))
        self.action.setText(_translate("MainWindow", "修改密码"))
        self.action_2.setText(_translate("MainWindow", "安全退出"))
        self.actionWritten_By_DYJ.setText(_translate("MainWindow", "Written By DYJ"))
        self.action_4.setText(_translate("MainWindow", "资源添加"))
        self.action_5.setText(_translate("MainWindow", "资源信息管理"))
        self.action_6.setText(_translate("MainWindow", "资源类别添加"))
        self.action_7.setText(_translate("MainWindow", "资源类别信息管理"))

    def open_resource_type(self, m):
        if m.text() == "资源类别添加":
            self.resourceTypeAdd = resourcesTypeAdd.Ui_Form()
            self.resourceTypeAdd.show()
        elif m.text() == "资源类别信息管理":
            self.resourceTypeManage = resourceTypeManage.Ui_Form()
            self.resourceTypeManage.show()

    def open_resource(self, m):
        if m.text() == "资源添加":
            self.resourceAdd = resourcesAdd.Ui_Form()
            self.resourceAdd.show()
        elif m.text() == "资源信息管理":
            self.resourceManage = resourceManage.Ui_Form()
            self.resourceManage.show()

    def open_setting(self, m):
        if m.text() == "修改密码":
            self.modifyPassword = modifyPassword.Ui_Form()
            self.modifyPassword.show()
        elif m.text() == "安全退出":
            reply = QMessageBox.question(self, "确认", "你确定要退出吗？",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.close()
        elif m.text() == "Written By DYJ":
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec())
