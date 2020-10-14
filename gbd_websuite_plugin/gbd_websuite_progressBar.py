###
# standard library imports
###
import os
import sys

###
# third party imports
###


# python bindings for QT application Framework
from qgis.PyQt import QtGui, QtWidgets, uic, QtCore

# 
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'gbd_websuite_progressBar_base.ui'))

'''class progressBarThread(QtCore.QThread):
    change_value = QtCore.pyqtSignal(int)
    def run(self, value):
        while value < 100:
            self.change_value.emit(value)'''

class progressBar(QtWidgets.QWidget, FORM_CLASS):

    def __init__(self, parent = None):
        super(progressBar, self).__init__(parent)

        self.setupUi(self)
        self.center()

    '''def startProgressBar(self):
        self.thread = progressBarThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()'''

    '''def setProgressVal(self, val):
        self.progressBar.setValue(val)'''

    def center(self):

        '''
        Center the Mainwindow in the active Screen
        https://stackoverflow.com/questions/20243637/pyqt4-center-window-on-active-screen
        '''
        
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())