# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eRiC\io\code\a2\ui\a2element\hotkey_edit.ui'
#
# Created: Sun Sep  4 00:11:04 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_edit(object):
    def setupUi(self, edit):
        edit.setObjectName("edit")
        edit.resize(528, 322)
        self.edit_layout = QtGui.QFormLayout(edit)
        self.edit_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.edit_layout.setContentsMargins(10, 5, 0, 5)
        self.edit_layout.setObjectName("edit_layout")
        self.internalNameLabel = QtGui.QLabel(edit)
        self.internalNameLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.internalNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.internalNameLabel.setObjectName("internalNameLabel")
        self.edit_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.internalNameLabel)
        self.cfg_name = QtGui.QLineEdit(edit)
        self.cfg_name.setObjectName("cfg_name")
        self.edit_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cfg_name)
        self.displayLabelLabel = QtGui.QLabel(edit)
        self.displayLabelLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.displayLabelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.displayLabelLabel.setObjectName("displayLabelLabel")
        self.edit_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.displayLabelLabel)
        self.cfg_label = QtGui.QLineEdit(edit)
        self.cfg_label.setObjectName("cfg_label")
        self.edit_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cfg_label)
        self.hotkeyLabel = QtGui.QLabel(edit)
        self.hotkeyLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.hotkeyLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.hotkeyLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hotkeyLabel.setObjectName("hotkeyLabel")
        self.edit_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.hotkeyLabel)
        self.functionLabel = QtGui.QLabel(edit)
        self.functionLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.functionLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.functionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.functionLabel.setObjectName("functionLabel")
        self.edit_layout.setWidget(5, QtGui.QFormLayout.LabelRole, self.functionLabel)
        self.functionCtrlLayout = QtGui.QVBoxLayout()
        self.functionCtrlLayout.setSpacing(6)
        self.functionCtrlLayout.setContentsMargins(-1, -1, -1, 0)
        self.functionCtrlLayout.setObjectName("functionCtrlLayout")
        self.functionRowLayout = QtGui.QHBoxLayout()
        self.functionRowLayout.setContentsMargins(-1, 0, -1, -1)
        self.functionRowLayout.setObjectName("functionRowLayout")
        self.cfg_functionMode = QtGui.QComboBox(edit)
        self.cfg_functionMode.setObjectName("cfg_functionMode")
        self.cfg_functionMode.addItem("")
        self.cfg_functionMode.addItem("")
        self.cfg_functionMode.addItem("")
        self.functionRowLayout.addWidget(self.cfg_functionMode)
        self.functionButton = QtGui.QPushButton(edit)
        self.functionButton.setMaximumSize(QtCore.QSize(50, 35))
        self.functionButton.setObjectName("functionButton")
        self.functionRowLayout.addWidget(self.functionButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.functionRowLayout.addItem(spacerItem)
        self.functionCtrlLayout.addLayout(self.functionRowLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.function_send_mode = QtGui.QComboBox(edit)
        self.function_send_mode.setObjectName("function_send_mode")
        self.function_send_mode.addItem("")
        self.function_send_mode.addItem("")
        self.function_send_mode.addItem("")
        self.function_send_mode.addItem("")
        self.function_send_mode.addItem("")
        self.horizontalLayout.addWidget(self.function_send_mode)
        self.run_label = QtGui.QLabel(edit)
        self.run_label.setObjectName("run_label")
        self.horizontalLayout.addWidget(self.run_label)
        self.functionText = QtGui.QLineEdit(edit)
        self.functionText.setObjectName("functionText")
        self.horizontalLayout.addWidget(self.functionText)
        self.functionCtrlLayout.addLayout(self.horizontalLayout)
        self.edit_layout.setLayout(5, QtGui.QFormLayout.FieldRole, self.functionCtrlLayout)
        self.scopeLabel = QtGui.QLabel(edit)
        self.scopeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.scopeLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.scopeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scopeLabel.setObjectName("scopeLabel")
        self.edit_layout.setWidget(6, QtGui.QFormLayout.LabelRole, self.scopeLabel)
        self.scopeCtrlLayout = QtGui.QVBoxLayout()
        self.scopeCtrlLayout.setSpacing(5)
        self.scopeCtrlLayout.setContentsMargins(-1, -1, -1, 0)
        self.scopeCtrlLayout.setObjectName("scopeCtrlLayout")
        self.scopeRowLayout = QtGui.QHBoxLayout()
        self.scopeRowLayout.setSpacing(9)
        self.scopeRowLayout.setContentsMargins(-1, 0, -1, -1)
        self.scopeRowLayout.setObjectName("scopeRowLayout")
        self.cfg_scopeMode = QtGui.QComboBox(edit)
        self.cfg_scopeMode.setObjectName("cfg_scopeMode")
        self.cfg_scopeMode.addItem("")
        self.cfg_scopeMode.addItem("")
        self.cfg_scopeMode.addItem("")
        self.scopeRowLayout.addWidget(self.cfg_scopeMode)
        self.scopePlus = QtGui.QPushButton(edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scopePlus.sizePolicy().hasHeightForWidth())
        self.scopePlus.setSizePolicy(sizePolicy)
        self.scopePlus.setMaximumSize(QtCore.QSize(50, 35))
        self.scopePlus.setObjectName("scopePlus")
        self.scopeRowLayout.addWidget(self.scopePlus)
        self.scopeMinus = QtGui.QPushButton(edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scopeMinus.sizePolicy().hasHeightForWidth())
        self.scopeMinus.setSizePolicy(sizePolicy)
        self.scopeMinus.setMaximumSize(QtCore.QSize(50, 35))
        self.scopeMinus.setObjectName("scopeMinus")
        self.scopeRowLayout.addWidget(self.scopeMinus)
        self.cfg_scopeChange = QtGui.QCheckBox(edit)
        self.cfg_scopeChange.setChecked(True)
        self.cfg_scopeChange.setObjectName("cfg_scopeChange")
        self.scopeRowLayout.addWidget(self.cfg_scopeChange)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.scopeRowLayout.addItem(spacerItem1)
        self.scopeCtrlLayout.addLayout(self.scopeRowLayout)
        self.cfg_scope = QtGui.QListWidget(edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfg_scope.sizePolicy().hasHeightForWidth())
        self.cfg_scope.setSizePolicy(sizePolicy)
        self.cfg_scope.setMinimumSize(QtCore.QSize(0, 40))
        self.cfg_scope.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cfg_scope.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cfg_scope.setObjectName("cfg_scope")
        self.scopeCtrlLayout.addWidget(self.cfg_scope)
        self.edit_layout.setLayout(6, QtGui.QFormLayout.FieldRole, self.scopeCtrlLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hotkey_button = A2Hotkey(edit)
        self.hotkey_button.setEnabled(True)
        self.hotkey_button.setObjectName("hotkey_button")
        self.verticalLayout.addWidget(self.hotkey_button)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.cfg_enabled = QtGui.QCheckBox(edit)
        self.cfg_enabled.setChecked(True)
        self.cfg_enabled.setObjectName("cfg_enabled")
        self.gridLayout.addWidget(self.cfg_enabled, 0, 0, 1, 1)
        self.cfg_disablable = QtGui.QCheckBox(edit)
        self.cfg_disablable.setChecked(True)
        self.cfg_disablable.setObjectName("cfg_disablable")
        self.gridLayout.addWidget(self.cfg_disablable, 3, 0, 1, 1)
        self.cfg_keyChange = QtGui.QCheckBox(edit)
        self.cfg_keyChange.setChecked(True)
        self.cfg_keyChange.setObjectName("cfg_keyChange")
        self.gridLayout.addWidget(self.cfg_keyChange, 0, 1, 1, 1)
        self.cfg_multiple = QtGui.QCheckBox(edit)
        self.cfg_multiple.setChecked(True)
        self.cfg_multiple.setObjectName("cfg_multiple")
        self.gridLayout.addWidget(self.cfg_multiple, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.edit_layout.setLayout(3, QtGui.QFormLayout.FieldRole, self.verticalLayout)

        self.retranslateUi(edit)
        QtCore.QMetaObject.connectSlotsByName(edit)

    def retranslateUi(self, edit):
        edit.setWindowTitle(QtGui.QApplication.translate("edit", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.internalNameLabel.setText(QtGui.QApplication.translate("edit", "internal name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_name.setText(QtGui.QApplication.translate("edit", "extensionX_hotkey1", None, QtGui.QApplication.UnicodeUTF8))
        self.displayLabelLabel.setText(QtGui.QApplication.translate("edit", "display label:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_label.setText(QtGui.QApplication.translate("edit", "make some awesome stuff", None, QtGui.QApplication.UnicodeUTF8))
        self.hotkeyLabel.setText(QtGui.QApplication.translate("edit", "hotkey:", None, QtGui.QApplication.UnicodeUTF8))
        self.functionLabel.setText(QtGui.QApplication.translate("edit", "function:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_functionMode.setItemText(0, QtGui.QApplication.translate("edit", "Run code", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_functionMode.setItemText(1, QtGui.QApplication.translate("edit", "Open file/url", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_functionMode.setItemText(2, QtGui.QApplication.translate("edit", "Send keystroke", None, QtGui.QApplication.UnicodeUTF8))
        self.functionButton.setText(QtGui.QApplication.translate("edit", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.function_send_mode.setItemText(0, QtGui.QApplication.translate("edit", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.function_send_mode.setItemText(1, QtGui.QApplication.translate("edit", "SendRaw", None, QtGui.QApplication.UnicodeUTF8))
        self.function_send_mode.setItemText(2, QtGui.QApplication.translate("edit", "SendInput", None, QtGui.QApplication.UnicodeUTF8))
        self.function_send_mode.setItemText(3, QtGui.QApplication.translate("edit", "SendPlay", None, QtGui.QApplication.UnicodeUTF8))
        self.function_send_mode.setItemText(4, QtGui.QApplication.translate("edit", "SendEvent", None, QtGui.QApplication.UnicodeUTF8))
        self.run_label.setText(QtGui.QApplication.translate("edit", "Run, ", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeLabel.setText(QtGui.QApplication.translate("edit", "scope:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeMode.setItemText(0, QtGui.QApplication.translate("edit", "global", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeMode.setItemText(1, QtGui.QApplication.translate("edit", "only in:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeMode.setItemText(2, QtGui.QApplication.translate("edit", "not in:", None, QtGui.QApplication.UnicodeUTF8))
        self.scopePlus.setText(QtGui.QApplication.translate("edit", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMinus.setText(QtGui.QApplication.translate("edit", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeChange.setText(QtGui.QApplication.translate("edit", "can be changed", None, QtGui.QApplication.UnicodeUTF8))
        self.hotkey_button.setText(QtGui.QApplication.translate("edit", "Win+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_enabled.setText(QtGui.QApplication.translate("edit", "enabled by default", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_disablable.setText(QtGui.QApplication.translate("edit", "can be disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_keyChange.setText(QtGui.QApplication.translate("edit", "can be changed", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_multiple.setText(QtGui.QApplication.translate("edit", "allow multiple hotkeys", None, QtGui.QApplication.UnicodeUTF8))

from a2widget.a2hotkey import A2Hotkey
