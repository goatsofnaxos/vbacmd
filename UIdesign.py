# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\All\Desktop\pyscript\eclipse\VBAcmd\UIdesign.ui'
#
# Created: Sat Jul 08 12:14:01 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(604, 779)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_11.addWidget(self.label_8)
        self.aiRangeMaxSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.aiRangeMaxSpinBox.setDecimals(2)
        self.aiRangeMaxSpinBox.setMinimum(-20.0)
        self.aiRangeMaxSpinBox.setMaximum(20.0)
        self.aiRangeMaxSpinBox.setSingleStep(0.01)
        self.aiRangeMaxSpinBox.setObjectName(_fromUtf8("aiRangeMaxSpinBox"))
        self.verticalLayout_11.addWidget(self.aiRangeMaxSpinBox)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_11.addWidget(self.label_9)
        self.aiRangeMinSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.aiRangeMinSpinBox.setDecimals(2)
        self.aiRangeMinSpinBox.setMinimum(-20.0)
        self.aiRangeMinSpinBox.setMaximum(20.0)
        self.aiRangeMinSpinBox.setSingleStep(0.01)
        self.aiRangeMinSpinBox.setObjectName(_fromUtf8("aiRangeMinSpinBox"))
        self.verticalLayout_11.addWidget(self.aiRangeMinSpinBox)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.chartTitle_AnalogInput = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chartTitle_AnalogInput.setFont(font)
        self.chartTitle_AnalogInput.setAlignment(QtCore.Qt.AlignCenter)
        self.chartTitle_AnalogInput.setObjectName(_fromUtf8("chartTitle_AnalogInput"))
        self.horizontalLayout_9.addWidget(self.chartTitle_AnalogInput)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.analogInPlot = Qwt5.QwtPlot(self.centralwidget)
        self.analogInPlot.setMinimumSize(QtCore.QSize(300, 150))
        self.analogInPlot.setMaximumSize(QtCore.QSize(16777215, 200))
        self.analogInPlot.setObjectName(_fromUtf8("analogInPlot"))
        self.verticalLayout_12.addWidget(self.analogInPlot)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.laserThresholdDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.laserThresholdDoubleSpinBox.setDecimals(1)
        self.laserThresholdDoubleSpinBox.setMinimum(0.0)
        self.laserThresholdDoubleSpinBox.setMaximum(10000.0)
        self.laserThresholdDoubleSpinBox.setSingleStep(0.5)
        self.laserThresholdDoubleSpinBox.setObjectName(_fromUtf8("laserThresholdDoubleSpinBox"))
        self.verticalLayout.addWidget(self.laserThresholdDoubleSpinBox)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.laserSDThresholdDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.laserSDThresholdDoubleSpinBox.setDecimals(1)
        self.laserSDThresholdDoubleSpinBox.setMinimum(0.0)
        self.laserSDThresholdDoubleSpinBox.setMaximum(10000.0)
        self.laserSDThresholdDoubleSpinBox.setSingleStep(0.1)
        self.laserSDThresholdDoubleSpinBox.setObjectName(_fromUtf8("laserSDThresholdDoubleSpinBox"))
        self.verticalLayout.addWidget(self.laserSDThresholdDoubleSpinBox)
        self.laserSDtext_label = QtGui.QLabel(self.centralwidget)
        self.laserSDtext_label.setAlignment(QtCore.Qt.AlignCenter)
        self.laserSDtext_label.setObjectName(_fromUtf8("laserSDtext_label"))
        self.verticalLayout.addWidget(self.laserSDtext_label)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.laserWaitTimeDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.laserWaitTimeDoubleSpinBox.setDecimals(1)
        self.laserWaitTimeDoubleSpinBox.setMinimum(0.0)
        self.laserWaitTimeDoubleSpinBox.setMaximum(10000.0)
        self.laserWaitTimeDoubleSpinBox.setSingleStep(1.0)
        self.laserWaitTimeDoubleSpinBox.setObjectName(_fromUtf8("laserWaitTimeDoubleSpinBox"))
        self.verticalLayout.addWidget(self.laserWaitTimeDoubleSpinBox)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.servoWaitTimeDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.servoWaitTimeDoubleSpinBox.setDecimals(1)
        self.servoWaitTimeDoubleSpinBox.setMinimum(0.0)
        self.servoWaitTimeDoubleSpinBox.setMaximum(10000.0)
        self.servoWaitTimeDoubleSpinBox.setSingleStep(1.0)
        self.servoWaitTimeDoubleSpinBox.setObjectName(_fromUtf8("servoWaitTimeDoubleSpinBox"))
        self.verticalLayout.addWidget(self.servoWaitTimeDoubleSpinBox)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chartTitle_laserPosition = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chartTitle_laserPosition.setFont(font)
        self.chartTitle_laserPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.chartTitle_laserPosition.setObjectName(_fromUtf8("chartTitle_laserPosition"))
        self.horizontalLayout_2.addWidget(self.chartTitle_laserPosition)
        self.chartTitle_servoPosition = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chartTitle_servoPosition.setFont(font)
        self.chartTitle_servoPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.chartTitle_servoPosition.setObjectName(_fromUtf8("chartTitle_servoPosition"))
        self.horizontalLayout_2.addWidget(self.chartTitle_servoPosition)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.positionPlot = Qwt5.QwtPlot(self.centralwidget)
        self.positionPlot.setMinimumSize(QtCore.QSize(300, 150))
        self.positionPlot.setMaximumSize(QtCore.QSize(16777215, 200))
        self.positionPlot.setObjectName(_fromUtf8("positionPlot"))
        self.verticalLayout_7.addWidget(self.positionPlot)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.forceThresholdDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.forceThresholdDoubleSpinBox.setDecimals(1)
        self.forceThresholdDoubleSpinBox.setMinimum(0.0)
        self.forceThresholdDoubleSpinBox.setMaximum(10000.0)
        self.forceThresholdDoubleSpinBox.setSingleStep(1.0)
        self.forceThresholdDoubleSpinBox.setObjectName(_fromUtf8("forceThresholdDoubleSpinBox"))
        self.verticalLayout_2.addWidget(self.forceThresholdDoubleSpinBox)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.forceTimeBeforeSlackDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.forceTimeBeforeSlackDoubleSpinBox.setDecimals(1)
        self.forceTimeBeforeSlackDoubleSpinBox.setMinimum(0.0)
        self.forceTimeBeforeSlackDoubleSpinBox.setMaximum(10000.0)
        self.forceTimeBeforeSlackDoubleSpinBox.setSingleStep(1.0)
        self.forceTimeBeforeSlackDoubleSpinBox.setObjectName(_fromUtf8("forceTimeBeforeSlackDoubleSpinBox"))
        self.verticalLayout_2.addWidget(self.forceTimeBeforeSlackDoubleSpinBox)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chartTitle_force = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chartTitle_force.setFont(font)
        self.chartTitle_force.setAlignment(QtCore.Qt.AlignCenter)
        self.chartTitle_force.setObjectName(_fromUtf8("chartTitle_force"))
        self.verticalLayout_3.addWidget(self.chartTitle_force)
        self.forcePlot = Qwt5.QwtPlot(self.centralwidget)
        self.forcePlot.setMinimumSize(QtCore.QSize(300, 150))
        self.forcePlot.setMaximumSize(QtCore.QSize(16777215, 200))
        self.forcePlot.setObjectName(_fromUtf8("forcePlot"))
        self.verticalLayout_3.addWidget(self.forcePlot)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_13.addWidget(self.line_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.controlModeGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.controlModeGroupBox.setObjectName(_fromUtf8("controlModeGroupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.controlModeGroupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.manualRadioButton = QtGui.QRadioButton(self.controlModeGroupBox)
        self.manualRadioButton.setChecked(False)
        self.manualRadioButton.setAutoExclusive(True)
        self.manualRadioButton.setObjectName(_fromUtf8("manualRadioButton"))
        self.verticalLayout_6.addWidget(self.manualRadioButton)
        self.automaticRadioButton = QtGui.QRadioButton(self.controlModeGroupBox)
        self.automaticRadioButton.setAutoExclusive(True)
        self.automaticRadioButton.setObjectName(_fromUtf8("automaticRadioButton"))
        self.verticalLayout_6.addWidget(self.automaticRadioButton)
        self.horizontalLayout_7.addWidget(self.controlModeGroupBox)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_7.addWidget(self.line)
        self.servoStateGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.servoStateGroupBox.setObjectName(_fromUtf8("servoStateGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.servoStateGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.slackPositionRadioButton = QtGui.QRadioButton(self.servoStateGroupBox)
        self.slackPositionRadioButton.setChecked(False)
        self.slackPositionRadioButton.setAutoExclusive(True)
        self.slackPositionRadioButton.setObjectName(_fromUtf8("slackPositionRadioButton"))
        self.verticalLayout_5.addWidget(self.slackPositionRadioButton)
        self.pullPositionRadioButton = QtGui.QRadioButton(self.servoStateGroupBox)
        self.pullPositionRadioButton.setAutoExclusive(True)
        self.pullPositionRadioButton.setObjectName(_fromUtf8("pullPositionRadioButton"))
        self.verticalLayout_5.addWidget(self.pullPositionRadioButton)
        self.horizontalLayout_7.addWidget(self.servoStateGroupBox)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_9.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.slackPositionDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.slackPositionDoubleSpinBox.setDecimals(1)
        self.slackPositionDoubleSpinBox.setMinimum(0.0)
        self.slackPositionDoubleSpinBox.setMaximum(99.0)
        self.slackPositionDoubleSpinBox.setSingleStep(0.1)
        self.slackPositionDoubleSpinBox.setProperty("value", 0.0)
        self.slackPositionDoubleSpinBox.setObjectName(_fromUtf8("slackPositionDoubleSpinBox"))
        self.verticalLayout_8.addWidget(self.slackPositionDoubleSpinBox)
        self.pullPositionDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pullPositionDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.pullPositionDoubleSpinBox.setSizePolicy(sizePolicy)
        self.pullPositionDoubleSpinBox.setDecimals(1)
        self.pullPositionDoubleSpinBox.setMinimum(0.0)
        self.pullPositionDoubleSpinBox.setMaximum(99.0)
        self.pullPositionDoubleSpinBox.setSingleStep(0.1)
        self.pullPositionDoubleSpinBox.setProperty("value", 0.0)
        self.pullPositionDoubleSpinBox.setObjectName(_fromUtf8("pullPositionDoubleSpinBox"))
        self.verticalLayout_8.addWidget(self.pullPositionDoubleSpinBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_7.addWidget(self.line_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem7 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.outTrigTextLabel2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outTrigTextLabel2.setFont(font)
        self.outTrigTextLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.outTrigTextLabel2.setObjectName(_fromUtf8("outTrigTextLabel2"))
        self.horizontalLayout_6.addWidget(self.outTrigTextLabel2)
        self.tubeStateTextLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tubeStateTextLabel.setFont(font)
        self.tubeStateTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tubeStateTextLabel.setObjectName(_fromUtf8("tubeStateTextLabel"))
        self.horizontalLayout_6.addWidget(self.tubeStateTextLabel)
        self.outTrigTextLabel1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outTrigTextLabel1.setFont(font)
        self.outTrigTextLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.outTrigTextLabel1.setObjectName(_fromUtf8("outTrigTextLabel1"))
        self.horizontalLayout_6.addWidget(self.outTrigTextLabel1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.startSig = QtGui.QLineEdit(self.centralwidget)
        self.startSig.setEnabled(False)
        self.startSig.setMinimumSize(QtCore.QSize(140, 0))
        self.startSig.setMaximumSize(QtCore.QSize(75, 16777215))
        self.startSig.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startSig.setObjectName(_fromUtf8("startSig"))
        self.horizontalLayout_5.addWidget(self.startSig)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "VBAcmd", None))
        self.label_8.setText(_translate("MainWindow", "RangeMax", None))
        self.label_9.setText(_translate("MainWindow", "RangeMin", None))
        self.chartTitle_AnalogInput.setText(_translate("MainWindow", "Analog input (V)", None))
        self.label.setText(_translate("MainWindow", "Laser θ", None))
        self.label_10.setText(_translate("MainWindow", "Laser SD θ", None))
        self.laserSDtext_label.setText(_translate("MainWindow", "Laser Text", None))
        self.label_2.setText(_translate("MainWindow", "Laser wait (s)", None))
        self.label_4.setText(_translate("MainWindow", "Servo wait (s)", None))
        self.chartTitle_laserPosition.setText(_translate("MainWindow", "Laser position (mm)", None))
        self.chartTitle_servoPosition.setText(_translate("MainWindow", "Servo position (mm)", None))
        self.label_3.setText(_translate("MainWindow", "Force θ", None))
        self.label_5.setText(_translate("MainWindow", "Force wait (s)", None))
        self.chartTitle_force.setText(_translate("MainWindow", "Force (g)", None))
        self.controlModeGroupBox.setTitle(_translate("MainWindow", "Control mode", None))
        self.manualRadioButton.setText(_translate("MainWindow", "Stick shift", None))
        self.automaticRadioButton.setText(_translate("MainWindow", "Automatic", None))
        self.servoStateGroupBox.setTitle(_translate("MainWindow", "Servo state", None))
        self.slackPositionRadioButton.setText(_translate("MainWindow", "Slackening", None))
        self.pullPositionRadioButton.setText(_translate("MainWindow", "Pulling", None))
        self.label_7.setText(_translate("MainWindow", "Slack position", None))
        self.label_6.setText(_translate("MainWindow", "Pull position", None))
        self.outTrigTextLabel2.setText(_translate("MainWindow", "_", None))
        self.tubeStateTextLabel.setText(_translate("MainWindow", "FSM state", None))
        self.outTrigTextLabel1.setText(_translate("MainWindow", "_", None))

from PyQt4 import Qwt5
