# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
import os
from PyQt4 import QtCore, QtGui;
from config.Config_Configuration import configData
from polyline.codec import PolylineCodec as pcod

DefaultFilter = "GPS Files (*.gps *.kml *.xml);;DataFiles (*.txt *.csv);;Project Files (*.prj *.py);;Images (*.png *.xpm *.jpg);;All Files (*.*)"
GPSFilter = "GPS Files (*.gps *.kml *.xml)"
DataFilter = "DataFiles (*.txt *.csv)"
ProjectFilter = "Project Files (*.prj *.py)"

class Tools_Locomotif(object):
	"""
	Docstring
	"""
	
	def setupTools(self):
		self.currentFilename = "tbd"
    	
	def selectDataFile(self):
		os.chdir( configData.getDataPath() )
		return self.selectUserFile("Data",DataFilter)

	def selectGPSFile(self):
		return self.selectUserFile("GPS",GPSFilter)

	def selectProjectFile(self):
		return self.selectUserFile("Project",ProjectFilter)

	def selectAnyFile(self):
		return self.selectUserFile("Datei")
		
	def selectUserFile(self, fcaption, selectedFilter="*.*"):
		""" Function to select a filename from disk """
		ofDialog = QtGui.QFileDialog(None)
		selectedFileName = ofDialog.getOpenFileName(None, "Open "+fcaption+" File", ".", DefaultFilter, selectedFilter )
		return selectedFileName

	def readDataFile(self, filePathAndName ):
		""" Function to read textfile from disk """
		result = QtCore.QString()
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		while (not istream.atEnd()):
			line = istream.readLine()
			result.append( line )
			result.append( "\n" )
		fhdl.close()
		return result

	def showInfo(self, label, text):
		msgBox = QtGui.QMessageBox(None)
		msgBox.setWindowTitle(label)
		msgBox.setText(text)
		msgBox.exec_()

	def showError(self, label, text):
		msgBox = QtGui.QMessageBox(None)
		msgBox.setWindowTitle(label)
		msgBox.setText(text)
		msgBox.exec_()

	def encodeGoogleMapsPath( self, srcPoints ):
		"""
		Punkteliste fuer Path auf Googla maps codieren
		"""
		result = ""
		# variante 2 mit echtem encoding
		# first convert to wanted list of coordinates
		coordinates = []
		points = srcPoints.split(",")
		for point in points:
			pvalues = point.split(" ")
			cpoint = []
			cpoint.append( float(pvalues[0]) )
			cpoint.append( float(pvalues[1]) )
			coordinates.append( cpoint );
		
		encoder = pcod()
		result = encoder.encode(coordinates)
		return result
