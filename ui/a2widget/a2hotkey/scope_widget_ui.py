# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\scope_widget.ui'
#
# Created: Mon May 14 16:15:20 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScopeWidget(object):
    def setupUi(self, ScopeWidget):
        ScopeWidget.setObjectName("ScopeWidget")
        ScopeWidget.resize(535, 146)
        ScopeWidget.setWindowTitle("Form")
        ScopeWidget.setToolTip("")
        self.formLayout = QtGui.QFormLayout(ScopeWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scopeMode_1 = QtGui.QRadioButton(ScopeWidget)
        self.scopeMode_1.setChecked(True)
        self.scopeMode_1.setObjectName("scopeMode_1")
        self.horizontalLayout_2.addWidget(self.scopeMode_1)
        self.scopeMode_2 = QtGui.QRadioButton(ScopeWidget)
        self.scopeMode_2.setChecked(False)
        self.scopeMode_2.setObjectName("scopeMode_2")
        self.horizontalLayout_2.addWidget(self.scopeMode_2)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scope_delete = QtGui.QToolButton(ScopeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_delete.sizePolicy().hasHeightForWidth())
        self.scope_delete.setSizePolicy(sizePolicy)
        self.scope_delete.setMaximumSize(QtCore.QSize(50, 35))
        self.scope_delete.setToolTip("")
        self.scope_delete.setText("-")
        self.scope_delete.setAutoRaise(True)
        self.scope_delete.setObjectName("scope_delete")
        self.horizontalLayout_2.addWidget(self.scope_delete)
        self.scope_add = QtGui.QToolButton(ScopeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_add.sizePolicy().hasHeightForWidth())
        self.scope_add.setSizePolicy(sizePolicy)
        self.scope_add.setMaximumSize(QtCore.QSize(50, 35))
        self.scope_add.setToolTip("")
        self.scope_add.setText("+")
        self.scope_add.setAutoRaise(True)
        self.scope_add.setObjectName("scope_add")
        self.horizontalLayout_2.addWidget(self.scope_add)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.cfg_scope = QtGui.QListWidget(ScopeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfg_scope.sizePolicy().hasHeightForWidth())
        self.cfg_scope.setSizePolicy(sizePolicy)
        self.cfg_scope.setMinimumSize(QtCore.QSize(0, 40))
        self.cfg_scope.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cfg_scope.setToolTip("")
        self.cfg_scope.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cfg_scope.setObjectName("cfg_scope")
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.cfg_scope)
        self.label_2 = QtGui.QLabel(ScopeWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.scope_title = A2ButtonField(ScopeWidget)
        self.scope_title.setObjectName("scope_title")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.scope_title)
        self.label_3 = QtGui.QLabel(ScopeWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.scope_class = A2ButtonField(ScopeWidget)
        self.scope_class.setObjectName("scope_class")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.scope_class)
        self.label_4 = QtGui.QLabel(ScopeWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.scope_exe = A2ButtonField(ScopeWidget)
        self.scope_exe.setObjectName("scope_exe")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.scope_exe)

        self.retranslateUi(ScopeWidget)
        QtCore.QMetaObject.connectSlotsByName(ScopeWidget)

    def retranslateUi(self, ScopeWidget):
        self.scopeMode_1.setText(QtGui.QApplication.translate("ScopeWidget", "only in:", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMode_2.setText(QtGui.QApplication.translate("ScopeWidget", "not in:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScopeWidget", "title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ScopeWidget", "window class", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ScopeWidget", "executable", None, QtGui.QApplication.UnicodeUTF8))

from a2widget.a2button_field import A2ButtonField
