# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\keyboard\numpad.ui'
#
# Created: Mon Jan 29 00:35:11 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Numpad(object):
    def setupUi(self, Numpad):
        Numpad.setObjectName("Numpad")
        Numpad.resize(726, 550)
        self.gridLayout = QtGui.QGridLayout(Numpad)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.numlock = QtGui.QPushButton(Numpad)
        self.numlock.setObjectName("numlock")
        self.gridLayout.addWidget(self.numlock, 1, 0, 1, 1)
        self.numpaddiv = QtGui.QPushButton(Numpad)
        self.numpaddiv.setObjectName("numpaddiv")
        self.gridLayout.addWidget(self.numpaddiv, 1, 1, 1, 1)
        self.numpad1 = QtGui.QPushButton(Numpad)
        self.numpad1.setObjectName("numpad1")
        self.gridLayout.addWidget(self.numpad1, 4, 0, 1, 1)
        self.numpad5 = QtGui.QPushButton(Numpad)
        self.numpad5.setObjectName("numpad5")
        self.gridLayout.addWidget(self.numpad5, 3, 1, 1, 1)
        self.numpadmult = QtGui.QPushButton(Numpad)
        self.numpadmult.setObjectName("numpadmult")
        self.gridLayout.addWidget(self.numpadmult, 1, 2, 1, 1)
        self.numpad8 = QtGui.QPushButton(Numpad)
        self.numpad8.setObjectName("numpad8")
        self.gridLayout.addWidget(self.numpad8, 2, 1, 1, 1)
        self.numpad4 = QtGui.QPushButton(Numpad)
        self.numpad4.setObjectName("numpad4")
        self.gridLayout.addWidget(self.numpad4, 3, 0, 1, 1)
        self.numpad3 = QtGui.QPushButton(Numpad)
        self.numpad3.setObjectName("numpad3")
        self.gridLayout.addWidget(self.numpad3, 4, 2, 1, 1)
        self.numpad6 = QtGui.QPushButton(Numpad)
        self.numpad6.setObjectName("numpad6")
        self.gridLayout.addWidget(self.numpad6, 3, 2, 1, 1)
        self.numpad7 = QtGui.QPushButton(Numpad)
        self.numpad7.setObjectName("numpad7")
        self.gridLayout.addWidget(self.numpad7, 2, 0, 1, 1)
        self.numpad2 = QtGui.QPushButton(Numpad)
        self.numpad2.setObjectName("numpad2")
        self.gridLayout.addWidget(self.numpad2, 4, 1, 1, 1)
        self.numpaddot = QtGui.QPushButton(Numpad)
        self.numpaddot.setObjectName("numpaddot")
        self.gridLayout.addWidget(self.numpaddot, 5, 2, 1, 1)
        self.numpad9 = QtGui.QPushButton(Numpad)
        self.numpad9.setObjectName("numpad9")
        self.gridLayout.addWidget(self.numpad9, 2, 2, 1, 1)
        self.numpad0 = QtGui.QPushButton(Numpad)
        self.numpad0.setObjectName("numpad0")
        self.gridLayout.addWidget(self.numpad0, 5, 0, 1, 2)
        self.numpadsub = QtGui.QPushButton(Numpad)
        self.numpadsub.setObjectName("numpadsub")
        self.gridLayout.addWidget(self.numpadsub, 1, 3, 1, 1)
        self.num_spacer = QtGui.QWidget(Numpad)
        self.num_spacer.setObjectName("num_spacer")
        self.gridLayout.addWidget(self.num_spacer, 0, 0, 1, 5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.numpadadd = QtGui.QPushButton(Numpad)
        self.numpadadd.setMinimumSize(QtCore.QSize(0, 120))
        self.numpadadd.setObjectName("numpadadd")
        self.verticalLayout_2.addWidget(self.numpadadd)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 3, 2, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.numpadenter = QtGui.QPushButton(Numpad)
        self.numpadenter.setMinimumSize(QtCore.QSize(0, 90))
        self.numpadenter.setObjectName("numpadenter")
        self.verticalLayout.addWidget(self.numpadenter)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 4, 3, 2, 1)
        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(Numpad)
        QtCore.QMetaObject.connectSlotsByName(Numpad)

    def retranslateUi(self, Numpad):
        Numpad.setWindowTitle(QtGui.QApplication.translate("Numpad", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.numlock.setText(QtGui.QApplication.translate("Numpad", "Num\n"
"Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.numpaddiv.setText(QtGui.QApplication.translate("Numpad", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad1.setText(QtGui.QApplication.translate("Numpad", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad5.setText(QtGui.QApplication.translate("Numpad", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadmult.setText(QtGui.QApplication.translate("Numpad", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad8.setText(QtGui.QApplication.translate("Numpad", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad4.setText(QtGui.QApplication.translate("Numpad", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad3.setText(QtGui.QApplication.translate("Numpad", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad6.setText(QtGui.QApplication.translate("Numpad", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad7.setText(QtGui.QApplication.translate("Numpad", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad2.setText(QtGui.QApplication.translate("Numpad", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.numpaddot.setText(QtGui.QApplication.translate("Numpad", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad9.setText(QtGui.QApplication.translate("Numpad", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad0.setText(QtGui.QApplication.translate("Numpad", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadsub.setText(QtGui.QApplication.translate("Numpad", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadadd.setText(QtGui.QApplication.translate("Numpad", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadenter.setText(QtGui.QApplication.translate("Numpad", "Enter", None, QtGui.QApplication.UnicodeUTF8))

