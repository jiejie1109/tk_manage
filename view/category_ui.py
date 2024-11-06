
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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
        icon.addPixmap(QtGui.QPixmap("../images/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setObjectName("addBtn")
        self.restBtm = QtWidgets.QPushButton(parent=Form)
        self.restBtm.setGeometry(QtCore.QRect(280, 220, 75, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/re.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restBtm.setIcon(icon1)
        self.restBtm.setObjectName("restBtm")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "资源类别添加"))
        self.label.setText(_translate("Form", "资源类别名称："))
        self.label_2.setText(_translate("Form", "资源类别描述："))
        self.addBtn.setText(_translate("Form", "添加"))
        self.restBtm.setText(_translate("Form", "重置"))
