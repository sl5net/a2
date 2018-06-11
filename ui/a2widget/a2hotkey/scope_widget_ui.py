# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\scope_widget.ui'
#
# Created: Mon Jun 11 15:51:56 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScopeWidget(object):
    def setupUi(self, ScopeWidget):
        ScopeWidget.setObjectName("ScopeWidget")
        ScopeWidget.resize(500, 146)
        ScopeWidget.setWindowTitle("Form")
        ScopeWidget.setToolTip("")
        self.verticalLayout = QtGui.QVBoxLayout(ScopeWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.type_radio_widget = QtGui.QWidget(ScopeWidget)
        self.type_radio_widget.setObjectName("type_radio_widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.type_radio_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scopeMode_0 = QtGui.QRadioButton(self.type_radio_widget)
        self.scopeMode_0.setChecked(True)
        self.scopeMode_0.setObjectName("scopeMode_0")
        self.horizontalLayout.addWidget(self.scopeMode_0)
        self.scopeMode_1 = QtGui.QRadioButton(self.type_radio_widget)
        self.scopeMode_1.setChecked(False)
        self.scopeMode_1.setObjectName("scopeMode_1")
        self.horizontalLayout.addWidget(self.scopeMode_1)
        self.scopeMode_2 = QtGui.QRadioButton(self.type_radio_widget)
        self.scopeMode_2.setChecked(False)
        self.scopeMode_2.setObjectName("scopeMode_2")
        self.horizontalLayout.addWidget(self.scopeMode_2)
        self.horizontalLayout_2.addWidget(self.type_radio_widget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.tool_buttons_widget = QtGui.QWidget(ScopeWidget)
        self.tool_buttons_widget.setObjectName("tool_buttons_widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tool_buttons_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scope_help = QtGui.QToolButton(self.tool_buttons_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_help.sizePolicy().hasHeightForWidth())
        self.scope_help.setSizePolicy(sizePolicy)
        self.scope_help.setMaximumSize(QtCore.QSize(50, 35))
        self.scope_help.setToolTip("Help on Scopes")
        self.scope_help.setText("h")
        self.scope_help.setAutoRaise(True)
        self.scope_help.setObjectName("scope_help")
        self.horizontalLayout_3.addWidget(self.scope_help)
        self.scope_pick = QtGui.QToolButton(self.tool_buttons_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_pick.sizePolicy().hasHeightForWidth())
        self.scope_pick.setSizePolicy(sizePolicy)
        self.scope_pick.setMaximumSize(QtCore.QSize(50, 35))
        self.scope_pick.setToolTip("Pick from a Window")
        self.scope_pick.setText("p")
        self.scope_pick.setAutoRaise(True)
        self.scope_pick.setObjectName("scope_pick")
        self.horizontalLayout_3.addWidget(self.scope_pick)
        self.scope_delete = QtGui.QToolButton(self.tool_buttons_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_delete.sizePolicy().hasHeightForWidth())
        self.scope_delete.setSizePolicy(sizePolicy)
        self.scope_delete.setMaximumSize(QtCore.QSize(50, 35))
        self.scope_delete.setToolTip("Delete Selected Scope")
        self.scope_delete.setText("-")
        self.scope_delete.setAutoRaise(True)
        self.scope_delete.setObjectName("scope_delete")
        self.horizontalLayout_3.addWidget(self.scope_delete)
        self.scope_add = QtGui.QToolButton(self.tool_buttons_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_add.sizePolicy().hasHeightForWidth())
        self.scope_add.setSizePolicy(sizePolicy)
        self.scope_add.setMaximumSize(QtCore.QSize(50, 35))
        self.scope_add.setToolTip("Add a Scope")
        self.scope_add.setText("+")
        self.scope_add.setAutoRaise(True)
        self.scope_add.setObjectName("scope_add")
        self.horizontalLayout_3.addWidget(self.scope_add)
        self.horizontalLayout_2.addWidget(self.tool_buttons_widget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cfg_scope = A2ListCompact(ScopeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfg_scope.sizePolicy().hasHeightForWidth())
        self.cfg_scope.setSizePolicy(sizePolicy)
        self.cfg_scope.setMinimumSize(QtCore.QSize(500, 40))
        self.cfg_scope.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cfg_scope.setToolTip("")
        self.cfg_scope.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cfg_scope.setObjectName("cfg_scope")
        self.verticalLayout.addWidget(self.cfg_scope)
        self.fields_widget = QtGui.QWidget(ScopeWidget)
        self.fields_widget.setObjectName("fields_widget")
        self.formLayout_2 = QtGui.QFormLayout(self.fields_widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtGui.QLabel(self.fields_widget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.scope_title = A2ButtonField(self.fields_widget)
        self.scope_title.setObjectName("scope_title")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.scope_title)
        self.label_3 = QtGui.QLabel(self.fields_widget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.scope_class = A2ButtonField(self.fields_widget)
        self.scope_class.setObjectName("scope_class")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.scope_class)
        self.label_4 = QtGui.QLabel(self.fields_widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.scope_exe = A2ButtonField(self.fields_widget)
        self.scope_exe.setObjectName("scope_exe")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.scope_exe)
        self.verticalLayout.addWidget(self.fields_widget)

        self.retranslateUi(ScopeWidget)
        QtCore.QMetaObject.connectSlotsByName(ScopeWidget)

    def retranslateUi(self, ScopeWidget):
        self.scopeMode_0.setToolTip(QtGui.QApplication.translate("ScopeWidget", "global - Makes it work anywhere in the system.", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMode_0.setText(QtGui.QApplication.translate("ScopeWidget", "golbal", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMode_1.setToolTip(QtGui.QApplication.translate("ScopeWidget", "include - To make it work ONLY in certain windows.", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMode_1.setText(QtGui.QApplication.translate("ScopeWidget", "include:", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMode_2.setToolTip(QtGui.QApplication.translate("ScopeWidget", "exclude - To make it work anywhere BUT not in given windows.", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMode_2.setText(QtGui.QApplication.translate("ScopeWidget", "exclude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScopeWidget", "title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ScopeWidget", "window class", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ScopeWidget", "executable", None, QtGui.QApplication.UnicodeUTF8))

from a2widget import A2ListCompact, A2ButtonField