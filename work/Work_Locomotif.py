# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 06:55:51 2015

@author: Thomas
"""
import sys
from PyQt4 import QtCore, QtGui, QtWebKit;
import locomotif as loc

class Work_Locomotif(object):
    """
    Docstring
    """
    def setupWork(self, locapp):
		self.initialized = 1
		self.lastcreated = 0
		locapp.ui.t1Data.setCurrentIndex(0)

    def workCleanTabs(self, locapp, rundata, cleanLevel):
		""" clean run data and display tabs """
		print "Clean Tabs"
		if cleanLevel<1:
			rundata.cleanBuffer()
			print "Clean Tabs data"
			#locapp.ui.t1FileData.setDisabled(1)
			locapp.ui.t1FileDataView.clear()
		if cleanLevel<2:
			print "Clean Tabs csv"
			#locapp.ui.t1DataFrame.setDisabled(1)
			locapp.ui.t1DataFrameView.clear()
		if cleanLevel<3:
			print "Clean Tabs poly"
			#locapp.ui.t1Polygon1.setDisabled(1)
			locapp.ui.t1Polygon1View.clear()
			#locapp.ui.t1Polygon2.setDisabled(1)
			locapp.ui.t1Polygon2View.clear()
			self.lastcreated = 0
		if cleanLevel<4:
			print "Clean Tabs map"
			scene = QtGui.QGraphicsScene();
			#locapp.ui.t1Map1.setDisabled(1)
			locapp.ui.t1Map1View.setScene(scene);
			#locapp.ui.t1Map2.setDisabled(1)
			locapp.ui.t1Map2View.setScene(scene);
			#locapp.ui.t1GoogleMaps.setDisabled(1)
		
    def workReadCSV(self, locapp, rundata):
		"""
		Get the selected Data File Name and read as CSV
		"""
		dataFilename = locapp.ui.t1LoadedDataFilename.text();
		if dataFilename == "":
			locapp.tools.showInfo( "Info", "SELECT INPUT FILE FIRST" )
			return
		# create data frame
		df = loc.read_csv( str(dataFilename), mapsta_version=100)
		rundata.setDF(df)
		locapp.ui.t1Data.setCurrentIndex(2)

    def workCreateCluster(self, locapp, rundata):
		"""
		Create Cluster for the loaded Dataframe
		"""
		df = rundata.getDF()
		#if df == None:
		#	locapp.tools.showInfo( "Info", "SELECT READ CSV FIRST" )
		#	return
		if locapp.ui.t1LoadedDataFilename.text() == "":
			locapp.tools.showInfo( "Info", "SELECT INPUT FILE FIRST" )
			return
		
		# create locomotif cluster object
		c = loc.Cluster(df)
		rundata.setCluster( c )
		locapp.ui.t1LoadedDatasets.setText(str(c.getDatasets()))
		locapp.ui.t1Data.setCurrentIndex(2)

    def workCreateVPolygone(self, locapp, rundata):
		"""
		Create Polygone from given cluster
		"""
		c = rundata.getCluster()
		if c == None:
			locapp.tools.showInfo( "Error", "FIRST YOU HAVE TO READ CSV AND CREATE DATASETS" )
			return
		if locapp.ui.t1LoadedDataFilename.text() == "":
			locapp.tools.showInfo( "Info", "SELECT INPUT FILE FIRST" )
			return
		# calculate polynoms
		res11, ref = c.voronoi('biomass')
		rundata.setVoronoi1( res11, ref )
		res12, ref = c.voronoi('diversity')
		rundata.setVoronoi2( res12, ref )
		# display
		self.putPolygonIntoTable( locapp, res11, locapp.ui.t1Polygon1View, rundata.getDataFont() )
		self.putPolygonIntoTable( locapp, res12, locapp.ui.t1Polygon2View, rundata.getDataFont() )
		# clean existing maps
		self.workCleanTabs( locapp, rundata, 3 )
		locapp.ui.t1Data.setCurrentIndex(3)
		self.lastcreated = 1

    def workCreateDPolygone(self, locapp, rundata):
		"""
		Create Polygone from given cluster
		"""
		c = rundata.getCluster()
		if c == None:
			locapp.tools.showInfo( "Error", "FIRST YOU HAVE TO READ CSV AND CREATE DATASETS" )
			return
		if locapp.ui.t1LoadedDataFilename.text() == "":
			locapp.tools.showInfo( "Info", "SELECT INPUT FILE FIRST" )
			return
		
		# Daten fuer Polygone berechnen
		res11, ref = c.delaunay('biomass')
		rundata.setDelaunay1( res11, ref )
		res12, ref = c.delaunay('diversity')
		rundata.setDelaunay2( res12, ref )
		# display
		self.putPolygonIntoTable( locapp, res11, locapp.ui.t1Polygon1View, rundata.getDataFont() )
		self.putPolygonIntoTable( locapp, res12, locapp.ui.t1Polygon2View, rundata.getDataFont() )
		# clean existing maps
		self.workCleanTabs( locapp, rundata, 3 )
		locapp.ui.t1Data.setCurrentIndex(3)
		self.lastcreated = 2

    def workCreateVMaps(self, locapp, rundata):
		# new size form input fields
		mapWidth, okw = locapp.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = locapp.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( mapWidth )
		rundata.setMapHeight( mapHeight )
		# stored polygons
		res11 = rundata.getVoronoi1();
		res12 = rundata.getVoronoi2();
		locapp.ui.t1Data.setCurrentIndex(5)
		rundata.debugRundata()

    def workCreateDMaps(self, locapp, rundata):
		# new size form input fields
		mapWidth, okw = locapp.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = locapp.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( mapWidth )
		rundata.setMapHeight( mapHeight )
		# stored polygons
		res11 = rundata.getDelaunay1();
		res12 = rundata.getDelaunay2();
		locapp.ui.t1Data.setCurrentIndex(5)
		rundata.debugRundata()

    def workCreateMaps(self, locapp, rundata):
		"""
		ReCreate the Maps for the loaded Datasets
		Use sizes from input fields
		"""
		# checks
		#if rundata.getCluster() == None:
		#	locapp.tools.showInfo( "Error", "FIRST YOU HAVE TO READ CSV AND CREATE DATASETS" )
		#	return
		if locapp.ui.t1LoadedDataFilename.text() == "":
			locapp.tools.showInfo( "Info", "SELECT INPUT FILE FIRST" )
			return
		
		# new size form input fields
		mapWidth, okw = locapp.ui.cmdMapWidth.text().toInt(10)
		mapHeight, okh = locapp.ui.cmdMapHeight.text().toInt(10)
		rundata.setMapWidth( mapWidth )
		rundata.setMapHeight( mapHeight )
		# which polygons have been created
		if self.lastcreated == 0: 
				locapp.tools.showInfo( "Error", "FIRST YOU HAVE TO CALCULATE POLYNOMS" )
				return
		if self.lastcreated == 1: 
			# stored filenames
			map1Filename = rundata.getV1Mapname()
			map2Filename = rundata.getV2Mapname()
			# stored polygons
			res11 = rundata.getVoronoi1();
			res12 = rundata.getVoronoi2();
			# create new maps for current cluster
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=map1Filename )
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=map2Filename )

		if self.lastcreated == 2: 
			# stored filenames
			map1Filename = rundata.getD1Mapname()
			map2Filename = rundata.getD2Mapname()
			# stored polygons
			res11 = rundata.getDelaunay1();
			res12 = rundata.getDelaunay2();
			# create new maps for current cluster
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res11, out_path=map1Filename )
			loc.Mapper(Style='Voronoi_index', size=(mapWidth, mapHeight), datasource=res12,out_path=map2Filename )
			
		# Show Maps
		scene1 = QtGui.QGraphicsScene();
		scene1.addPixmap( QtGui.QPixmap(map1Filename) )
		locapp.ui.t1Map1View.setScene(scene1);
		scene2 = QtGui.QGraphicsScene();
		scene2.addPixmap( QtGui.QPixmap(map2Filename) )
		locapp.ui.t1Map2View.setScene(scene2);
		locapp.ui.t1Data.setCurrentIndex(5)
		rundata.debugRundata()
		
    def readDataFileIntoTable(self, locapp, filePathAndName ):
		""" 
		Function to display textfile in table 
		"""
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		# clear table 
		locapp.ui.t1FileDataView.clear()
		initRowCount = locapp.ui.t1FileDataView.rowCount()
		# read headert line with table names
		line = istream.readLine()
		fields = line.split(';')
		numofcols = fields.count()
		locapp.ui.t1FileDataView.setHorizontalHeaderLabels( fields )
		locapp.ui.t1FileDataView.setColumnWidth(0,140)
		locapp.ui.t1FileDataView.setColumnWidth(1,140)
		# read data lines
		rowIndex = 0
		while (not istream.atEnd()):
			line = istream.readLine()
			values = line.split(';')
			numofcols = values.count()
			if rowIndex>=initRowCount:
				locapp.ui.t1FileDataView.insertRow(rowIndex)
			locapp.ui.t1FileDataView.setRowHeight(rowIndex,22)
			colIndex = 0
			for value in values:
				item = QtGui.QTableWidgetItem()
				item.setText( str(value) )
				locapp.ui.t1FileDataView.setItem( rowIndex, colIndex, item )
				# print "Zelle " + str(colIndex) + " / "+ str(rowIndex)+" = " + value
				colIndex = colIndex+1
			rowIndex = rowIndex+ 1
		fhdl.close()

    def markDataOnGoogleMap(self, locapp, filePathAndName):
		""" display google map with data points marked """
		# prepare GOOGLE MAPS url
		maphint = locapp.ui.t1GoogleMapsHint
		map = locapp.ui.t1GoogleMapsView
		url = "http://maps.google.com/maps/api/staticmap?maptype=hybrid&sensor=false&language=de"
		url = url + "&size=750x550"
		# read file and append markers
		fhdl = QtCore.QFile(filePathAndName)
		fhdl.open(QtCore.QIODevice.ReadWrite)
		istream = QtCore.QTextStream(fhdl)
		# skip header line
		line = istream.readLine()
		numl = 0
		nump = 0
		while (not istream.atEnd()):
			line = istream.readLine()
			numl = numl + 1
			values = line.split(';')
			urlpart = "&markers="+str(values[0])+","+str(values[1])
			if (len(url)+len(urlpart)) < 1850:
				url = url + "&" + urlpart
				nump = nump + 1	
			
		# display
		map.load( QtCore.QUrl(url))
		# display a hint if not all lines are displayed in the map
		if nump < numl:
			maphint.setText("ATTENTION: Big data, not all points may be displayed at the same time")

    def putCSVIntoTable(self, locapp, df ):
		""" Function display CSV in table """
		# clear table 
		locapp.ui.t1DataFrameView.clear()
		initRowCount = locapp.ui.t1DataFrameView.rowCount()
		# set table header
		colIndex = 0
		for col in df.columns:
			item = QtGui.QTableWidgetItem()
			item.setText( str(col) )
			locapp.ui.t1DataFrameView.setHorizontalHeaderItem( colIndex, item )
			colIndex = colIndex+1
		locapp.ui.t1DataFrameView.setColumnWidth(2,260)
		# display data lines
		rowIndex = 0
		for value in df.values:
			if rowIndex>=initRowCount:
				locapp.ui.t1DataFrameView.insertRow(rowIndex)
			locapp.ui.t1DataFrameView.setRowHeight(rowIndex,22)
			colIndex = 0
			# df object has always 3 columns
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[0]) )
			locapp.ui.t1DataFrameView.setItem( rowIndex, colIndex, item )
			colIndex = colIndex+1
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[1]) )
			locapp.ui.t1DataFrameView.setItem( rowIndex, colIndex, item )
			colIndex = colIndex+1
			item = QtGui.QTableWidgetItem()
			item.setText( str(value[2]) )
			locapp.ui.t1DataFrameView.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1

    def putPolygonIntoTable(self, locapp, pres, uiTable, font ):
		""" Function display Polygone in table """
		# clear table 
		uiTable.clear()

		# set table header
		item = QtGui.QTableWidgetItem()
		item.setText( "Geometry" )
		uiTable.setHorizontalHeaderItem( 0, item )
		item = QtGui.QTableWidgetItem()
		item.setText( "Value" )
		uiTable.setHorizontalHeaderItem( 1, item )
		uiTable.setColumnWidth(0,500)

		rowIndex = 0
		initRowCount = uiTable.rowCount()
		for geomvalue in pres.geometry:
			if rowIndex>=initRowCount:
				uiTable.insertRow(rowIndex)
			uiTable.setRowHeight(rowIndex,22)
			colIndex = 0
			# table has 2 columns
			item = QtGui.QTableWidgetItem()
			item.setText( str(geomvalue) )
			uiTable.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1
		
		rowIndex = 0
		initRowCount = uiTable.rowCount()
		for value in pres.value:
			if rowIndex>=initRowCount:
				uiTable.insertRow(rowIndex)
			uiTable.setRowHeight(rowIndex,22)
			colIndex = 1
			# table has 2 columns
			item = QtGui.QTableWidgetItem()
			item.setFont(font)
			item.setText( str(value) )
			uiTable.setItem( rowIndex, colIndex, item )
			rowIndex = rowIndex+ 1

    def markPolygonOnGoogleMap(self, locapp, pres):
		""" display google map with data points marked """
		# prepare GOOGLE MAPS url
		maphint = locapp.ui.t1GoogleMaps2Hint
		map = locapp.ui.t1GoogleMaps2View
		url = "http://maps.google.com/maps/api/staticmap?maptype=hybrid&sensor=false&language=de"
		url = url + "&size=750x550"
		# scan polygone and append markers
		num = 0
		for geomvalue in pres.geometry:
			# transform polygon (geomvalue) into googlemaps path
			# sample
			# POLYGON ((47.990827281500003 7.88942045146,
			#           48.003640800699998 7.86850930989,
			#           48.001608965734277 7.86510335449,
			#           47.988457948584305 7.86510335449,
			#           47.982788794699999 7.89045027516,
			#           47.990827281500003 7.88942045146
			#         ))
			line = str(geomvalue)
			line = line.replace( "POLYGON ((", "")
			line = line.replace( "))", "")
			# into googlepath
			# path=color:0x0000ff|weight:5|
			#   40.737102,-73.990318|
			#   40.749825,-73.987963|
			#   40.752946,-73.987384|
			#   40.755823,-73.986397

			# das waere die schnelle variante
			#line = line.replace( ",", "|")
			#line = line.replace( " ", ",")
			#urlpart = "path=color:0x0000ff|"+line
			
			# 2 variante mit weniger kommastellen der punkte
			#urlpart = "path=color:0x0000ff"
			#points = line.split(",")
			#for point in points:
			#	# point2 = point.replace(" ", ",")
			#	pvalues = point.split(" ")
			#	latval = float( str('{:10.4f}'.format(float(pvalues[0]))) )
			#	lonval = float( str('{:10.4f}'.format(float(pvalues[1]))) )
			#	urlpart = urlpart + '|' + str(latval) + "," + str(lonval)
			
			# 3 variante mit codierten paths
			encodedPath = locapp.tools.encodeGoogleMapsPath(line)
			urlpart = "path=enc:" + encodedPath
			
			# total path length must be < 2048
			# internal conversion to cgi causes special chars to be length 3
			# so we calculate with a len < 1950
			# if num < 29:
			if (len(url)+len(urlpart)) < 1850:
				url = url + "&" + urlpart
				num = num + 1	

		# display
		map.load( QtCore.QUrl(url))
		# display a hint if not all lines are displayed in the map
		if num < len(pres.geometry):
			maphint.setText("ATTENTION: Big data, not all polygones may be displayed at the same time")
			