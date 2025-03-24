# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1800, 960)
        self.folder_edit = QtWidgets.QLineEdit(Form)
        self.folder_edit.setGeometry(QtCore.QRect(11, 131, 461, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.folder_edit.setFont(font)
        self.folder_edit.setText("")
        self.folder_edit.setReadOnly(False)
        self.folder_edit.setObjectName("folder_edit")
        self.FileName = QtWidgets.QLineEdit(Form)
        self.FileName.setGeometry(QtCore.QRect(150, 160, 481, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FileName.setFont(font)
        self.FileName.setObjectName("FileName")
        self.labelFilename = QtWidgets.QLabel(Form)
        self.labelFilename.setGeometry(QtCore.QRect(11, 163, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFilename.setFont(font)
        self.labelFilename.setObjectName("labelFilename")
        self.labelDirectory = QtWidgets.QLabel(Form)
        self.labelDirectory.setGeometry(QtCore.QRect(11, 110, 80, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDirectory.setFont(font)
        self.labelDirectory.setObjectName("labelDirectory")
        self.folderButton = QtWidgets.QPushButton(Form)
        self.folderButton.setGeometry(QtCore.QRect(480, 130, 151, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.folderButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.folderButton.setFont(font)
        self.folderButton.setObjectName("folderButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 103))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelExpTime = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelExpTime.setFont(font)
        self.labelExpTime.setObjectName("labelExpTime")
        self.gridLayout_2.addWidget(self.labelExpTime, 3, 3, 1, 1)
        self.Current_Mag = QtWidgets.QLabel(self.layoutWidget)
        self.Current_Mag.setText("")
        self.Current_Mag.setObjectName("Current_Mag")
        self.gridLayout_2.addWidget(self.Current_Mag, 3, 0, 1, 1)
        self.ROrateLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ROrateLabel.setFont(font)
        self.ROrateLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ROrateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ROrateLabel.setObjectName("ROrateLabel")
        self.gridLayout_2.addWidget(self.ROrateLabel, 0, 0, 1, 1)
        self.ROrateComboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ROrateComboBox.setFont(font)
        self.ROrateComboBox.setObjectName("ROrateComboBox")
        self.gridLayout_2.addWidget(self.ROrateComboBox, 0, 1, 1, 1)
        self.pModeComboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pModeComboBox.setFont(font)
        self.pModeComboBox.setObjectName("pModeComboBox")
        self.gridLayout_2.addWidget(self.pModeComboBox, 1, 1, 1, 1)
        self.PModeLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PModeLabel.setFont(font)
        self.PModeLabel.setTextFormat(QtCore.Qt.PlainText)
        self.PModeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PModeLabel.setObjectName("PModeLabel")
        self.gridLayout_2.addWidget(self.PModeLabel, 1, 0, 1, 1)
        self.gain_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gain_label.setFont(font)
        self.gain_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gain_label.setObjectName("gain_label")
        self.gridLayout_2.addWidget(self.gain_label, 0, 3, 1, 1)
        self.gain_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gain_spinBox.setFont(font)
        self.gain_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gain_spinBox.setMinimum(1)
        self.gain_spinBox.setMaximum(2)
        self.gain_spinBox.setObjectName("gain_spinBox")
        self.gridLayout_2.addWidget(self.gain_spinBox, 0, 4, 1, 1)
        self.labelBinning = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelBinning.setFont(font)
        self.labelBinning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBinning.setObjectName("labelBinning")
        self.gridLayout_2.addWidget(self.labelBinning, 1, 3, 1, 1)
        self.binningComboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.binningComboBox.setFont(font)
        self.binningComboBox.setObjectName("binningComboBox")
        self.gridLayout_2.addWidget(self.binningComboBox, 1, 4, 1, 1)
        self.ExpTime = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ExpTime.setFont(font)
        self.ExpTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ExpTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ExpTime.setMaximum(200000.0)
        self.ExpTime.setProperty("value", 99.0)
        self.ExpTime.setObjectName("ExpTime")
        self.gridLayout_2.addWidget(self.ExpTime, 3, 4, 1, 1)
        self.save_Button = QtWidgets.QPushButton(Form)
        self.save_Button.setGeometry(QtCore.QRect(640, 130, 81, 56))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_Button.setFont(font)
        self.save_Button.setObjectName("save_Button")
        self.SetCam_button = QtWidgets.QPushButton(Form)
        self.SetCam_button.setGeometry(QtCore.QRect(800, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SetCam_button.setFont(font)
        self.SetCam_button.setObjectName("SetCam_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 190, 305, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Set_Ref_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Set_Ref_button.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Set_Ref_button.setFont(font)
        self.Set_Ref_button.setObjectName("Set_Ref_button")
        self.horizontalLayout_3.addWidget(self.Set_Ref_button)
        self.remove_ref_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.remove_ref_button.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remove_ref_button.setFont(font)
        self.remove_ref_button.setObjectName("remove_ref_button")
        self.horizontalLayout_3.addWidget(self.remove_ref_button)
        self.Take_snap_button = QtWidgets.QPushButton(Form)
        self.Take_snap_button.setEnabled(True)
        self.Take_snap_button.setGeometry(QtCore.QRect(140, 190, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Take_snap_button.setFont(font)
        self.Take_snap_button.setObjectName("Take_snap_button")
        self.StartButton = QtWidgets.QPushButton(Form)
        self.StartButton.setGeometry(QtCore.QRect(12, 187, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartButton.setFont(font)
        self.StartButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.StartButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QPushButton(Form)
        self.StopButton.setGeometry(QtCore.QRect(270, 190, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.StopButton.setObjectName("StopButton")
        self.refAutoLims_checkBox = QtWidgets.QCheckBox(Form)
        self.refAutoLims_checkBox.setGeometry(QtCore.QRect(20, 266, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refAutoLims_checkBox.setFont(font)
        self.refAutoLims_checkBox.setChecked(True)
        self.refAutoLims_checkBox.setObjectName("refAutoLims_checkBox")
        self.diffAutoLims_checkBox = QtWidgets.QCheckBox(Form)
        self.diffAutoLims_checkBox.setGeometry(QtCore.QRect(930, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diffAutoLims_checkBox.setFont(font)
        self.diffAutoLims_checkBox.setChecked(True)
        self.diffAutoLims_checkBox.setObjectName("diffAutoLims_checkBox")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1040, 270, 301, 32))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.diffMinInt_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diffMinInt_spinBox.setFont(font)
        self.diffMinInt_spinBox.setMinimum(-65535)
        self.diffMinInt_spinBox.setMaximum(65535)
        self.diffMinInt_spinBox.setProperty("value", -500)
        self.diffMinInt_spinBox.setObjectName("diffMinInt_spinBox")
        self.horizontalLayout_2.addWidget(self.diffMinInt_spinBox)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.diffMaxInt_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diffMaxInt_spinBox.setFont(font)
        self.diffMaxInt_spinBox.setMinimum(-65535)
        self.diffMaxInt_spinBox.setMaximum(65535)
        self.diffMaxInt_spinBox.setProperty("value", 500)
        self.diffMaxInt_spinBox.setObjectName("diffMaxInt_spinBox")
        self.horizontalLayout_2.addWidget(self.diffMaxInt_spinBox)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 270, 301, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.refMinInt_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refMinInt_spinBox.setFont(font)
        self.refMinInt_spinBox.setMaximum(65535)
        self.refMinInt_spinBox.setObjectName("refMinInt_spinBox")
        self.horizontalLayout.addWidget(self.refMinInt_spinBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.refMaxInt_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refMaxInt_spinBox.setFont(font)
        self.refMaxInt_spinBox.setMaximum(65535)
        self.refMaxInt_spinBox.setProperty("value", 1000)
        self.refMaxInt_spinBox.setObjectName("refMaxInt_spinBox")
        self.horizontalLayout.addWidget(self.refMaxInt_spinBox)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(730, 150, 236, 135))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.saveRef_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveRef_checkBox.setFont(font)
        self.saveRef_checkBox.setChecked(True)
        self.saveRef_checkBox.setObjectName("saveRef_checkBox")
        self.verticalLayout.addWidget(self.saveRef_checkBox)
        self.saveDiff_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveDiff_checkBox.setFont(font)
        self.saveDiff_checkBox.setChecked(True)
        self.saveDiff_checkBox.setObjectName("saveDiff_checkBox")
        self.verticalLayout.addWidget(self.saveDiff_checkBox)
        self.save_datFiles_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_datFiles_checkBox.setFont(font)
        self.save_datFiles_checkBox.setChecked(True)
        self.save_datFiles_checkBox.setObjectName("save_datFiles_checkBox")
        self.verticalLayout.addWidget(self.save_datFiles_checkBox)
        self.save_h5Files_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.save_h5Files_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_h5Files_checkBox.setFont(font)
        self.save_h5Files_checkBox.setChecked(True)
        self.save_h5Files_checkBox.setObjectName("save_h5Files_checkBox")
        self.verticalLayout.addWidget(self.save_h5Files_checkBox)
        self.Image_view = ImageView(Form)
        self.Image_view.setGeometry(QtCore.QRect(10, 310, 951, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Image_view.sizePolicy().hasHeightForWidth())
        self.Image_view.setSizePolicy(sizePolicy)
        self.Image_view.setObjectName("Image_view")
        self.Diff_view = ImageView(Form)
        self.Diff_view.setGeometry(QtCore.QRect(970, 310, 850, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Diff_view.sizePolicy().hasHeightForWidth())
        self.Diff_view.setSizePolicy(sizePolicy)
        self.Diff_view.setObjectName("Diff_view")
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(960, 10, 801, 251))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Log_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Log_label.setFont(font)
        self.Log_label.setObjectName("Log_label")
        self.gridLayout.addWidget(self.Log_label, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.status_memo_PlainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget3)
        self.status_memo_PlainTextEdit.setEnabled(True)
        self.status_memo_PlainTextEdit.setReadOnly(True)
        self.status_memo_PlainTextEdit.setObjectName("status_memo_PlainTextEdit")
        self.gridLayout.addWidget(self.status_memo_PlainTextEdit, 1, 2, 1, 1)
        self.cam_params_plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget3)
        self.cam_params_plainTextEdit.setReadOnly(True)
        self.cam_params_plainTextEdit.setObjectName("cam_params_plainTextEdit")
        self.gridLayout.addWidget(self.cam_params_plainTextEdit, 1, 0, 1, 1)
        self.comments_memo_PlainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget3)
        self.comments_memo_PlainTextEdit.setObjectName("comments_memo_PlainTextEdit")
        self.gridLayout.addWidget(self.comments_memo_PlainTextEdit, 1, 1, 1, 1)
        self.Comments_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Comments_label.setFont(font)
        self.Comments_label.setObjectName("Comments_label")
        self.gridLayout.addWidget(self.Comments_label, 0, 1, 1, 1)
        self.SaveSettings_button = QtWidgets.QPushButton(Form)
        self.SaveSettings_button.setEnabled(True)
        self.SaveSettings_button.setGeometry(QtCore.QRect(800, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SaveSettings_button.setFont(font)
        self.SaveSettings_button.setObjectName("SaveSettings_button")
        self.LoadSettings_button = QtWidgets.QPushButton(Form)
        self.LoadSettings_button.setEnabled(True)
        self.LoadSettings_button.setGeometry(QtCore.QRect(800, 100, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoadSettings_button.setFont(font)
        self.LoadSettings_button.setObjectName("LoadSettings_button")
        self.CameraReady_indButton = QtWidgets.QPushButton(Form)
        self.CameraReady_indButton.setEnabled(False)
        self.CameraReady_indButton.setGeometry(QtCore.QRect(460, 270, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CameraReady_indButton.setFont(font)
        self.CameraReady_indButton.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.CameraReady_indButton.setObjectName("CameraReady_indButton")

        self.retranslateUi(Form)
        self.ROrateComboBox.setCurrentIndex(-1)
        self.pModeComboBox.setCurrentIndex(-1)
        self.binningComboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Camera live imaging"))
        self.FileName.setText(_translate("Form", "Run_"))
        self.labelFilename.setText(_translate("Form", "File name (no .ext)"))
        self.labelDirectory.setText(_translate("Form", "Folder path"))
        self.folderButton.setText(_translate("Form", "Choose Folder Path"))
        self.labelExpTime.setText(_translate("Form", "Exp. time (ms)"))
        self.ROrateLabel.setText(_translate("Form", "Camera ROrate"))
        self.PModeLabel.setText(_translate("Form", "Camera PMode"))
        self.gain_label.setText(_translate("Form", "Camera Gain"))
        self.labelBinning.setText(_translate("Form", "Binning"))
        self.save_Button.setText(_translate("Form", "Save"))
        self.SetCam_button.setText(_translate("Form", "Set Cam"))
        self.Set_Ref_button.setText(_translate("Form", "Set Reference"))
        self.remove_ref_button.setText(_translate("Form", "Delete Reference"))
        self.Take_snap_button.setText(_translate("Form", "Snapshot"))
        self.StartButton.setText(_translate("Form", "Start live"))
        self.StopButton.setText(_translate("Form", "Stop"))
        self.refAutoLims_checkBox.setText(_translate("Form", "Auto lims"))
        self.diffAutoLims_checkBox.setText(_translate("Form", "Auto lims"))
        self.label_3.setText(_translate("Form", "Min"))
        self.label_4.setText(_translate("Form", "Max"))
        self.label.setText(_translate("Form", "Min"))
        self.label_2.setText(_translate("Form", "Max"))
        self.saveRef_checkBox.setText(_translate("Form", "Save reference image?"))
        self.saveDiff_checkBox.setText(_translate("Form", "Save difference image?"))
        self.save_datFiles_checkBox.setText(_translate("Form", "Save .dat files?"))
        self.save_h5Files_checkBox.setText(_translate("Form", "Save .h5 files?"))
        self.Log_label.setText(_translate("Form", "Log"))
        self.label_6.setText(_translate("Form", "Camera settings"))
        self.comments_memo_PlainTextEdit.setPlainText(_translate("Form", "Sample:\n"
"Pump power:\n"
"Pump polarization:\n"
""))
        self.Comments_label.setText(_translate("Form", "Comments"))
        self.SaveSettings_button.setText(_translate("Form", "Save settings"))
        self.LoadSettings_button.setText(_translate("Form", "Load settings"))
        self.CameraReady_indButton.setText(_translate("Form", "Camera busy"))
from pyqtgraph import ImageView
