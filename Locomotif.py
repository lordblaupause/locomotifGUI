# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Mirko
"""
import sys
import os
from PyQt4 import QtGui, QtCore
from ui.Ui_Locomotif import Ui_Locomotif
from tools.Tools_Locomotif import Tools_Locomotif
from work.Work_Locomotif import Work_Locomotif
from data.Rundata_Locomotif import Rundata_Locomotif
from config.Config_Configuration import *
from ConfigDialog import ConfigDialog
import locomotif as loc

# globaler Datenspeicher
rundata = Rundata_Locomotif()

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
		self.ui.setupUi(self)

		# setup global config
		configData.setupConfig()

		# load tools
		self.tools = Tools_Locomotif()
		self.tools.setupTools()
		# setup global rundata
		rundata.setupRundata()
		# load work
		self.work = Work_Locomotif()
		self.work.setupWork(self)
        
		# create font for data display
		dataFont = QtGui.QFont()
		dataFont.setStyleHint(QtGui.QFont.Courier)
		rundata.setDataFont( dataFont )
		
		# more initialisations
		self.ui.mainDataDisplay.setTabText(0,"Data Record 1")
		self.ui.mainDataDisplay.setTabText(1,"Data Record 2")
		self.ui.mainDataDisplay.setCurrentIndex(0)
		
		# load configuration values and stor in config class
		__base__ = os.path.abspath(os.path.dirname(__file__))
		configData.initConfig( __base__ )
		configData.debugConfig()

		# initial values for maps
		mapWidth = configData.getMapWidth()
		rundata.setMapWidth( mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = configData.getMapHeight()
		rundata.setMapHeight( mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))
		
# These are custom slots used within Qt Designer

	def doConfigDialog(self, Locomotif):
		print "open configuration dialog"
		dialog = ConfigDialog(self)
		dialog.setModal(1)
		ret = dialog.exec_()
		# transfer some values
		mapWidth = configData.getMapWidth()
		rundata.setMapWidth( mapWidth )
		self.ui.cmdMapWidth.setText(str(mapWidth))
		mapHeight = configData.getMapHeight()
		rundata.setMapHeight( mapHeight )
		self.ui.cmdMapHeight.setText(str(mapHeight))
				
	def openDataFile(self, Locomotif):
		""" Load a Data File for Further Processing """
		dataFilename = self.tools.selectDataFile()
		if dataFilename == "":
			self.tools.showInfo( "Info", "NO FILE SELECTED" )
			return 0
		
		# deactivate all tabs 
		self.work.workCleanTabs( self, rundata, 0 )
		self.ui.t1Data.setCurrentIndex(0)
		
		# store nme in global data	
		rundata.setDataFileName( dataFilename )
		self.ui.loadedDataFilename.setText(dataFilename)
		self.ui.t1LoadedDataFilename.setText(dataFilename)
		# load and display initial data
		self.work.readDataFileIntoTable( self, dataFilename )
		self.work.markDataOnGoogleMap( self, dataFilename )
		
		# initial names for maps
		mapv1Filename = configData.getMapPath() + "/map1_v.png"
		mapv2Filename = configData.getMapPath() + "/map2_v.png"
		rundata.setV1Mapname( mapv1Filename )
		rundata.setV2Mapname( mapv2Filename )
		mapd1Filename = configData.getMapPath() + "/map1_d.png"
		mapd2Filename = configData.getMapPath() + "/map2_d.png"
		rundata.setD1Mapname( mapd1Filename )
		rundata.setD2Mapname( mapd2Filename )
		
		return 1
		
	def openGPSFile(self, Locomotif):
		""" Load a GPS File for Further Processing """
		gpsFileName = self.tools.selectGPSFile()

	def openProjectFile(self, Locomotif):
		""" Load a Project File for Further Processing """
		projectFileName = self.tools.selectProjectFile()

	def doReadCSV(self, Locomotif):
		"""
		Reload the CSV DataFrames with the given name
		"""
		self.work.workReadCSV( self, rundata )
		df = rundata.getDF()
		self.work.putCSVIntoTable( self, df )
		"""
		Create Cluster for the loaded Dataframe
		"""
		self.work.workCreateCluster( self, rundata )

	def doCreateVPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateVPolygone(self, rundata )
		self.work.markPolygonOnGoogleMap(self,rundata.getVoronoi1())

	def doCreateDPolygone(self, Locomotif):
		"""
		Create Polygone from given cluster
		"""
		self.work.workCreateDPolygone(self, rundata )
		self.work.markPolygonOnGoogleMap(self,rundata.getDelaunay1())

	def doCreateMaps(self, Locomotif):
		"""
		Slot for button CreateMap
		"""
		self.work.workCreateMaps( self, rundata )


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Locomotif()
    myapp.show()
    sys.exit(app.exec_())