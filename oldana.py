# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oldana.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Old(object):
    def setupUi(self, Old):
        Old.setObjectName("Old")
        Old.resize(747, 360)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Old)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Old)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.icpeak = QtWidgets.QLineEdit(Old)
        self.icpeak.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.icpeak.setFont(font)
        self.icpeak.setObjectName("icpeak")
        self.gridLayout.addWidget(self.icpeak, 5, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Old)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Old)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 3)
        self.format = QtWidgets.QComboBox(Old)
        self.format.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.format.setFont(font)
        self.format.setObjectName("format")
        self.format.addItem("")
        self.format.addItem("")
        self.gridLayout.addWidget(self.format, 2, 1, 1, 2)
        self.analyse = QtWidgets.QPushButton(Old)
        self.analyse.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.analyse.setFont(font)
        self.analyse.setObjectName("analyse")
        self.gridLayout.addWidget(self.analyse, 2, 0, 1, 1)
        self.choose_1 = QtWidgets.QPushButton(Old)
        self.choose_1.setMaximumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.choose_1.setFont(font)
        self.choose_1.setObjectName("choose_1")
        self.gridLayout.addWidget(self.choose_1, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Old)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(Old)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 3)
        self.path_2 = QtWidgets.QLineEdit(Old)
        self.path_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.path_2.setFont(font)
        self.path_2.setObjectName("path_2")
        self.gridLayout.addWidget(self.path_2, 7, 0, 1, 2)
        self.choose_2 = QtWidgets.QPushButton(Old)
        self.choose_2.setMaximumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.choose_2.setFont(font)
        self.choose_2.setObjectName("choose_2")
        self.gridLayout.addWidget(self.choose_2, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(Old)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.path_1 = QtWidgets.QLineEdit(Old)
        self.path_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.path_1.setFont(font)
        self.path_1.setObjectName("path_1")
        self.gridLayout.addWidget(self.path_1, 4, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Old)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 8)

        self.retranslateUi(Old)
        QtCore.QMetaObject.connectSlotsByName(Old)

    def retranslateUi(self, Old):
        _translate = QtCore.QCoreApplication.translate
        Old.setWindowTitle(_translate("Old", "Form"))
        self.label.setText(_translate("Old", "数据展示"))
        self.label_2.setText(_translate("Old", "IC数据路径"))
        self.pushButton.setText(_translate("Old", "删除全部图像"))
        self.format.setItemText(0, _translate("Old", "Excel"))
        self.format.setItemText(1, _translate("Old", "Txt"))
        self.analyse.setText(_translate("Old", "数据分析"))
        self.choose_1.setText(_translate("Old", "..."))
        self.label_6.setText(_translate("Old", "锂电池老化分析"))
        self.label_5.setText(_translate("Old", "量化分析结果储存路径"))
        self.choose_2.setText(_translate("Old", "..."))
        self.label_4.setText(_translate("Old", "初始循环IC峰值："))
        self.label_3.setText(_translate("Old", "LAM量化结果"))
