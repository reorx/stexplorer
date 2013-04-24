#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Dec 25 18:51:16 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!


import os
import sys
import logging
import types
from PyQt4 import QtCore, QtGui
from stex.cmd_line import get_songid_from_alternative
from stex.parse import get_songinfo
from stex.downloader import fetch_file_resp, mkdir

import coreui


# PROGRESS_BAR_SIGNAL = QtCore.SIGNAL('change(int)')
_fromUtf8 = QtCore.QString.fromUtf8


class Settings(object):
    chunk_size = 1024 * 100


def bindEvent(obj, name, method):
    """
    Bind event to QWidget instance,
    this function actually do dynamically method binding to the instance,
    for which the relevant event handling method will be overrided.
    """
    setattr(obj, name,
            types.MethodType(method, obj, obj.__class__))


def truncatePath(path, limit=35):
    if path.endswith(os.sep):
        path = path.rstrip(os.sep)
    path_splits = path.split(os.sep)
    if path_splits <= 2:
        return path
    item_number = len(path_splits)
    pos = 2
    while item_number - pos >= 2:
        truncated = os.sep.join(path_splits[:-pos] + ['...', path_splits[-1]])
        print truncated
        if len(truncated) < 35:
            return truncated
        pos += 1
    return path


def popDirectoryDialog(lineEdit, event):
    logging.info('lineEdit_2 clicked, %s', event)
    dirpath = QtGui.QFileDialog.getExistingDirectory()
    if dirpath:
        lineEdit._value = dirpath
        lineEdit.setToolTip(dirpath)
        lineEdit.setText(truncatePath(str(dirpath)))


class STEXMainWindow(QtGui.QMainWindow, coreui.Ui_MainWindow):
    def __init__(self):
        super(STEXMainWindow, self).__init__()
        self.setupUi(self)

        self.settings = Settings()
        self._started = False
        self._root_path = os.path.abspath(os.getcwd())

        # Reset window size to be fixed
        self.setFixedSize(self.size())

        self.lineEdit_2._value = os.path.join(self._root_path, 'downloads')
        self.lineEdit_2.setToolTip(self.lineEdit_2._value)
        self.lineEdit_2.setText('./downloads')
        bindEvent(self.lineEdit_2, 'mousePressEvent', popDirectoryDialog)
        #win.connect(self.lineEdit_2, QtCore.SIGNAL('directory()'), win.)

    def menuExample(self):
        pass

    def start(self):
        """
        This method will be triggered by clicking "Start" button
        """
        logging.debug('Start button triggered')
        if self._started:
            logging.warning('Already started')
            return
        self._started = True
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        url = self.lineEdit.text().__str__()

        self.thread = DownloadThread(self, url)
        self.thread.start()

    def done(self):
        self.changeProgressBar(100)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self._started = False

    def changeProgressBar(self, value):
        self.progressBar.setValue(int(value))

    def resetProgressBar(self):
        logging.debug('Reset progress bar')
        self.changeProgressBar(100)
        self.progressBar.reset()

    def getDirpath(self):
        # Remember to transform QString to str
        return str(self.lineEdit_2._value)


class DownloadThread(QtCore.QThread):
    def __init__(self, win, url):
        super(DownloadThread, self).__init__()
        win.connect(self, QtCore.SIGNAL('change(int)'), win.changeProgressBar)
        win.connect(self, QtCore.SIGNAL('done()'), win.done)
        self._win = win
        self._url = url

    def run(self):
        songid = get_songid_from_alternative(self._url)
        songinfo = get_songinfo(songid)

        dirpath = self._win.getDirpath()
        mkdir(dirpath)
        filepath = os.path.join(dirpath, songinfo['filename'])

        resp = fetch_file_resp(songinfo['_mediaurl'])

        with open(filepath, 'wb') as f:
            chunk_size = self._win.settings.chunk_size
            song_size = int(resp.info().getheaders('Content-Length')[0])
            song_size_d = 0

            while True:
                buf = resp.read(chunk_size)
                if not buf:
                    break
                f.write(buf)
                process_rate = 100 * float(song_size_d) / float(song_size)
                self.emit(QtCore.SIGNAL('change(int)'), process_rate)
                song_size_d += chunk_size

        self.emit(QtCore.SIGNAL('done()'))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app = QtGui.QApplication(sys.argv)

    win = STEXMainWindow()
    win.show()

    sys.exit(app.exec_())
