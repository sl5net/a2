# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eRiC\io\code\a2\ui\checkbox_edit.ui'
#
# Created: Mon Oct 12 09:51:54 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_checkbox_edit(object):
    def setupUi(self, checkbox_edit):
        checkbox_edit.setObjectName("checkbox_edit")
        checkbox_edit.resize(977, 182)
        self.verticalLayout = QtGui.QVBoxLayout(checkbox_edit)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(10, 5, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.internalNameLayout = QtGui.QHBoxLayout()
        self.internalNameLayout.setObjectName("internalNameLayout")
        self.internalNameLabel = QtGui.QLabel(checkbox_edit)
        self.internalNameLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.internalNameLabel.setObjectName("internalNameLabel")
        self.internalNameLayout.addWidget(self.internalNameLabel)
        self.cfg_name = QtGui.QLineEdit(checkbox_edit)
        self.cfg_name.setObjectName("cfg_name")
        self.internalNameLayout.addWidget(self.cfg_name)
        self.verticalLayout.addLayout(self.internalNameLayout)
        self.displayLabelLayout = QtGui.QHBoxLayout()
        self.displayLabelLayout.setObjectName("displayLabelLayout")
        self.displayLabelLabel = QtGui.QLabel(checkbox_edit)
        self.displayLabelLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.displayLabelLabel.setObjectName("displayLabelLabel")
        self.displayLabelLayout.addWidget(self.displayLabelLabel)
        self.cfg_label = QtGui.QLineEdit(checkbox_edit)
        self.cfg_label.setObjectName("cfg_label")
        self.displayLabelLayout.addWidget(self.cfg_label)
        self.verticalLayout.addLayout(self.displayLabelLayout)
        self.enabledLayout = QtGui.QHBoxLayout()
        self.enabledLayout.setContentsMargins(-1, -1, -1, 10)
        self.enabledLayout.setObjectName("enabledLayout")
        self.label = QtGui.QLabel(checkbox_edit)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setText("")
        self.label.setObjectName("label")
        self.enabledLayout.addWidget(self.label)
        self.cfg_enabled = QtGui.QCheckBox(checkbox_edit)
        self.cfg_enabled.setChecked(True)
        self.cfg_enabled.setObjectName("cfg_enabled")
        self.enabledLayout.addWidget(self.cfg_enabled)
        self.verticalLayout.addLayout(self.enabledLayout)

        self.retranslateUi(checkbox_edit)
        QtCore.QMetaObject.connectSlotsByName(checkbox_edit)

    def retranslateUi(self, checkbox_edit):
        checkbox_edit.setWindowTitle(QtGui.QApplication.translate("checkbox_edit", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.internalNameLabel.setText(QtGui.QApplication.translate("checkbox_edit", "internal name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_name.setText(QtGui.QApplication.translate("checkbox_edit", "extensionX_checkbox1", None, QtGui.QApplication.UnicodeUTF8))
        self.displayLabelLabel.setText(QtGui.QApplication.translate("checkbox_edit", "display label:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_label.setText(QtGui.QApplication.translate("checkbox_edit", "toggle some value On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_enabled.setText(QtGui.QApplication.translate("checkbox_edit", "enabled by default", None, QtGui.QApplication.UnicodeUTF8))

