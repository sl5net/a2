'''
Text field that automatically gets bigger the more lines you add.

@created: 01.11.2016
@author: eric
'''
from PySide import QtGui, QtCore


class a2TextField(QtGui.QPlainTextEdit):

    def __init__(self, parent=None, *args, **kwargs):
        super(a2TextField, self).__init__(parent, *args, **kwargs)
        # self.leaveEvent()
        self.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        size_policy.setVerticalStretch(0)
        size_policy.setHorizontalStretch(0)
        self.setSizePolicy(size_policy)

        self.blockCountChanged.connect(self._set_height_to_block_count)
        self._cursor_height = None
        self._backup_height = 16

    def showEvent(self, *args, **kwargs):
        self._set_height_to_block_count()
        return QtGui.QPlainTextEdit.showEvent(self, *args, **kwargs)

    def setText(self, this):
        self.setPlainText(this)
        self._set_height_to_block_count()

    def _set_height_to_block_count(self, block_count=None):
        if block_count is None:
            block_count = self.blockCount()

        cursor_height = self.cursorRect().height()
        if cursor_height:
            self._cursor_height = cursor_height
        elif self._cursor_height is None:
            cursor_height = self._backup_height
        else:
            cursor_height = self._cursor_height

        magic_height = (cursor_height / 3) + 5
        height = (cursor_height * block_count) + magic_height

        self.setMinimumHeight(height)
        self.setMaximumHeight(height)


class a2CodeField(a2TextField):
    """
    Just subclassed to be identifyable via CSS to apply a monospace font.
    """
    def __init__(self, parent=None, *args, **kwargs):
        a2TextField.__init__(self, parent, *args, **kwargs)
