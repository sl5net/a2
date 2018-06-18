# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\keyboard_dialog\base.ui'
#
# Created: Mon Jun 18 14:12:20 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Keyboard(object):
    def setupUi(self, Keyboard):
        Keyboard.setObjectName("Keyboard")
        Keyboard.resize(744, 332)
        self.dialog_layout = QtGui.QVBoxLayout(Keyboard)
        self.dialog_layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.dialog_layout.setObjectName("dialog_layout")
        self.top_layout = QtGui.QHBoxLayout()
        self.top_layout.setContentsMargins(-1, 10, -1, 10)
        self.top_layout.setObjectName("top_layout")
        self.key_field = QtGui.QLineEdit(Keyboard)
        self.key_field.setText("")
        self.key_field.setReadOnly(True)
        self.key_field.setObjectName("key_field")
        self.top_layout.addWidget(self.key_field)
        self.option_button = A2MoreButton(Keyboard)
        self.option_button.setObjectName("option_button")
        self.top_layout.addWidget(self.option_button)
        self.label_2 = QtGui.QLabel(Keyboard)
        self.label_2.setObjectName("label_2")
        self.top_layout.addWidget(self.label_2)
        self.check_numpad = QtGui.QCheckBox(Keyboard)
        self.check_numpad.setText("Num Pad")
        self.check_numpad.setObjectName("check_numpad")
        self.top_layout.addWidget(self.check_numpad)
        self.check_mouse = QtGui.QCheckBox(Keyboard)
        self.check_mouse.setText("Mouse")
        self.check_mouse.setObjectName("check_mouse")
        self.top_layout.addWidget(self.check_mouse)
        self.dialog_layout.addLayout(self.top_layout)
        self.keys_widget = QtGui.QWidget(Keyboard)
        self.keys_widget.setObjectName("keys_widget")
        self.keys_layout = QtGui.QHBoxLayout(self.keys_widget)
        self.keys_layout.setContentsMargins(0, 0, 0, 0)
        self.keys_layout.setContentsMargins(0, 0, 0, 0)
        self.keys_layout.setObjectName("keys_layout")
        self.main_widget = QtGui.QWidget(self.keys_widget)
        self.main_widget.setObjectName("main_widget")
        self.main_layout = QtGui.QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.f_row = QtGui.QHBoxLayout()
        self.f_row.setObjectName("f_row")
        self.escape = QtGui.QPushButton(self.main_widget)
        self.escape.setText("Esc")
        self.escape.setObjectName("escape")
        self.f_row.addWidget(self.escape)
        self.main_layout.addLayout(self.f_row)
        self.f_spacer = QtGui.QWidget(self.main_widget)
        self.f_spacer.setObjectName("f_spacer")
        self.main_layout.addWidget(self.f_spacer)
        self.enter_key_rows = QtGui.QHBoxLayout()
        self.enter_key_rows.setObjectName("enter_key_rows")
        self.top_letter_rows = QtGui.QVBoxLayout()
        self.top_letter_rows.setObjectName("top_letter_rows")
        self.number_row = QtGui.QHBoxLayout()
        self.number_row.setObjectName("number_row")
        self.backspace = QtGui.QPushButton(self.main_widget)
        self.backspace.setText("Backspace")
        self.backspace.setObjectName("backspace")
        self.number_row.addWidget(self.backspace)
        self.top_letter_rows.addLayout(self.number_row)
        self.letter_row_top = QtGui.QHBoxLayout()
        self.letter_row_top.setObjectName("letter_row_top")
        self.tab = QtGui.QPushButton(self.main_widget)
        self.tab.setText("Tab")
        self.tab.setObjectName("tab")
        self.letter_row_top.addWidget(self.tab)
        self.top_letter_rows.addLayout(self.letter_row_top)
        self.enter_key_rows.addLayout(self.top_letter_rows)
        self.main_layout.addLayout(self.enter_key_rows)
        self.letter_row_middle = QtGui.QHBoxLayout()
        self.letter_row_middle.setObjectName("letter_row_middle")
        self.capslock = QtGui.QPushButton(self.main_widget)
        self.capslock.setText("Caps Lock")
        self.capslock.setObjectName("capslock")
        self.letter_row_middle.addWidget(self.capslock)
        self.main_layout.addLayout(self.letter_row_middle)
        self.letter_row_bottom = QtGui.QHBoxLayout()
        self.letter_row_bottom.setObjectName("letter_row_bottom")
        self.lshift = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lshift.setFont(font)
        self.lshift.setText("Shift")
        self.lshift.setObjectName("lshift")
        self.letter_row_bottom.addWidget(self.lshift)
        self.rshift = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.rshift.setFont(font)
        self.rshift.setText("Shift")
        self.rshift.setObjectName("rshift")
        self.letter_row_bottom.addWidget(self.rshift)
        self.main_layout.addLayout(self.letter_row_bottom)
        self.bottom_row = QtGui.QHBoxLayout()
        self.bottom_row.setObjectName("bottom_row")
        self.lctrl = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lctrl.setFont(font)
        self.lctrl.setText("Ctrl")
        self.lctrl.setObjectName("lctrl")
        self.bottom_row.addWidget(self.lctrl)
        self.lwin = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lwin.setFont(font)
        self.lwin.setText("Win")
        self.lwin.setObjectName("lwin")
        self.bottom_row.addWidget(self.lwin)
        self.lalt = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lalt.setFont(font)
        self.lalt.setText("Alt")
        self.lalt.setObjectName("lalt")
        self.bottom_row.addWidget(self.lalt)
        self.space = QtGui.QPushButton(self.main_widget)
        self.space.setText("Space")
        self.space.setCheckable(True)
        self.space.setObjectName("space")
        self.bottom_row.addWidget(self.space)
        self.ralt = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.ralt.setFont(font)
        self.ralt.setText("Alt")
        self.ralt.setObjectName("ralt")
        self.bottom_row.addWidget(self.ralt)
        self.rwin = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.rwin.setFont(font)
        self.rwin.setText("Win")
        self.rwin.setObjectName("rwin")
        self.bottom_row.addWidget(self.rwin)
        self.appskey = QtGui.QPushButton(self.main_widget)
        self.appskey.setText("AppsKey")
        self.appskey.setObjectName("appskey")
        self.bottom_row.addWidget(self.appskey)
        self.rctrl = QtGui.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.rctrl.setFont(font)
        self.rctrl.setText("Ctrl")
        self.rctrl.setObjectName("rctrl")
        self.bottom_row.addWidget(self.rctrl)
        self.bottom_row.setStretch(3, 1)
        self.main_layout.addLayout(self.bottom_row)
        self.keys_layout.addWidget(self.main_widget)
        self.dialog_layout.addWidget(self.keys_widget)
        self.bottom_layout = QtGui.QHBoxLayout()
        self.bottom_layout.setContentsMargins(-1, 15, -1, -1)
        self.bottom_layout.setObjectName("bottom_layout")
        self.a2ok_button = QtGui.QPushButton(Keyboard)
        self.a2ok_button.setText("OK")
        self.a2ok_button.setObjectName("a2ok_button")
        self.bottom_layout.addWidget(self.a2ok_button)
        self.a2cancel_button = QtGui.QPushButton(Keyboard)
        self.a2cancel_button.setText("Cancel")
        self.a2cancel_button.setFlat(True)
        self.a2cancel_button.setObjectName("a2cancel_button")
        self.bottom_layout.addWidget(self.a2cancel_button)
        self.bottom_layout.setStretch(0, 1)
        self.dialog_layout.addLayout(self.bottom_layout)
        self.dialog_layout.setStretch(1, 1)

        self.retranslateUi(Keyboard)
        QtCore.QMetaObject.connectSlotsByName(Keyboard)

    def retranslateUi(self, Keyboard):
        Keyboard.setWindowTitle(QtGui.QApplication.translate("Keyboard", "Hotkey Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.option_button.setText(QtGui.QApplication.translate("Keyboard", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Keyboard", "Show:", None, QtGui.QApplication.UnicodeUTF8))

from a2widget import A2MoreButton
