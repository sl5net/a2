# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eRiC\io\code\a2\ui\test\draft.ui'
#
# Created: Sun Mar  8 02:04:58 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1333, 1158)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setAutoFillBackground(False)
        self.splitter.setFrameShape(QtGui.QFrame.Box)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView2 = QtGui.QListView(self.groupBox)
        self.listView2.setObjectName("listView2")
        self.verticalLayout.addWidget(self.listView2)
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 802, 906))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.checkBox_4 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_3.addWidget(self.checkBox_6)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -478, 768, 1628))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setBold(False)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.plainTextEdit.setTabChangesFocus(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_6.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.checkBox_7 = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_8.addWidget(self.checkBox_7)
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_8.addWidget(self.pushButton_3)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_8 = QtGui.QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_9.addWidget(self.checkBox_8)
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox_6)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_9.addWidget(self.checkBox_9)
        self.verticalLayout_8.addWidget(self.groupBox_6)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setMinimumSize(QtCore.QSize(0, 20))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.groupBox_7 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_7)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.groupBox_7)
        self.commandLinkButton_2.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCheckable(True)
        self.commandLinkButton_2.setChecked(False)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.horizontalLayout_2.addWidget(self.commandLinkButton_2)
        self.verticalLayout_8.addWidget(self.groupBox_7)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.frame_2 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_2 = QtGui.QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_10.addWidget(self.checkBox_2)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.groupBox_8 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_11.addWidget(self.lineEdit_2)
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_8)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_2.setBaseSize(QtCore.QSize(0, 200))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_11.addWidget(self.textEdit_2)
        self.verticalLayout_8.addWidget(self.groupBox_8)
        self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_8.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_8.addWidget(self.pushButton_6)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1333, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "modules", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Module XY", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "A Text: A description text that mumbles across the window with so called words compromised of \"letters\" and punctuation. Sometimes it even has a meaning!", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "a checkbox that does something", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "A Button that calls some action", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox enablable", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_6.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "normal mode", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "module information:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "display name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "module name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "description:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A Text: A description text that mumbles across the window with so called words compromised of &quot;letters&quot; and punctuation. Sometimes it even has a meaning!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("MainWindow", "asdasdf\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "author:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setText(QtGui.QApplication.translate("MainWindow", "my name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "version:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setText(QtGui.QApplication.translate("MainWindow", "0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setText(QtGui.QApplication.translate("MainWindow", "a checkbox that does something", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "A Button that calls some action", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox enablable", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_8.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_9.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "new element", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("MainWindow", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton_2.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "This is something for a Text Label", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("MainWindow", "Edit Text:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("MainWindow", "Module1_Text", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is something for a Text Label</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "edit mode", None, QtGui.QApplication.UnicodeUTF8))

