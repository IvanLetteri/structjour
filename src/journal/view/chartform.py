# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\chartform.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 804)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/ZSLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 26, 669, 748))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_19.addWidget(self.label)
        self.styleCb = QtWidgets.QComboBox(self.layoutWidget)
        self.styleCb.setObjectName("styleCb")
        self.horizontalLayout_19.addWidget(self.styleCb)
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_20.addWidget(self.label_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridhCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.gridhCb.setObjectName("gridhCb")
        self.verticalLayout_6.addWidget(self.gridhCb)
        self.gridvCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.gridvCb.setObjectName("gridvCb")
        self.verticalLayout_6.addWidget(self.gridvCb)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.line_5 = QtWidgets.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_7.addWidget(self.line_5)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_21.addWidget(self.label_2)
        self.markerColorUp = QtWidgets.QLineEdit(self.layoutWidget)
        self.markerColorUp.setObjectName("markerColorUp")
        self.horizontalLayout_21.addWidget(self.markerColorUp)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.line_12 = QtWidgets.QFrame(self.layoutWidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_7.addWidget(self.line_12)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(120, 0))
        self.label_14.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_22.addWidget(self.label_14)
        self.markerColorDown = QtWidgets.QLineEdit(self.layoutWidget)
        self.markerColorDown.setObjectName("markerColorDown")
        self.horizontalLayout_22.addWidget(self.markerColorDown)
        self.verticalLayout_7.addLayout(self.horizontalLayout_22)
        self.line_6 = QtWidgets.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_7.addWidget(self.line_6)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_23.addWidget(self.label_3)
        self.markerEdgeColor = QtWidgets.QLineEdit(self.layoutWidget)
        self.markerEdgeColor.setObjectName("markerEdgeColor")
        self.horizontalLayout_23.addWidget(self.markerEdgeColor)
        self.verticalLayout_7.addLayout(self.horizontalLayout_23)
        self.line_7 = QtWidgets.QFrame(self.layoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_7.addWidget(self.line_7)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_24.addWidget(self.label_4)
        self.markerAlpha = QtWidgets.QLineEdit(self.layoutWidget)
        self.markerAlpha.setObjectName("markerAlpha")
        self.horizontalLayout_24.addWidget(self.markerAlpha)
        self.verticalLayout_7.addLayout(self.horizontalLayout_24)
        self.line_13 = QtWidgets.QFrame(self.layoutWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_7.addWidget(self.line_13)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_25.addWidget(self.label_15)
        self.markerSize = QtWidgets.QSpinBox(self.layoutWidget)
        self.markerSize.setMinimum(3)
        self.markerSize.setMaximum(200)
        self.markerSize.setObjectName("markerSize")
        self.horizontalLayout_25.addWidget(self.markerSize)
        self.verticalLayout_7.addLayout(self.horizontalLayout_25)
        self.line_8 = QtWidgets.QFrame(self.layoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_7.addWidget(self.line_8)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(120, 0))
        self.label_6.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_26.addWidget(self.label_6)
        self.colorUp = QtWidgets.QLineEdit(self.layoutWidget)
        self.colorUp.setObjectName("colorUp")
        self.horizontalLayout_26.addWidget(self.colorUp)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.line_9 = QtWidgets.QFrame(self.layoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_7.addWidget(self.line_9)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(120, 0))
        self.label_7.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_27.addWidget(self.label_7)
        self.colorDown = QtWidgets.QLineEdit(self.layoutWidget)
        self.colorDown.setObjectName("colorDown")
        self.horizontalLayout_27.addWidget(self.colorDown)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.line_10 = QtWidgets.QFrame(self.layoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_7.addWidget(self.line_10)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_28.addWidget(self.label_9)
        self.interactive = QtWidgets.QCheckBox(self.layoutWidget)
        self.interactive.setText("")
        self.interactive.setObjectName("interactive")
        self.horizontalLayout_28.addWidget(self.interactive)
        self.verticalLayout_7.addLayout(self.horizontalLayout_28)
        spacerItem1 = QtWidgets.QSpacerItem(20, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_29.addLayout(self.verticalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem2)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_29.addWidget(self.line_3)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chart1MA1 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart1MA1.sizePolicy().hasHeightForWidth())
        self.chart1MA1.setSizePolicy(sizePolicy)
        self.chart1MA1.setMinimumSize(QtCore.QSize(85, 0))
        self.chart1MA1.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart1MA1.setObjectName("chart1MA1")
        self.horizontalLayout.addWidget(self.chart1MA1)
        self.chart1MA1Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart1MA1Spin.setMinimum(5)
        self.chart1MA1Spin.setMaximum(200)
        self.chart1MA1Spin.setProperty("value", 9)
        self.chart1MA1Spin.setObjectName("chart1MA1Spin")
        self.horizontalLayout.addWidget(self.chart1MA1Spin)
        self.chart1MA1Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart1MA1Color.setObjectName("chart1MA1Color")
        self.horizontalLayout.addWidget(self.chart1MA1Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chart1MA2 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart1MA2.sizePolicy().hasHeightForWidth())
        self.chart1MA2.setSizePolicy(sizePolicy)
        self.chart1MA2.setMinimumSize(QtCore.QSize(85, 0))
        self.chart1MA2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart1MA2.setObjectName("chart1MA2")
        self.horizontalLayout_2.addWidget(self.chart1MA2)
        self.chart1MA2Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart1MA2Spin.setMinimum(5)
        self.chart1MA2Spin.setMaximum(200)
        self.chart1MA2Spin.setProperty("value", 20)
        self.chart1MA2Spin.setObjectName("chart1MA2Spin")
        self.horizontalLayout_2.addWidget(self.chart1MA2Spin)
        self.chart1MA2Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart1MA2Color.setObjectName("chart1MA2Color")
        self.horizontalLayout_2.addWidget(self.chart1MA2Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chart1MA3 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart1MA3.sizePolicy().hasHeightForWidth())
        self.chart1MA3.setSizePolicy(sizePolicy)
        self.chart1MA3.setMinimumSize(QtCore.QSize(85, 0))
        self.chart1MA3.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart1MA3.setObjectName("chart1MA3")
        self.horizontalLayout_3.addWidget(self.chart1MA3)
        self.chart1MA3Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart1MA3Spin.setMinimum(5)
        self.chart1MA3Spin.setMaximum(200)
        self.chart1MA3Spin.setProperty("value", 50)
        self.chart1MA3Spin.setObjectName("chart1MA3Spin")
        self.horizontalLayout_3.addWidget(self.chart1MA3Spin)
        self.chart1MA3Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart1MA3Color.setObjectName("chart1MA3Color")
        self.horizontalLayout_3.addWidget(self.chart1MA3Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chart1MA4 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart1MA4.sizePolicy().hasHeightForWidth())
        self.chart1MA4.setSizePolicy(sizePolicy)
        self.chart1MA4.setMinimumSize(QtCore.QSize(85, 0))
        self.chart1MA4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart1MA4.setObjectName("chart1MA4")
        self.horizontalLayout_4.addWidget(self.chart1MA4)
        self.chart1MA4Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart1MA4Spin.setMinimum(5)
        self.chart1MA4Spin.setMaximum(200)
        self.chart1MA4Spin.setProperty("value", 200)
        self.chart1MA4Spin.setObjectName("chart1MA4Spin")
        self.horizontalLayout_4.addWidget(self.chart1MA4Spin)
        self.chart1MA4Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart1MA4Color.setObjectName("chart1MA4Color")
        self.horizontalLayout_4.addWidget(self.chart1MA4Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chart1VWAP = QtWidgets.QCheckBox(self.layoutWidget)
        self.chart1VWAP.setObjectName("chart1VWAP")
        self.horizontalLayout_5.addWidget(self.chart1VWAP)
        spacerItem5 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.chart1VWAPColor = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart1VWAPColor.setObjectName("chart1VWAPColor")
        self.horizontalLayout_5.addWidget(self.chart1VWAPColor)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_18.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_17.addWidget(self.label_11)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chart2MA1 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart2MA1.sizePolicy().hasHeightForWidth())
        self.chart2MA1.setSizePolicy(sizePolicy)
        self.chart2MA1.setMinimumSize(QtCore.QSize(85, 0))
        self.chart2MA1.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart2MA1.setObjectName("chart2MA1")
        self.horizontalLayout_6.addWidget(self.chart2MA1)
        self.chart2MA1Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart2MA1Spin.setMinimum(5)
        self.chart2MA1Spin.setMaximum(200)
        self.chart2MA1Spin.setProperty("value", 9)
        self.chart2MA1Spin.setObjectName("chart2MA1Spin")
        self.horizontalLayout_6.addWidget(self.chart2MA1Spin)
        self.chart2MA1Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart2MA1Color.setObjectName("chart2MA1Color")
        self.horizontalLayout_6.addWidget(self.chart2MA1Color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.chart2MA2 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart2MA2.sizePolicy().hasHeightForWidth())
        self.chart2MA2.setSizePolicy(sizePolicy)
        self.chart2MA2.setMinimumSize(QtCore.QSize(85, 0))
        self.chart2MA2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart2MA2.setObjectName("chart2MA2")
        self.horizontalLayout_7.addWidget(self.chart2MA2)
        self.chart2MA2Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart2MA2Spin.setMinimum(5)
        self.chart2MA2Spin.setMaximum(200)
        self.chart2MA2Spin.setProperty("value", 20)
        self.chart2MA2Spin.setObjectName("chart2MA2Spin")
        self.horizontalLayout_7.addWidget(self.chart2MA2Spin)
        self.chart2MA2Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart2MA2Color.setObjectName("chart2MA2Color")
        self.horizontalLayout_7.addWidget(self.chart2MA2Color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.chart2MA3 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart2MA3.sizePolicy().hasHeightForWidth())
        self.chart2MA3.setSizePolicy(sizePolicy)
        self.chart2MA3.setMinimumSize(QtCore.QSize(85, 0))
        self.chart2MA3.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart2MA3.setObjectName("chart2MA3")
        self.horizontalLayout_8.addWidget(self.chart2MA3)
        self.chart2MA3Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart2MA3Spin.setMinimum(5)
        self.chart2MA3Spin.setMaximum(200)
        self.chart2MA3Spin.setProperty("value", 50)
        self.chart2MA3Spin.setObjectName("chart2MA3Spin")
        self.horizontalLayout_8.addWidget(self.chart2MA3Spin)
        self.chart2MA3Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart2MA3Color.setObjectName("chart2MA3Color")
        self.horizontalLayout_8.addWidget(self.chart2MA3Color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.chart2MA4 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart2MA4.sizePolicy().hasHeightForWidth())
        self.chart2MA4.setSizePolicy(sizePolicy)
        self.chart2MA4.setMinimumSize(QtCore.QSize(85, 0))
        self.chart2MA4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart2MA4.setObjectName("chart2MA4")
        self.horizontalLayout_9.addWidget(self.chart2MA4)
        self.chart2MA4Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart2MA4Spin.setMinimum(5)
        self.chart2MA4Spin.setMaximum(200)
        self.chart2MA4Spin.setProperty("value", 200)
        self.chart2MA4Spin.setObjectName("chart2MA4Spin")
        self.horizontalLayout_9.addWidget(self.chart2MA4Spin)
        self.chart2MA4Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart2MA4Color.setObjectName("chart2MA4Color")
        self.horizontalLayout_9.addWidget(self.chart2MA4Color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.chart2VWAP = QtWidgets.QCheckBox(self.layoutWidget)
        self.chart2VWAP.setObjectName("chart2VWAP")
        self.horizontalLayout_10.addWidget(self.chart2VWAP)
        spacerItem7 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.chart2VWAPColor = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart2VWAPColor.setObjectName("chart2VWAPColor")
        self.horizontalLayout_10.addWidget(self.chart2VWAPColor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem8 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_17.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.chart3MA1 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart3MA1.sizePolicy().hasHeightForWidth())
        self.chart3MA1.setSizePolicy(sizePolicy)
        self.chart3MA1.setMinimumSize(QtCore.QSize(85, 0))
        self.chart3MA1.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart3MA1.setObjectName("chart3MA1")
        self.horizontalLayout_11.addWidget(self.chart3MA1)
        self.chart3MA1Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart3MA1Spin.setMinimum(5)
        self.chart3MA1Spin.setMaximum(200)
        self.chart3MA1Spin.setProperty("value", 9)
        self.chart3MA1Spin.setObjectName("chart3MA1Spin")
        self.horizontalLayout_11.addWidget(self.chart3MA1Spin)
        self.chart3MA1Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart3MA1Color.setObjectName("chart3MA1Color")
        self.horizontalLayout_11.addWidget(self.chart3MA1Color)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.chart3MA2 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart3MA2.sizePolicy().hasHeightForWidth())
        self.chart3MA2.setSizePolicy(sizePolicy)
        self.chart3MA2.setMinimumSize(QtCore.QSize(85, 0))
        self.chart3MA2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart3MA2.setObjectName("chart3MA2")
        self.horizontalLayout_12.addWidget(self.chart3MA2)
        self.chart3MA2Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart3MA2Spin.setMinimum(5)
        self.chart3MA2Spin.setMaximum(200)
        self.chart3MA2Spin.setProperty("value", 20)
        self.chart3MA2Spin.setObjectName("chart3MA2Spin")
        self.horizontalLayout_12.addWidget(self.chart3MA2Spin)
        self.chart3MA2Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart3MA2Color.setObjectName("chart3MA2Color")
        self.horizontalLayout_12.addWidget(self.chart3MA2Color)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.chart3MA3 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart3MA3.sizePolicy().hasHeightForWidth())
        self.chart3MA3.setSizePolicy(sizePolicy)
        self.chart3MA3.setMinimumSize(QtCore.QSize(85, 0))
        self.chart3MA3.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart3MA3.setObjectName("chart3MA3")
        self.horizontalLayout_13.addWidget(self.chart3MA3)
        self.chart3MA3Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart3MA3Spin.setMinimum(5)
        self.chart3MA3Spin.setMaximum(200)
        self.chart3MA3Spin.setProperty("value", 50)
        self.chart3MA3Spin.setObjectName("chart3MA3Spin")
        self.horizontalLayout_13.addWidget(self.chart3MA3Spin)
        self.chart3MA3Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart3MA3Color.setObjectName("chart3MA3Color")
        self.horizontalLayout_13.addWidget(self.chart3MA3Color)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.chart3MA4 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart3MA4.sizePolicy().hasHeightForWidth())
        self.chart3MA4.setSizePolicy(sizePolicy)
        self.chart3MA4.setMinimumSize(QtCore.QSize(85, 0))
        self.chart3MA4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.chart3MA4.setObjectName("chart3MA4")
        self.horizontalLayout_14.addWidget(self.chart3MA4)
        self.chart3MA4Spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.chart3MA4Spin.setMinimum(5)
        self.chart3MA4Spin.setMaximum(200)
        self.chart3MA4Spin.setProperty("value", 200)
        self.chart3MA4Spin.setObjectName("chart3MA4Spin")
        self.horizontalLayout_14.addWidget(self.chart3MA4Spin)
        self.chart3MA4Color = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart3MA4Color.setObjectName("chart3MA4Color")
        self.horizontalLayout_14.addWidget(self.chart3MA4Color)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.chart3VWAP = QtWidgets.QCheckBox(self.layoutWidget)
        self.chart3VWAP.setObjectName("chart3VWAP")
        self.horizontalLayout_15.addWidget(self.chart3VWAP)
        spacerItem9 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.chart3VWAPColor = QtWidgets.QLineEdit(self.layoutWidget)
        self.chart3VWAPColor.setObjectName("chart3VWAPColor")
        self.horizontalLayout_15.addWidget(self.chart3VWAPColor)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_16.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_29.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_29)
        self.line_11 = QtWidgets.QFrame(self.layoutWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_9.addWidget(self.line_11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Chart Configuration"))
        self.label_13.setText(_translate("Form", "Settings will affect updated charts. They will have no effect on saved charts."))
        self.label.setText(_translate("Form", "style"))
        self.label_8.setText(_translate("Form", "Grid"))
        self.gridhCb.setText(_translate("Form", "Horizontal"))
        self.gridvCb.setText(_translate("Form", "Vertical"))
        self.label_2.setText(_translate("Form", "Marker color up"))
        self.label_14.setText(_translate("Form", "Marker color down"))
        self.label_3.setText(_translate("Form", "Marker edge color"))
        self.label_4.setText(_translate("Form", "Marker alpha"))
        self.markerAlpha.setToolTip(_translate("Form", "<html><head/><body><p>Values between 0 and 1</p></body></html>"))
        self.label_15.setText(_translate("Form", "Marker size"))
        self.label_6.setText(_translate("Form", "Color up"))
        self.label_7.setText(_translate("Form", "Color down"))
        self.label_9.setText(_translate("Form", "Interactive"))
        self.label_5.setText(_translate("Form", "          Moving Averages"))
        self.label_10.setText(_translate("Form", "Chart 1"))
        self.chart1MA1.setText(_translate("Form", "9 EMA"))
        self.chart1MA2.setText(_translate("Form", "20 EMA"))
        self.chart1MA3.setText(_translate("Form", "50 SMA"))
        self.chart1MA4.setText(_translate("Form", "200 SMA"))
        self.chart1VWAP.setText(_translate("Form", "VWAP"))
        self.label_11.setText(_translate("Form", "Chart 2"))
        self.chart2MA1.setText(_translate("Form", "9 EMA"))
        self.chart2MA2.setText(_translate("Form", "20 EMA"))
        self.chart2MA3.setText(_translate("Form", "50 SMA"))
        self.chart2MA4.setText(_translate("Form", "200 SMA"))
        self.chart2VWAP.setText(_translate("Form", "VWAP"))
        self.label_12.setText(_translate("Form", "Chart 3"))
        self.chart3MA1.setText(_translate("Form", "9 EMA"))
        self.chart3MA2.setText(_translate("Form", "20 EMA"))
        self.chart3MA3.setText(_translate("Form", "50 SMA"))
        self.chart3MA4.setText(_translate("Form", "200 SMA"))
        self.chart3VWAP.setText(_translate("Form", "VWAP"))


