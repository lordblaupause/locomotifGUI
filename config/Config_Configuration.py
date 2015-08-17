# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
import os
from PyQt4 import QtCore;

class Config_Configuration(object):
	"""
	Docstring
	"""
	def setupConfig(self):
		self.dataPath = ""
		self.mapPath = ""
		self.mapWidth = 700
		self.mapHeight = 600

	def debugConfig(self):
		print "DataPath = " + self.dataPath
		print "MapPath = " + self.mapPath
		print "MapWidth = " + str(self.mapWidth)
		print "MapHeight = " + str(self.mapHeight)

	def initConfig(self, homePath):
		# read configuration file
		cfgPath = homePath + "\\etc"
		cfgFile = cfgPath + "\\lcGui.resources"
		# TODO READ
		parentDir = os.path.dirname( homePath )
		self.dataPath = parentDir + "\\sample_data"
		self.mapPath = parentDir + "\\results"
		self.mapWidth = 700
		self.mapHeight = 600

	def setDataPath( self, path ):
		self.dataPath = path

	def getDataPath( self ):
		return self.dataPath

	def setMapPath( self, path ):
		self.mapPath = path

	def getMapPath( self ):
		return self.mapPath

	def setMapWidth( self, width ):
		self.mapWidth = width

	def getMapWidth( self ):
		return self.mapWidth

	def setMapHeight( self, height ):
		self.mapHeight = height

	def getMapHeight( self ):
		return self.mapHeight

# Global Config Data to be used throughout the application
		
configData = Config_Configuration()

		