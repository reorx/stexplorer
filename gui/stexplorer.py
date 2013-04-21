#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Dec 25 18:51:16 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!


import sys
import logging
import functools
from PyQt4 import QtCore, QtGui

import coreui


class Settings(object):
    chunk_size = 1024 * 100


class STEXMainWindow(QtGui.QMainWindow, coreui.Ui_MainWindow):
    def __init__(self):
        super(STEXMainWindow, self).__init__()
        self.setupUi(self)
        self.setupData()

    def setupData(self):
        self.settings = Settings()

    def menuExample(self):
        pass

    def async_download(self, callback):
        from stex.cmd_line import get_songid_from_alternative
        from stex.parse import get_songinfo, make_fpath
        from stex.downloader import fetch_file_resp

        lineText = self.lineEdit.text().__str__()
        songid = get_songid_from_alternative(lineText)
        songinfo = get_songinfo(songid)

        resp = fetch_file_resp(songinfo['_mediaurl'])
        fpath = make_fpath(songinfo)

        with open(fpath, 'wb') as f:
            chunk_size = self.settings.chunk_size
            song_size = int(resp.info().getheaders('Content-Length')[0])
            song_size_d = 0

            while True:
                buf = resp.read(chunk_size)
                if not buf:
                    break
                f.write(buf)
                self.changeProgressBar(100 * float(song_size_d) / float(song_size))
                song_size_d += chunk_size

            self.changeProgressBar(100)
        self.progressBar.reset()

        callback()

    def start(self):
        """
        This method will be triggered by clicking "Start" button
        """
        logging.info('Start button triggered')
        self.togglePushButton(False)
        self.async_download(functools.partial(self.togglePushButton, True))

    def changeProgressBar(self, value):
        self.progressBar.setValue(int(value))

    def togglePushButton(self, flag):
        if flag:
            self.pushButton.setEnabled(True)
            self.pushButton.setText('Start')
        else:
            self.pushButton.setEnabled(False)
            self.pushButton.setText('--')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app = QtGui.QApplication(sys.argv)

    win = STEXMainWindow()
    win.show()

    sys.exit(app.exec_())
