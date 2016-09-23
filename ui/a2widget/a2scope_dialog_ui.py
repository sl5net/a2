# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2ctrl\scopeDialog.ui'
#
# Created: Wed Aug 31 21:47:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScopeDialog(object):
    def setupUi(self, ScopeDialog):
        ScopeDialog.setObjectName("ScopeDialog")
        ScopeDialog.resize(780, 167)
        self.verticalLayout = QtGui.QVBoxLayout(ScopeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.helpButton = QtGui.QPushButton(ScopeDialog)
        self.helpButton.setMinimumSize(QtCore.QSize(200, 0))
        self.helpButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.helpButton.setStyleSheet("* {text-align: right}")
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_5.addWidget(self.helpButton)
        self.scopeText = QtGui.QLineEdit(ScopeDialog)
        self.scopeText.setReadOnly(True)
        self.scopeText.setObjectName("scopeText")
        self.horizontalLayout_5.addWidget(self.scopeText)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.titleButton = QtGui.QPushButton(ScopeDialog)
        self.titleButton.setMinimumSize(QtCore.QSize(200, 0))
        self.titleButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.titleButton.setStyleSheet("* {text-align: right}")
        self.titleButton.setObjectName("titleButton")
        self.horizontalLayout_2.addWidget(self.titleButton)
        self.scopeTitle = QtGui.QLineEdit(ScopeDialog)
        self.scopeTitle.setObjectName("scopeTitle")
        self.horizontalLayout_2.addWidget(self.scopeTitle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.classButton = QtGui.QPushButton(ScopeDialog)
        self.classButton.setMinimumSize(QtCore.QSize(200, 0))
        self.classButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.classButton.setStyleSheet("* {text-align: right}")
        self.classButton.setObjectName("classButton")
        self.horizontalLayout_3.addWidget(self.classButton)
        self.scopeClass = QtGui.QLineEdit(ScopeDialog)
        self.scopeClass.setObjectName("scopeClass")
        self.horizontalLayout_3.addWidget(self.scopeClass)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exeButton = QtGui.QPushButton(ScopeDialog)
        self.exeButton.setMinimumSize(QtCore.QSize(200, 0))
        self.exeButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.exeButton.setStyleSheet("* {text-align: right}")
        self.exeButton.setObjectName("exeButton")
        self.horizontalLayout_4.addWidget(self.exeButton)
        self.scopeExe = QtGui.QLineEdit(ScopeDialog)
        self.scopeExe.setObjectName("scopeExe")
        self.horizontalLayout_4.addWidget(self.scopeExe)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.a2ok_button = QtGui.QPushButton(ScopeDialog)
        self.a2ok_button.setObjectName("a2ok_button")
        self.horizontalLayout.addWidget(self.a2ok_button)
        self.a2cancel_button = QtGui.QPushButton(ScopeDialog)
        self.a2cancel_button.setFlat(True)
        self.a2cancel_button.setObjectName("a2cancel_button")
        self.horizontalLayout.addWidget(self.a2cancel_button)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ScopeDialog)
        QtCore.QMetaObject.connectSlotsByName(ScopeDialog)
        ScopeDialog.setTabOrder(self.scopeText, self.scopeTitle)
        ScopeDialog.setTabOrder(self.scopeTitle, self.scopeClass)
        ScopeDialog.setTabOrder(self.scopeClass, self.scopeExe)
        ScopeDialog.setTabOrder(self.scopeExe, self.a2ok_button)
        ScopeDialog.setTabOrder(self.a2ok_button, self.a2cancel_button)
        ScopeDialog.setTabOrder(self.a2cancel_button, self.helpButton)
        ScopeDialog.setTabOrder(self.helpButton, self.titleButton)
        ScopeDialog.setTabOrder(self.titleButton, self.classButton)
        ScopeDialog.setTabOrder(self.classButton, self.exeButton)

    def retranslateUi(self, ScopeDialog):
        ScopeDialog.setWindowTitle(QtGui.QApplication.translate("ScopeDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.helpButton.setText(QtGui.QApplication.translate("ScopeDialog", "scope description", None, QtGui.QApplication.UnicodeUTF8))
        self.titleButton.setText(QtGui.QApplication.translate("ScopeDialog", "title", None, QtGui.QApplication.UnicodeUTF8))
        self.classButton.setText(QtGui.QApplication.translate("ScopeDialog", "window class", None, QtGui.QApplication.UnicodeUTF8))
        self.exeButton.setText(QtGui.QApplication.translate("ScopeDialog", "executable", None, QtGui.QApplication.UnicodeUTF8))
        self.a2ok_button.setText(QtGui.QApplication.translate("ScopeDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.a2cancel_button.setText(QtGui.QApplication.translate("ScopeDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
