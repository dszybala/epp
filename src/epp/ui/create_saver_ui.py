# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eyeon\repos\epp\src\_ui\create_saver.ui'
#
# Created: Fri Mar 01 13:01:15 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlgCreateSaver(object):
    def setupUi(self, dlgCreateSaver):
        dlgCreateSaver.setObjectName("dlgCreateSaver")
        dlgCreateSaver.resize(425, 405)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/epp_128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgCreateSaver.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(dlgCreateSaver)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblHeader = QtGui.QLabel(dlgCreateSaver)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lblHeader.setFont(font)
        self.lblHeader.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lblHeader.setMargin(10)
        self.lblHeader.setObjectName("lblHeader")
        self.verticalLayout_2.addWidget(self.lblHeader)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(12, 9, 15, 24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout1 = QtGui.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self._lblShot = QtGui.QLabel(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblShot.sizePolicy().hasHeightForWidth())
        self._lblShot.setSizePolicy(sizePolicy)
        self._lblShot.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self._lblShot.setFont(font)
        self._lblShot.setObjectName("_lblShot")
        self.gridLayout1.addWidget(self._lblShot, 3, 0, 1, 1)
        self._lblProject = QtGui.QLabel(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblProject.sizePolicy().hasHeightForWidth())
        self._lblProject.setSizePolicy(sizePolicy)
        self._lblProject.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self._lblProject.setFont(font)
        self._lblProject.setObjectName("_lblProject")
        self.gridLayout1.addWidget(self._lblProject, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout1.addItem(spacerItem, 2, 0, 1, 1)
        self.cmbProject = QtGui.QComboBox(dlgCreateSaver)
        self.cmbProject.setObjectName("cmbProject")
        self.gridLayout1.addWidget(self.cmbProject, 1, 1, 1, 1)
        self.cmbShot = QtGui.QComboBox(dlgCreateSaver)
        self.cmbShot.setObjectName("cmbShot")
        self.gridLayout1.addWidget(self.cmbShot, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout1)
        self.line = QtGui.QFrame(dlgCreateSaver)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout1_2 = QtGui.QGridLayout()
        self.gridLayout1_2.setObjectName("gridLayout1_2")
        self._lblVersion = QtGui.QLabel(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblVersion.sizePolicy().hasHeightForWidth())
        self._lblVersion.setSizePolicy(sizePolicy)
        self._lblVersion.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self._lblVersion.setFont(font)
        self._lblVersion.setObjectName("_lblVersion")
        self.gridLayout1_2.addWidget(self._lblVersion, 3, 0, 1, 1)
        self._lblName = QtGui.QLabel(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblName.sizePolicy().hasHeightForWidth())
        self._lblName.setSizePolicy(sizePolicy)
        self._lblName.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self._lblName.setFont(font)
        self._lblName.setObjectName("_lblName")
        self.gridLayout1_2.addWidget(self._lblName, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout1_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spnVersion = QtGui.QSpinBox(dlgCreateSaver)
        self.spnVersion.setPrefix("")
        self.spnVersion.setMinimum(1)
        self.spnVersion.setMaximum(9999)
        self.spnVersion.setObjectName("spnVersion")
        self.horizontalLayout.addWidget(self.spnVersion)
        self.butMatch = QtGui.QPushButton(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butMatch.sizePolicy().hasHeightForWidth())
        self.butMatch.setSizePolicy(sizePolicy)
        self.butMatch.setObjectName("butMatch")
        self.horizontalLayout.addWidget(self.butMatch)
        self.gridLayout1_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.lblPreview = QtGui.QLabel(dlgCreateSaver)
        self.lblPreview.setText("")
        self.lblPreview.setObjectName("lblPreview")
        self.gridLayout1_2.addWidget(self.lblPreview, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lneName = QtGui.QLineEdit(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lneName.sizePolicy().hasHeightForWidth())
        self.lneName.setSizePolicy(sizePolicy)
        self.lneName.setObjectName("lneName")
        self.horizontalLayout_4.addWidget(self.lneName)
        self.butMatchName = QtGui.QPushButton(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butMatchName.sizePolicy().hasHeightForWidth())
        self.butMatchName.setSizePolicy(sizePolicy)
        self.butMatchName.setObjectName("butMatchName")
        self.horizontalLayout_4.addWidget(self.butMatchName)
        self.gridLayout1_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self._lblFormat = QtGui.QLabel(dlgCreateSaver)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblFormat.sizePolicy().hasHeightForWidth())
        self._lblFormat.setSizePolicy(sizePolicy)
        self._lblFormat.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self._lblFormat.setFont(font)
        self._lblFormat.setObjectName("_lblFormat")
        self.gridLayout1_2.addWidget(self._lblFormat, 4, 0, 1, 1)
        self.cmbFormat = QtGui.QComboBox(dlgCreateSaver)
        self.cmbFormat.setObjectName("cmbFormat")
        self.gridLayout1_2.addWidget(self.cmbFormat, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout1_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.lblStatus = QtGui.QLabel(dlgCreateSaver)
        self.lblStatus.setStyleSheet("")
        self.lblStatus.setOpenExternalLinks(True)
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout.addWidget(self.lblStatus)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.butCreate = QtGui.QPushButton(dlgCreateSaver)
        self.butCreate.setObjectName("butCreate")
        self.horizontalLayout_2.addWidget(self.butCreate)
        self.butCancel = QtGui.QPushButton(dlgCreateSaver)
        self.butCancel.setObjectName("butCancel")
        self.horizontalLayout_2.addWidget(self.butCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dlgCreateSaver)
        QtCore.QObject.connect(self.butCreate, QtCore.SIGNAL("clicked()"), dlgCreateSaver.accept)
        QtCore.QObject.connect(self.butCancel, QtCore.SIGNAL("clicked()"), dlgCreateSaver.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgCreateSaver)
        dlgCreateSaver.setTabOrder(self.butCreate, self.butCancel)

    def retranslateUi(self, dlgCreateSaver):
        dlgCreateSaver.setWindowTitle(QtGui.QApplication.translate("dlgCreateSaver", "Create Saver", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHeader.setText(QtGui.QApplication.translate("dlgCreateSaver", "Create Saver", None, QtGui.QApplication.UnicodeUTF8))
        self._lblShot.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Project name and also the projects root directory name", None, QtGui.QApplication.UnicodeUTF8))
        self._lblShot.setWhatsThis(QtGui.QApplication.translate("dlgCreateSaver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The </span><span style=\" font-size:8pt; font-weight:600;\">Name</span><span style=\" font-size:8pt;\"> for the project needs to be set based on studio conventions. This name is also used for the root folder of the project. Make sure it is file system safe and does not contain invalid characters. The default widget limits input to valid characters. Already existing project names can not be used to prevent data loss through overwriting.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._lblShot.setText(QtGui.QApplication.translate("dlgCreateSaver", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self._lblProject.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Format Template for production.", None, QtGui.QApplication.UnicodeUTF8))
        self._lblProject.setWhatsThis(QtGui.QApplication.translate("dlgCreateSaver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:600;\">Format Templates</span> are presets of Width, Height, Framerage (FPS) and Aspect Ratios for a Production. They are stored in your <span style=\" font-style:italic;\">epp_root\\templates\\formats.xml</span> file. As starting point formats can be imported during install of epp from eyeon Fusion.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._lblProject.setText(QtGui.QApplication.translate("dlgCreateSaver", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self._lblVersion.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Project name and also the projects root directory name", None, QtGui.QApplication.UnicodeUTF8))
        self._lblVersion.setWhatsThis(QtGui.QApplication.translate("dlgCreateSaver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The </span><span style=\" font-size:8pt; font-weight:600;\">Name</span><span style=\" font-size:8pt;\"> for the project needs to be set based on studio conventions. This name is also used for the root folder of the project. Make sure it is file system safe and does not contain invalid characters. The default widget limits input to valid characters. Already existing project names can not be used to prevent data loss through overwriting.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._lblVersion.setText(QtGui.QApplication.translate("dlgCreateSaver", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self._lblName.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Format Template for production.", None, QtGui.QApplication.UnicodeUTF8))
        self._lblName.setWhatsThis(QtGui.QApplication.translate("dlgCreateSaver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:600;\">Format Templates</span> are presets of Width, Height, Framerage (FPS) and Aspect Ratios for a Production. They are stored in your <span style=\" font-style:italic;\">epp_root\\templates\\formats.xml</span> file. As starting point formats can be imported during install of epp from eyeon Fusion.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._lblName.setText(QtGui.QApplication.translate("dlgCreateSaver", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.butMatch.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Next available version", None, QtGui.QApplication.UnicodeUTF8))
        self.butMatch.setText(QtGui.QApplication.translate("dlgCreateSaver", "Match", None, QtGui.QApplication.UnicodeUTF8))
        self.butMatchName.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Next available version", None, QtGui.QApplication.UnicodeUTF8))
        self.butMatchName.setText(QtGui.QApplication.translate("dlgCreateSaver", "Match", None, QtGui.QApplication.UnicodeUTF8))
        self._lblFormat.setToolTip(QtGui.QApplication.translate("dlgCreateSaver", "Project name and also the projects root directory name", None, QtGui.QApplication.UnicodeUTF8))
        self._lblFormat.setWhatsThis(QtGui.QApplication.translate("dlgCreateSaver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The </span><span style=\" font-size:8pt; font-weight:600;\">Name</span><span style=\" font-size:8pt;\"> for the project needs to be set based on studio conventions. This name is also used for the root folder of the project. Make sure it is file system safe and does not contain invalid characters. The default widget limits input to valid characters. Already existing project names can not be used to prevent data loss through overwriting.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._lblFormat.setText(QtGui.QApplication.translate("dlgCreateSaver", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setStatusTip(QtGui.QApplication.translate("dlgCreateSaver", "Warning Status", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("dlgCreateSaver", "WARINING", None, QtGui.QApplication.UnicodeUTF8))
        self.butCreate.setStatusTip(QtGui.QApplication.translate("dlgCreateSaver", "Create Project and Directories", None, QtGui.QApplication.UnicodeUTF8))
        self.butCreate.setText(QtGui.QApplication.translate("dlgCreateSaver", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.butCancel.setStatusTip(QtGui.QApplication.translate("dlgCreateSaver", "Cancel the operation", None, QtGui.QApplication.UnicodeUTF8))
        self.butCancel.setText(QtGui.QApplication.translate("dlgCreateSaver", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import epp_rc
