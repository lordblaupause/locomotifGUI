# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
#from PyQt4 import QtCore, QtGui;

class Rundata_Locomotif(object):
	"""
	Docstring
	"""
	def setupRundata(self):
		self.dataFilename = ""
		self.gpsFilename = ""
		self.projectFilename = ""
		self.df = None
		self.cluster = None
		self.voronoi1values = None
		self.voronoi1ref = None
		self.voronoi2values = None
		self.voronoi2ref = None
		self.delaunay1values = None
		self.delaunay1ref = None
		self.delaunay2values = None
		self.delaunay2ref = None
		self.mapwidth = 0
		self.mapheight = 0
		self.mapv1filename = ""
		self.mapv2filename = ""
		self.mapd1filename = ""
		self.mapd2filename = ""

	def debugRundata(self):
		print "DataFilename = " + self.datafilename
		print "GPSFilename = " + self.gpsFilename
		print "ProjectFilename = " + self.projectFilename
		print "DataFrame = "
		print self.df
		print "Cluster Datasets = "
		print self.cluster.getDatasets()
		print "Voronoi1 REF = " + self.voronoi1ref
		print "Voronoi1 values = "
		print self.voronoi1values
		print "Voronoi2 REF = " + self.voronoi2ref
		print "Voronoi2 values = "
		print self.voronoi2values
		print "Delaunay1 REF = " + self.delaunay1ref
		print "Delaunay1 values = "
		print self.delaunay1values
		print "Delaunay2 REF = " + self.delaunay2ref
		print "Delaunay2 values = "
		print self.delaunay2values
		print "Map Width = " + str(self.mapwidth)
		print "Map Height = " + str(self.mapheight)
		print "MapV1Filename = " + self.mapv1filename
		print "MapV2Filename = " + self.mapv2filename
		print "MapD1Filename = " + self.mapd1filename
		print "MapD2Filename = " + self.mapd2filename

	def cleanBuffer( self ):
		print "Clean RUndata"
		self.dataFilename = ""
		self.gpsFilename = ""
		self.projectFilename = ""
		self.df = None
		self.cluster = None
		self.voronoi1values = None
		self.voronoi1ref = None
		self.voronoi2values = None
		self.voronoi2ref = None
		self.delaunay1values = None
		self.delaunay1ref = None
		self.delaunay2values = None
		self.delaunay2ref = None
		self.mapwidth = 0
		self.mapheight = 0
		self.mapv1filename = ""
		self.mapv2filename = ""
		self.mapd1filename = ""
		self.mapd2filename = ""
	
	def setDataFont( self, font ):
		self.datafont = font

	def getDataFont( self ):
		return self.datafont

	def setDataFileName( self, fname ):
		self.datafilename = str(fname)

	def setGpsFileName( self, fname ):
		self.gpsFilename = str(fname)

	def setProjectFileName( self, fname ):
		self.projectFilename = str(fname)
		
	def setDF( self, df ):
		self.df = df		

	def getDF( self ):
		return self.df		

	def setCluster( self, cluster ):
		self.cluster = cluster	

	def getCluster( self ):
		return self.cluster

	def setVoronoi1( self, res, ref ):
		self.voronoi1values = res
		self.voronoi1ref = str(ref)

	def getVoronoi1( self ):
		return self.voronoi1values

	def setVoronoi2( self, res, ref ):
		self.voronoi2values = res	
		self.voronoi2ref = str(ref)

	def getVoronoi2( self ):
		return self.voronoi2values	

	def setDelaunay1( self, res, ref ):
		self.delaunay1values = res
		self.delaunay1ref = str(ref)

	def getDelaunay1( self ):
		return self.delaunay1values

	def setDelaunay2( self, res, ref ):
		self.delaunay2values = res	
		self.delaunay2ref = str(ref)

	def getDelaunay2( self ):
		return self.delaunay2values	

	def setMapWidth( self, w ):
		self.mapwidth = w
		
	def setMapHeight( self, h ):
		self.mapheight = h
		
	def setV1Mapname( self, filename ):
		self.mapv1filename = filename

	def getV1Mapname( self ):
		return self.mapv1filename

	def setV2Mapname( self, filename ):
		self.mapv2filename = filename

	def getV2Mapname( self ):
		return self.mapv2filename

	def setD1Mapname( self, filename ):
		self.mapd1filename = filename

	def getD1Mapname( self ):
		return self.mapd1filename

	def setD2Mapname( self, filename ):
		self.mapd2filename = filename

	def getD2Mapname( self ):
		return self.mapd2filename


		
		