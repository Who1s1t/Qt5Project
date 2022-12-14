from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(300, 400)
        App.setMaximumSize(QtCore.QSize(300, 400))
        App.setStyleSheet("background-color: rgb(39, 39, 39);\n"
                          "")
        self.bupdate = QtWidgets.QPushButton(App)
        self.bupdate.setGeometry(QtCore.QRect(20, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bupdate.setFont(font)
        self.bupdate.setStyleSheet("background-color: rgb(255, 130, 46);")
        self.bupdate.setObjectName("bupdate")
        self.widget = QtWidgets.QWidget(App)
        self.widget.setGeometry(QtCore.QRect(20, 80, 251, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b = QtWidgets.QComboBox(self.widget)
        self.b.setEnabled(True)
        self.b.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                             "")
        self.b.setEditable(False)
        self.b.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.b.setIconSize(QtCore.QSize(16, 16))
        self.b.setDuplicatesEnabled(False)
        self.b.setFrame(True)
        self.b.setObjectName("b")
        self.verticalLayout.addWidget(self.b)
        self.iz = QtWidgets.QLineEdit(self.widget)
        self.iz.setToolTipDuration(-4)
        self.iz.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.iz.setObjectName("iz")
        self.verticalLayout.addWidget(self.iz)
        self.b_2 = QtWidgets.QComboBox(self.widget)
        self.b_2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                               "color: rgb(0, 0, 0);")
        self.b_2.setObjectName("b_2")
        self.verticalLayout.addWidget(self.b_2)
        self.v = QtWidgets.QLineEdit(self.widget)
        self.v.setToolTipDuration(-4)
        self.v.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.v.setObjectName("v")
        self.verticalLayout.addWidget(self.v)
        self.but = QtWidgets.QPushButton(self.widget)
        self.but.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.but.setObjectName("but")
        self.verticalLayout.addWidget(self.but)

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Form"))
        self.bupdate.setText(_translate("App", "PushButton"))
        self.but.setText(_translate("App", "PushButton"))
