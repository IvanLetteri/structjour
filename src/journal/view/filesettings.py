# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\filesettings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 575)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/ZSLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(31, 44, 458, 473))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.journalBtn = QtWidgets.QPushButton(self.widget)
        self.journalBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.journalBtn.setObjectName("journalBtn")
        self.horizontalLayout.addWidget(self.journalBtn)
        self.journal = QtWidgets.QLineEdit(self.widget)
        self.journal.setMinimumSize(QtCore.QSize(300, 0))
        self.journal.setObjectName("journal")
        self.horizontalLayout.addWidget(self.journal)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.schemeBtn = QtWidgets.QPushButton(self.widget)
        self.schemeBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.schemeBtn.setObjectName("schemeBtn")
        self.horizontalLayout_2.addWidget(self.schemeBtn)
        self.scheme = QtWidgets.QLineEdit(self.widget)
        self.scheme.setMinimumSize(QtCore.QSize(300, 0))
        self.scheme.setObjectName("scheme")
        self.horizontalLayout_2.addWidget(self.scheme)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.schemeLbl = QtWidgets.QLabel(self.widget)
        self.schemeLbl.setObjectName("schemeLbl")
        self.verticalLayout_2.addWidget(self.schemeLbl)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dasInfileBtn = QtWidgets.QPushButton(self.widget)
        self.dasInfileBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dasInfileBtn.setObjectName("dasInfileBtn")
        self.horizontalLayout_3.addWidget(self.dasInfileBtn)
        self.dasInfile = QtWidgets.QLineEdit(self.widget)
        self.dasInfile.setMinimumSize(QtCore.QSize(300, 0))
        self.dasInfile.setObjectName("dasInfile")
        self.horizontalLayout_3.addWidget(self.dasInfile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.dasInfileLbl = QtWidgets.QLabel(self.widget)
        self.dasInfileLbl.setObjectName("dasInfileLbl")
        self.verticalLayout_2.addWidget(self.dasInfileLbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dasInfile2Btn = QtWidgets.QPushButton(self.widget)
        self.dasInfile2Btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dasInfile2Btn.setObjectName("dasInfile2Btn")
        self.horizontalLayout_4.addWidget(self.dasInfile2Btn)
        self.dasInfile2 = QtWidgets.QLineEdit(self.widget)
        self.dasInfile2.setMinimumSize(QtCore.QSize(300, 0))
        self.dasInfile2.setObjectName("dasInfile2")
        self.horizontalLayout_4.addWidget(self.dasInfile2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ibInfileBtn = QtWidgets.QPushButton(self.widget)
        self.ibInfileBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ibInfileBtn.setObjectName("ibInfileBtn")
        self.horizontalLayout_5.addWidget(self.ibInfileBtn)
        self.ibInfile = QtWidgets.QLineEdit(self.widget)
        self.ibInfile.setObjectName("ibInfile")
        self.horizontalLayout_5.addWidget(self.ibInfile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.outdirDefault = QtWidgets.QRadioButton(self.widget)
        self.outdirDefault.setObjectName("outdirDefault")
        self.verticalLayout.addWidget(self.outdirDefault)
        self.outdirStatic = QtWidgets.QRadioButton(self.widget)
        self.outdirStatic.setObjectName("outdirStatic")
        self.verticalLayout.addWidget(self.outdirStatic)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.outdir = QtWidgets.QLineEdit(self.widget)
        self.outdir.setMinimumSize(QtCore.QSize(300, 0))
        self.outdir.setObjectName("outdir")
        self.horizontalLayout_6.addWidget(self.outdir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.outdirLbl = QtWidgets.QLabel(self.widget)
        self.outdirLbl.setObjectName("outdirLbl")
        self.verticalLayout_2.addWidget(self.outdirLbl)
        self.explainDateLbl = QtWidgets.QLabel(self.widget)
        self.explainDateLbl.setObjectName("explainDateLbl")
        self.verticalLayout_2.addWidget(self.explainDateLbl)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.theDateBtn = QtWidgets.QPushButton(self.widget)
        self.theDateBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.theDateBtn.setObjectName("theDateBtn")
        self.horizontalLayout_7.addWidget(self.theDateBtn)
        self.theDate = QtWidgets.QDateEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theDate.sizePolicy().hasHeightForWidth())
        self.theDate.setSizePolicy(sizePolicy)
        self.theDate.setObjectName("theDate")
        self.horizontalLayout_7.addWidget(self.theDate)
        self.theDateCbox = QtWidgets.QCheckBox(self.widget)
        self.theDateCbox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.theDateCbox.setChecked(False)
        self.theDateCbox.setObjectName("theDateCbox")
        self.horizontalLayout_7.addWidget(self.theDateCbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.okBtn = QtWidgets.QPushButton(self.widget)
        self.okBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_8.addWidget(self.okBtn)
        spacerItem = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Settings"))
        self.journalBtn.setText(_translate("Dialog", "Journal Directory"))
        self.journal.setText(_translate("Dialog", "C:/traders/journal/"))
        self.label.setText(_translate("Dialog", "Directory Naming Scheme. Enter to commit"))
        self.schemeBtn.setText(_translate("Dialog", "Set Default"))
        self.scheme.setToolTip(_translate("Dialog", "<html><head/><body><p>Use the date variables as seen in the default naming scheme and see the result below. Please retain a month/day directory structure. Both directories should sort alpa-numerically. After editing press enter to update the naming scheme.</p></body></html>"))
        self.scheme.setText(_translate("Dialog", "_{Year}{month}_{MONTH}/_{month}{day}_{DAY}/"))
        self.schemeLbl.setText(_translate("Dialog", "_201901_January/_0114_Monday"))
        self.dasInfileBtn.setToolTip(_translate("Dialog", "<html><head/><body><p>Click this button to return the edit box to just the file name.</p></body></html>"))
        self.dasInfileBtn.setText(_translate("Dialog", "DAS Trades export"))
        self.dasInfile.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter only the filename. Press enter to see the resulting pathfile name. The color will indicate if the file exists or not.</span></p></body></html>"))
        self.dasInfile.setText(_translate("Dialog", "trades.csv"))
        self.dasInfileLbl.setText(_translate("Dialog", "C:/traders/journal/_2019_January_0114_Monday/trades.csv"))
        self.dasInfile2Btn.setText(_translate("Dialog", "DAS positions export"))
        self.dasInfile2.setText(_translate("Dialog", "positions.csv"))
        self.label_3.setText(_translate("Dialog", "C:/traders/journal/_2019_January_0114_Monday/positions.csv"))
        self.ibInfileBtn.setText(_translate("Dialog", "IB Activity Statement"))
        self.ibInfile.setToolTip(_translate("Dialog", "<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">Using the (simplified) globular {*}</span></h3><p><span style=\" font-size:10pt;\">Use the </span><span style=\" font-size:10pt; font-weight:600;\">{*}</span><span style=\" font-size:10pt;\"> to replace any characters.</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Activity{*}.html</span><span style=\" font-size:10pt;\"> will match </span><span style=\" font-size:10pt; font-weight:600;\">ActivityStatementU1234567.html</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Activity{*}0904{*}.html</span><span style=\" font-size:10pt;\"> would match </span><span style=\" font-size:10pt; font-weight:600;\">ActivityStatement.20190904.html</span></p><p><span style=\" font-size:10pt; font-weight:600;\">{*}.html</span><span style=\" font-size:10pt;\"> will show all files ending in html</span></p><p><span style=\" font-size:10pt;\">Press enter to see the results. Press again to return to your glob.</span></p></body></html>"))
        self.ibInfile.setText(_translate("Dialog", "Activity{*}.html"))
        self.label_4.setText(_translate("Dialog", "C:/traders/journal/_2019_January_0114_Monday/Activity_20190104.html"))
        self.outdirDefault.setText(_translate("Dialog", "Default"))
        self.outdirStatic.setText(_translate("Dialog", "Static"))
        self.outdir.setToolTip(_translate("Dialog", "<html><head/><body><p>Leave blank if you would like the outdir to be the same as the indir. Othersiwe this will be a subdirectory of the indir. Press enter to see the results below. If its red, it does not yet exist. It will be created when there is a file to save to it.</p></body></html>"))
        self.outdir.setText(_translate("Dialog", "out/"))
        self.outdirLbl.setText(_translate("Dialog", "C:/traders/journal/_2019_January_0114_Monday/out/"))
        self.explainDateLbl.setText(_translate("Dialog", "Date will be used to locate daily directories and set dates if missing (DAS trade)"))
        self.theDateBtn.setText(_translate("Dialog", "Set to Today"))
        self.theDate.setToolTip(_translate("Dialog", "<html><head/><body><p>Date will be used to locate the desired directories for input files. It wil also be used if the input files are missing dates. This is the case for the DAS trades export file, aka trades.csv.</p></body></html>"))
        self.theDateCbox.setText(_translate("Dialog", "Set today when program opens."))
        self.okBtn.setText(_translate("Dialog", "OK"))

