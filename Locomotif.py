# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Mirko
"""
import sys
from PyQt4 import QtGui, QtCore
from ui.Ui_Locomotif import Ui_Locomotif
from tools.Tools_Locomotif import Tools_Locomotif

class Locomotif(QtGui.QMainWindow):
    """
    Docstring
    """
    def __init__(self, parent=None):
        """
        Docstring
        """
        # load all basic PyQt4 functions from QWidget
        QtGui.QWidget.__init__(self, parent)
        
        # load the ui
        self.ui = Ui_Locomotif()
        # Ui_Locomotif knows setupUi and retranslateUi methods
        self.ui.setupUi(self)

        # load tools
        self.tools = Tools_Locomotif()
        self.tools.setupTools(self)

# These are custom slots uses within Qt Designer
# They call the functions from Tools

    def openDataFile(self, Locomotif):
        self.tools.openDataFile(self)

    def openGPSFile(self, Locomotif):
        self.tools.openGPSFile(self)

    def openProjectFile(self, Locomotif):
        self.tools.openProjectFile(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Locomotif()
    myapp.show()
    sys.exit(app.exec_())