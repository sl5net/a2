# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\keyboard\mouse.ui'
#
# Created: Sun Jan 28 22:51:28 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Mouse(object):
    def setupUi(self, Mouse):
        Mouse.setObjectName("Mouse")
        Mouse.resize(420, 289)
        self.verticalLayout = QtGui.QVBoxLayout(Mouse)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inner_widget = QtGui.QWidget(Mouse)
        self.inner_widget.setMaximumSize(QtCore.QSize(420, 200))
        self.inner_widget.setObjectName("inner_widget")
        self.main_layout = QtGui.QHBoxLayout(self.inner_widget)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.lbutton = QtGui.QPushButton(self.inner_widget)
        self.lbutton.setMinimumSize(QtCore.QSize(0, 200))
        self.lbutton.setMaximumSize(QtCore.QSize(100, 200))
        self.lbutton.setBaseSize(QtCore.QSize(0, 0))
        self.lbutton.setObjectName("lbutton")
        self.main_layout.addWidget(self.lbutton)
        self.wheelleft = QtGui.QPushButton(self.inner_widget)
        self.wheelleft.setMaximumSize(QtCore.QSize(40, 180))
        self.wheelleft.setText("")
        self.wheelleft.setObjectName("wheelleft")
        self.main_layout.addWidget(self.wheelleft)
        self.middle_layout = QtGui.QVBoxLayout()
        self.middle_layout.setSpacing(10)
        self.middle_layout.setObjectName("middle_layout")
        self.wheelup = QtGui.QPushButton(self.inner_widget)
        self.wheelup.setMaximumSize(QtCore.QSize(100, 40))
        self.wheelup.setText("")
        self.wheelup.setObjectName("wheelup")
        self.middle_layout.addWidget(self.wheelup)
        self.mbutton = QtGui.QPushButton(self.inner_widget)
        self.mbutton.setMinimumSize(QtCore.QSize(0, 100))
        self.mbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mbutton.setObjectName("mbutton")
        self.middle_layout.addWidget(self.mbutton)
        self.wheeldown = QtGui.QPushButton(self.inner_widget)
        self.wheeldown.setMaximumSize(QtCore.QSize(100, 40))
        self.wheeldown.setText("")
        self.wheeldown.setObjectName("wheeldown")
        self.middle_layout.addWidget(self.wheeldown)
        self.main_layout.addLayout(self.middle_layout)
        self.wheelright = QtGui.QPushButton(self.inner_widget)
        self.wheelright.setMaximumSize(QtCore.QSize(40, 180))
        self.wheelright.setText("")
        self.wheelright.setObjectName("wheelright")
        self.main_layout.addWidget(self.wheelright)
        self.rbutton = QtGui.QPushButton(self.inner_widget)
        self.rbutton.setMinimumSize(QtCore.QSize(0, 200))
        self.rbutton.setMaximumSize(QtCore.QSize(100, 200))
        self.rbutton.setObjectName("rbutton")
        self.main_layout.addWidget(self.rbutton)
        self.verticalLayout.addWidget(self.inner_widget)
        self._mouse_body = QtGui.QWidget(Mouse)
        self._mouse_body.setObjectName("_mouse_body")
        self.verticalLayout.addWidget(self._mouse_body)

        self.retranslateUi(Mouse)
        QtCore.QMetaObject.connectSlotsByName(Mouse)

    def retranslateUi(self, Mouse):
        Mouse.setWindowTitle(QtGui.QApplication.translate("Mouse", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lbutton.setToolTip(QtGui.QApplication.translate("Mouse", "Left Mouse Button", None, QtGui.QApplication.UnicodeUTF8))
        self.lbutton.setText(QtGui.QApplication.translate("Mouse", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.wheelleft.setToolTip(QtGui.QApplication.translate("Mouse", "Wheel Left", None, QtGui.QApplication.UnicodeUTF8))
        self.wheelup.setToolTip(QtGui.QApplication.translate("Mouse", "Wheel Up", None, QtGui.QApplication.UnicodeUTF8))
        self.mbutton.setToolTip(QtGui.QApplication.translate("Mouse", "Middle Mouse Button", None, QtGui.QApplication.UnicodeUTF8))
        self.mbutton.setText(QtGui.QApplication.translate("Mouse", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.wheeldown.setToolTip(QtGui.QApplication.translate("Mouse", "Wheel Down", None, QtGui.QApplication.UnicodeUTF8))
        self.wheelright.setToolTip(QtGui.QApplication.translate("Mouse", "Wheel Right", None, QtGui.QApplication.UnicodeUTF8))
        self.rbutton.setToolTip(QtGui.QApplication.translate("Mouse", "Right Mouse Button", None, QtGui.QApplication.UnicodeUTF8))
        self.rbutton.setText(QtGui.QApplication.translate("Mouse", "R", None, QtGui.QApplication.UnicodeUTF8))

