# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui;

DefaultFilter = "GPS Files (*.gps *.kml *.xml);;DataFiles (*.txt *.csv);;Project Files (*.prj *.py);;Images (*.png *.xpm *.jpg);;All Files (*.*)"
GPSFilter = "GPS Files (*.gps *.kml *.xml)"
DataFilter = "DataFiles (*.txt *.csv)"
ProjectFilter = "Project Files (*.prj *.py)"

class Tools_Locomotif(object):
    def setupTools(self, Locomotif):
    	self.currentFilename = "tbd"
    	
    def openDataFile(self, Locomotif):
        self.openUserFile(self,"Data",DataFilter);

    def openGPSFile(self, Locomotif):
        self.openUserFile(self,"GPS",GPSFilter);

    def openProjectFile(self, Locomotif):
        self.openUserFile(self,"Project",ProjectFilter);

    def openUserFile(self, Locomotif, fcaption, selectedFilter):
        self.ofDialog = QtGui.QFileDialog(None)
        tmpFileName = self.ofDialog.getOpenFileName(None, "Open "+fcaption+" File", ".", DefaultFilter, selectedFilter );
        self.msgBox = QtGui.QMessageBox(None)
        self.msgBox.setText("Selected File was \"" + tmpFileName + "\"")
        self.msgBox.exec_()
        return tmpFileName;


