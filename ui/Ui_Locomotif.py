# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Locomotif.ui'
#
# Created: Mon Jul 27 00:33:21 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Locomotif(object):
    def setupUi(self, Locomotif):
        Locomotif.setObjectName(_fromUtf8("Locomotif"))
        Locomotif.resize(873, 682)
        self.centralwidget = QtGui.QWidget(Locomotif)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.qwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot.setGeometry(QtCore.QRect(40, 120, 551, 311))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        Locomotif.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Locomotif)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuWindow = QtGui.QMenu(self.menuView)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        Locomotif.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Locomotif)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Locomotif.setStatusBar(self.statusbar)
        self.QuickCommand = QtGui.QDockWidget(Locomotif)
        self.QuickCommand.setAcceptDrops(True)
        self.QuickCommand.setAutoFillBackground(False)
        self.QuickCommand.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.QuickCommand.setFloating(False)
        self.QuickCommand.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickCommand.setObjectName(_fromUtf8("QuickCommand"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.formLayout = QtGui.QFormLayout(self.dockWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cmdLoadGPSFile = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadGPSFile.setObjectName(_fromUtf8("cmdLoadGPSFile"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.cmdLoadGPSFile)
        self.cmdLoadProject = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadProject.setObjectName(_fromUtf8("cmdLoadProject"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.cmdLoadProject)
        self.cmdLoadDataFile = QtGui.QPushButton(self.dockWidgetContents)
        self.cmdLoadDataFile.setObjectName(_fromUtf8("cmdLoadDataFile"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.cmdLoadDataFile)
        self.QuickCommand.setWidget(self.dockWidgetContents)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickCommand)
        self.QuickStatus = QtGui.QDockWidget(Locomotif)
        self.QuickStatus.setAutoFillBackground(False)
        self.QuickStatus.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QuickStatus.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickStatus.setObjectName(_fromUtf8("QuickStatus"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.label = QtGui.QLabel(self.dockWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.loadedDataFileName = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.loadedDataFileName.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.loadedDataFileName.setObjectName(_fromUtf8("loadedDataFileName"))
        self.QuickStatus.setWidget(self.dockWidgetContents_2)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.QuickStatus)
        self.QuickEdit = QtGui.QDockWidget(Locomotif)
        self.QuickEdit.setEnabled(False)
        self.QuickEdit.setAutoFillBackground(False)
        self.QuickEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QuickEdit.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.QuickEdit.setObjectName(_fromUtf8("QuickEdit"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.QuickEdit.setWidget(self.dockWidgetContents_4)
        Locomotif.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.QuickEdit)
        self.actionQuit = QtGui.QAction(Locomotif)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuick_Command_Box = QtGui.QAction(Locomotif)
        self.actionQuick_Command_Box.setCheckable(True)
        self.actionQuick_Command_Box.setChecked(True)
        self.actionQuick_Command_Box.setObjectName(_fromUtf8("actionQuick_Command_Box"))
        self.actionHelp = QtGui.QAction(Locomotif)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionOpen_GPS_File = QtGui.QAction(Locomotif)
        self.actionOpen_GPS_File.setObjectName(_fromUtf8("actionOpen_GPS_File"))
        self.actionOpen_Project = QtGui.QAction(Locomotif)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionStatus_Box = QtGui.QAction(Locomotif)
        self.actionStatus_Box.setCheckable(True)
        self.actionStatus_Box.setChecked(True)
        self.actionStatus_Box.setObjectName(_fromUtf8("actionStatus_Box"))
        self.menuFile.addAction(self.actionOpen_GPS_File)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuWindow.addAction(self.actionQuick_Command_Box)
        self.menuWindow.addAction(self.actionStatus_Box)
        self.menuView.addAction(self.menuWindow.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(Locomotif)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Locomotif.close)
        QtCore.QObject.connect(self.actionQuick_Command_Box, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickCommand.show)
        QtCore.QObject.connect(self.actionStatus_Box, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.QuickStatus.show)
        QtCore.QObject.connect(self.actionOpen_Project, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openProjectFile)
        QtCore.QObject.connect(self.cmdLoadGPSFile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openGPSFile)
        QtCore.QObject.connect(self.cmdLoadProject, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openProjectFile)
        QtCore.QObject.connect(self.actionOpen_GPS_File, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), Locomotif.openGPSFile)
        QtCore.QObject.connect(self.cmdLoadDataFile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Locomotif.openDataFile)
        QtCore.QMetaObject.connectSlotsByName(Locomotif)

    def retranslateUi(self, Locomotif):
        Locomotif.setWindowTitle(_translate("Locomotif", "MainWindow", None))
        self.menuFile.setTitle(_translate("Locomotif", "File", None))
        self.menuView.setTitle(_translate("Locomotif", "View", None))
        self.menuWindow.setTitle(_translate("Locomotif", "Window", None))
        self.QuickCommand.setWhatsThis(_translate("Locomotif", "<html><head/><body><p>Bla Bla ...</p></body></html>", None))
        self.QuickCommand.setWindowTitle(_translate("Locomotif", "Commands", None))
        self.cmdLoadGPSFile.setText(_translate("Locomotif", "open GPS File", None))
        self.cmdLoadProject.setText(_translate("Locomotif", "open Project", None))
        self.cmdLoadDataFile.setText(_translate("Locomotif", "open Data File", None))
        self.QuickStatus.setWindowTitle(_translate("Locomotif", "Status", None))
        self.label.setText(_translate("Locomotif", "Datendatei", None))
        self.QuickEdit.setWindowTitle(_translate("Locomotif", "Edit", None))
        self.actionQuit.setText(_translate("Locomotif", "Quit", None))
        self.actionQuick_Command_Box.setText(_translate("Locomotif", "Quick Command Box", None))
        self.actionHelp.setText(_translate("Locomotif", "Help", None))
        self.actionOpen_GPS_File.setText(_translate("Locomotif", "Open GPS File...", None))
        self.actionOpen_Project.setText(_translate("Locomotif", "Open Project...", None))
        self.actionStatus_Box.setText(_translate("Locomotif", "Status Box", None))

from PyQt4 import Qwt5
