# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_Configuration.ui'
#
# Created: Sun Aug 16 20:44:50 2015
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

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName(_fromUtf8("Configuration"))
        Configuration.resize(651, 311)
        self.buttonBox = QtGui.QDialogButtonBox(Configuration)
        self.buttonBox.setGeometry(QtCore.QRect(290, 200, 341, 32))
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_6 = QtGui.QLabel(Configuration)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(Configuration)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.editCfgMapPath = QtGui.QLineEdit(Configuration)
        self.editCfgMapPath.setGeometry(QtCore.QRect(140, 50, 411, 20))
        self.editCfgMapPath.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMapPath.setObjectName(_fromUtf8("editCfgMapPath"))
        self.editCfgDataPath = QtGui.QLineEdit(Configuration)
        self.editCfgDataPath.setGeometry(QtCore.QRect(140, 20, 411, 20))
        self.editCfgDataPath.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgDataPath.setObjectName(_fromUtf8("editCfgDataPath"))
        self.cmdSelCfgDataPath = QtGui.QPushButton(Configuration)
        self.cmdSelCfgDataPath.setGeometry(QtCore.QRect(560, 20, 75, 23))
        self.cmdSelCfgDataPath.setObjectName(_fromUtf8("cmdSelCfgDataPath"))
        self.cmdSelCfgMapPath = QtGui.QPushButton(Configuration)
        self.cmdSelCfgMapPath.setGeometry(QtCore.QRect(560, 50, 75, 23))
        self.cmdSelCfgMapPath.setObjectName(_fromUtf8("cmdSelCfgMapPath"))
        self.groupBox = QtGui.QGroupBox(Configuration)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 151, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 41, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.editCfgMapWidth = QtGui.QLineEdit(self.groupBox)
        self.editCfgMapWidth.setGeometry(QtCore.QRect(70, 20, 51, 20))
        self.editCfgMapWidth.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMapWidth.setObjectName(_fromUtf8("editCfgMapWidth"))
        self.editCfgMapHeight = QtGui.QLineEdit(self.groupBox)
        self.editCfgMapHeight.setGeometry(QtCore.QRect(70, 50, 51, 20))
        self.editCfgMapHeight.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.editCfgMapHeight.setObjectName(_fromUtf8("editCfgMapHeight"))

        self.retranslateUi(Configuration)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Configuration.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Configuration.reject)
        QtCore.QObject.connect(self.cmdSelCfgDataPath, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Configuration.doSelectDataPath)
        QtCore.QObject.connect(self.cmdSelCfgMapPath, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Configuration.doSelectMapPath)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(_translate("Configuration", "Settings", None))
        self.label_6.setText(_translate("Configuration", "Path for Map Files", None))
        self.label_5.setText(_translate("Configuration", "Path for Data Files", None))
        self.cmdSelCfgDataPath.setText(_translate("Configuration", "Browse", None))
        self.cmdSelCfgMapPath.setText(_translate("Configuration", "Browse", None))
        self.groupBox.setTitle(_translate("Configuration", "Map Dimesions", None))
        self.label_7.setText(_translate("Configuration", "Width:", None))
        self.label_8.setText(_translate("Configuration", "Height", None))

