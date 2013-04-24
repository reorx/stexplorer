# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core.ui'
#
# Created: Wed Apr 24 16:15:39 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(378, 271)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 241, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 90, 341, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 160, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(290, 200, 71, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 241, 23))
        self.lineEdit_2.setStyleSheet(_fromUtf8("QLineEdit {color: #555;}"))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionST_Explorer = QtGui.QAction(MainWindow)
        self.actionST_Explorer.setCheckable(False)
        self.actionST_Explorer.setChecked(False)
        self.actionST_Explorer.setEnabled(True)
        self.actionST_Explorer.setObjectName(_fromUtf8("actionST_Explorer"))
        self.actionAn_example = QtGui.QAction(MainWindow)
        self.actionAn_example.setObjectName(_fromUtf8("actionAn_example"))
        self.actionAuthor = QtGui.QAction(MainWindow)
        self.actionAuthor.setObjectName(_fromUtf8("actionAuthor"))
        self.menuAbout.addAction(self.actionST_Explorer)
        self.menuAbout.addAction(self.actionAuthor)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAn_example)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.start)
        QtCore.QObject.connect(self.actionAn_example, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.menuExample)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.checkBox.setText(_translate("MainWindow", "ID3 auto fix", None))
        self.label.setText(_translate("MainWindow", "Song id/url", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.label_2.setText(_translate("MainWindow", "Directory", None))
        self.menuAbout.setTitle(_translate("MainWindow", "about", None))
        self.actionST_Explorer.setText(_translate("MainWindow", "ST Explorer", None))
        self.actionAn_example.setText(_translate("MainWindow", "an example", None))
        self.actionAuthor.setText(_translate("MainWindow", "author", None))

