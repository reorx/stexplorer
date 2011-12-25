# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Dec 25 18:51:16 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

# fix py2exe uninclude package problem
#import sip #@UnusedImport

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(383, 256)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 241, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 60, 341, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "ID3 auto fix", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Song id/url", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 130, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(290, 180, 71, 23))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "about", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionST_Explorer = QtGui.QAction(MainWindow)
        self.actionST_Explorer.setCheckable(False)
        self.actionST_Explorer.setChecked(False)
        self.actionST_Explorer.setEnabled(True)
        self.actionST_Explorer.setText(QtGui.QApplication.translate("MainWindow", "ST Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionST_Explorer.setObjectName(_fromUtf8("actionST_Explorer"))
        self.menuAbout.addAction(self.actionST_Explorer)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupData(self):
        self.getSettings()
        self.proc = {}

    def retranslateUi(self, MainWindow):
        pass
    
    def getSettings(self):
        class Settings: pass
        self.settings = Settings()
        self.settings.download = {
            'chunk_size': 1024*100,
        }
    def FN_downloadBylineText(self):
        from cmd_line import get_songid_from_alternative
        from parse import get_songinfo, make_fpath
        from downloader import fetch_file_resp
        
        lineText = self.lineEdit.text().__str__()
        songid = get_songid_from_alternative(lineText)
        songinfo = get_songinfo(songid)
        
        resp = fetch_file_resp(songinfo['_mediaurl'])
        fpath = make_fpath(songinfo)
        with open(fpath, 'wb') as f:
            chunk_size = self.settings.download['chunk_size']
            song_size = int(resp.info().getheaders('Content-Length')[0])
            song_size_d = 0
            while True:
                buf = resp.read(chunk_size)
                if not buf: break
                f.write(buf)
                self.changeProgressBar(100*float(song_size_d)/float(song_size))
                song_size_d += chunk_size
            self.changeProgressBar(100)
    
    def start(self):
        self.pushButton.setEnabled(False)
        self.FN_downloadBylineText()
        self.pushButton.setEnabled(True)

    def changeProgressBar(self, value):
        self.progressBar.setProperty("value", int(value))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupData()
    MainWindow.show()
    sys.exit(app.exec_())

