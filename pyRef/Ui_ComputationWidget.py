# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'computationWidgetkbctGg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ComputationWidget(object):
    def setupUi(self, ComputationWidget):
        if not ComputationWidget.objectName():
            ComputationWidget.setObjectName(u"ComputationWidget")
        ComputationWidget.resize(501, 454)
        self.ComputationWidget_gridLayout = QGridLayout(ComputationWidget)
        self.ComputationWidget_gridLayout.setSpacing(0)
        self.ComputationWidget_gridLayout.setObjectName(u"ComputationWidget_gridLayout")
        self.ComputationWidget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.centralFrame = QFrame(ComputationWidget)
        self.centralFrame.setObjectName(u"centralFrame")
        self.centralFrame.setFrameShape(QFrame.StyledPanel)
        self.centralFrame_gridLayout = QGridLayout(self.centralFrame)
        self.centralFrame_gridLayout.setSpacing(0)
        self.centralFrame_gridLayout.setObjectName(u"centralFrame_gridLayout")
        self.centralFrame_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.shabGrid = QGridLayout()
        self.shabGrid.setSpacing(0)
        self.shabGrid.setObjectName(u"shabGrid")
        self.kinematicLabel = QLabel(self.centralFrame)
        self.kinematicLabel.setObjectName(u"kinematicLabel")
        self.kinematicLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.kinematicLabel, 0, 0, 1, 1)

        self.alphaComboBox = QComboBox(self.centralFrame)
        self.alphaComboBox.setObjectName(u"alphaComboBox")

        self.shabGrid.addWidget(self.alphaComboBox, 3, 1, 1, 1)

        self.pdfComboBox = QComboBox(self.centralFrame)
        self.pdfComboBox.setObjectName(u"pdfComboBox")

        self.shabGrid.addWidget(self.pdfComboBox, 1, 1, 1, 1)

        self.pdfModHorizontalLayout = QHBoxLayout()
        self.pdfModHorizontalLayout.setSpacing(0)
        self.pdfModHorizontalLayout.setObjectName(u"pdfModHorizontalLayout")
        self.pdfModLineEdit = QLineEdit(self.centralFrame)
        self.pdfModLineEdit.setObjectName(u"pdfModLineEdit")

        self.pdfModHorizontalLayout.addWidget(self.pdfModLineEdit)

        self.pdfModBtn = QPushButton(self.centralFrame)
        self.pdfModBtn.setObjectName(u"pdfModBtn")

        self.pdfModHorizontalLayout.addWidget(self.pdfModBtn)


        self.shabGrid.addLayout(self.pdfModHorizontalLayout, 2, 1, 1, 1)

        self.kinemHorizontalLayout = QHBoxLayout()
        self.kinemHorizontalLayout.setSpacing(0)
        self.kinemHorizontalLayout.setObjectName(u"kinemHorizontalLayout")
        self.kinemFileLineEdit = QLineEdit(self.centralFrame)
        self.kinemFileLineEdit.setObjectName(u"kinemFileLineEdit")

        self.kinemHorizontalLayout.addWidget(self.kinemFileLineEdit)

        self.kinemFileBtn = QPushButton(self.centralFrame)
        self.kinemFileBtn.setObjectName(u"kinemFileBtn")

        self.kinemHorizontalLayout.addWidget(self.kinemFileBtn)


        self.shabGrid.addLayout(self.kinemHorizontalLayout, 0, 1, 1, 1)

        self.binsLabel = QLabel(self.centralFrame)
        self.binsLabel.setObjectName(u"binsLabel")
        self.binsLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.binsLabel, 6, 0, 1, 1)

        self.alphaLabel = QLabel(self.centralFrame)
        self.alphaLabel.setObjectName(u"alphaLabel")
        self.alphaLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.alphaLabel, 3, 0, 1, 1)

        self.integratorComboBox = QComboBox(self.centralFrame)
        self.integratorComboBox.setObjectName(u"integratorComboBox")

        self.shabGrid.addWidget(self.integratorComboBox, 4, 1, 1, 1)

        self.binCutLabel = QLabel(self.centralFrame)
        self.binCutLabel.setObjectName(u"binCutLabel")
        self.binCutLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.binCutLabel, 5, 0, 1, 1)

        self.pdfLabel = QLabel(self.centralFrame)
        self.pdfLabel.setObjectName(u"pdfLabel")
        self.pdfLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.pdfLabel, 1, 0, 1, 1)

        self.integratorLabel = QLabel(self.centralFrame)
        self.integratorLabel.setObjectName(u"integratorLabel")
        self.integratorLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.integratorLabel, 4, 0, 1, 1)

        self.pdfModLabel = QLabel(self.centralFrame)
        self.pdfModLabel.setObjectName(u"pdfModLabel")
        self.pdfModLabel.setAlignment(Qt.AlignCenter)

        self.shabGrid.addWidget(self.pdfModLabel, 2, 0, 1, 1)

        self.binCutHorizontalLayout = QHBoxLayout()
        self.binCutHorizontalLayout.setSpacing(0)
        self.binCutHorizontalLayout.setObjectName(u"binCutHorizontalLayout")
        self.binCutLineEdit = QLineEdit(self.centralFrame)
        self.binCutLineEdit.setObjectName(u"binCutLineEdit")

        self.binCutHorizontalLayout.addWidget(self.binCutLineEdit)

        self.binCutBnt = QPushButton(self.centralFrame)
        self.binCutBnt.setObjectName(u"binCutBnt")

        self.binCutHorizontalLayout.addWidget(self.binCutBnt)


        self.shabGrid.addLayout(self.binCutHorizontalLayout, 5, 1, 1, 1)

        self.binsVerticalLayout = QVBoxLayout()
        self.binsVerticalLayout.setSpacing(0)
        self.binsVerticalLayout.setObjectName(u"binsVerticalLayout")
        self.binsHandHorizontalLayout = QHBoxLayout()
        self.binsHandHorizontalLayout.setSpacing(0)
        self.binsHandHorizontalLayout.setObjectName(u"binsHandHorizontalLayout")
        self.binsHandHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.binsNumLineEdit = QLineEdit(self.centralFrame)
        self.binsNumLineEdit.setObjectName(u"binsNumLineEdit")
        self.binsNumLineEdit.setAlignment(Qt.AlignCenter)

        self.binsHandHorizontalLayout.addWidget(self.binsNumLineEdit)

        self.binsStartLineEdit = QLineEdit(self.centralFrame)
        self.binsStartLineEdit.setObjectName(u"binsStartLineEdit")
        self.binsStartLineEdit.setAlignment(Qt.AlignCenter)

        self.binsHandHorizontalLayout.addWidget(self.binsStartLineEdit)

        self.binsDeltaLineEdit = QLineEdit(self.centralFrame)
        self.binsDeltaLineEdit.setObjectName(u"binsDeltaLineEdit")
        self.binsDeltaLineEdit.setAlignment(Qt.AlignCenter)

        self.binsHandHorizontalLayout.addWidget(self.binsDeltaLineEdit)


        self.binsVerticalLayout.addLayout(self.binsHandHorizontalLayout)

        self.binsFileHorizontalLayout = QHBoxLayout()
        self.binsFileHorizontalLayout.setSpacing(0)
        self.binsFileHorizontalLayout.setObjectName(u"binsFileHorizontalLayout")
        self.binsFileHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.binsFileCheckBox = QCheckBox(self.centralFrame)
        self.binsFileCheckBox.setObjectName(u"binsFileCheckBox")

        self.binsFileHorizontalLayout.addWidget(self.binsFileCheckBox)

        self.BinsFileLineEdit = QLineEdit(self.centralFrame)
        self.BinsFileLineEdit.setObjectName(u"BinsFileLineEdit")
        self.BinsFileLineEdit.setEnabled(False)

        self.binsFileHorizontalLayout.addWidget(self.BinsFileLineEdit)

        self.binsFileBtn = QPushButton(self.centralFrame)
        self.binsFileBtn.setObjectName(u"binsFileBtn")
        self.binsFileBtn.setEnabled(False)

        self.binsFileHorizontalLayout.addWidget(self.binsFileBtn)


        self.binsVerticalLayout.addLayout(self.binsFileHorizontalLayout)


        self.shabGrid.addLayout(self.binsVerticalLayout, 6, 1, 1, 1)


        self.centralFrame_gridLayout.addLayout(self.shabGrid, 1, 0, 1, 1)

        self.parametersVerticalLayout = QVBoxLayout()
        self.parametersVerticalLayout.setSpacing(0)
        self.parametersVerticalLayout.setObjectName(u"parametersVerticalLayout")
        self.parametersVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.parametersHorizontalLayout = QHBoxLayout()
        self.parametersHorizontalLayout.setSpacing(0)
        self.parametersHorizontalLayout.setObjectName(u"parametersHorizontalLayout")
        self.parametersHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.parametersLabel = QLabel(self.centralFrame)
        self.parametersLabel.setObjectName(u"parametersLabel")
        self.parametersLabel.setAlignment(Qt.AlignCenter)

        self.parametersHorizontalLayout.addWidget(self.parametersLabel)

        self.addParametersBtn = QPushButton(self.centralFrame)
        self.addParametersBtn.setObjectName(u"addParametersBtn")

        self.parametersHorizontalLayout.addWidget(self.addParametersBtn)

        self.removeParametersBtn = QPushButton(self.centralFrame)
        self.removeParametersBtn.setObjectName(u"removeParametersBtn")

        self.parametersHorizontalLayout.addWidget(self.removeParametersBtn)


        self.parametersVerticalLayout.addLayout(self.parametersHorizontalLayout)

        self.parametersTableWidget = QTableWidget(self.centralFrame)
        if (self.parametersTableWidget.columnCount() < 2):
            self.parametersTableWidget.setColumnCount(2)
        if (self.parametersTableWidget.rowCount() < 1):
            self.parametersTableWidget.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.parametersTableWidget.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.parametersTableWidget.setItem(0, 1, __qtablewidgetitem1)
        self.parametersTableWidget.setObjectName(u"parametersTableWidget")
        self.parametersTableWidget.setRowCount(1)
        self.parametersTableWidget.setColumnCount(2)
        self.parametersTableWidget.horizontalHeader().setVisible(False)

        self.parametersVerticalLayout.addWidget(self.parametersTableWidget)


        self.centralFrame_gridLayout.addLayout(self.parametersVerticalLayout, 2, 0, 1, 1)

        self.nameLabel = QLabel(self.centralFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setAlignment(Qt.AlignCenter)

        self.centralFrame_gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)


        self.ComputationWidget_gridLayout.addWidget(self.centralFrame, 0, 0, 1, 1)


        self.retranslateUi(ComputationWidget)

        QMetaObject.connectSlotsByName(ComputationWidget)
    # setupUi

    def retranslateUi(self, ComputationWidget):
        self.kinematicLabel.setText(QCoreApplication.translate("ComputationWidget", u"Kinematic", None))
        self.pdfModBtn.setText(QCoreApplication.translate("ComputationWidget", u"file", None))
        self.kinemFileBtn.setText(QCoreApplication.translate("ComputationWidget", u"file", None))
        self.binsLabel.setText(QCoreApplication.translate("ComputationWidget", u"BINs", None))
        self.alphaLabel.setText(QCoreApplication.translate("ComputationWidget", u"Alpha", None))
        self.binCutLabel.setText(QCoreApplication.translate("ComputationWidget", u"BIN cut", None))
        self.pdfLabel.setText(QCoreApplication.translate("ComputationWidget", u"PDF", None))
        self.integratorLabel.setText(QCoreApplication.translate("ComputationWidget", u"Integrator", None))
        self.pdfModLabel.setText(QCoreApplication.translate("ComputationWidget", u"PDF mod", None))
        self.binCutBnt.setText(QCoreApplication.translate("ComputationWidget", u"PushButton", None))
        self.binsNumLineEdit.setText(QCoreApplication.translate("ComputationWidget", u"Num", None))
        self.binsStartLineEdit.setText(QCoreApplication.translate("ComputationWidget", u"Start", None))
        self.binsDeltaLineEdit.setText(QCoreApplication.translate("ComputationWidget", u"Delta", None))
        self.binsFileCheckBox.setText(QCoreApplication.translate("ComputationWidget", u"File", None))
        self.binsFileBtn.setText(QCoreApplication.translate("ComputationWidget", u"PushButton", None))
        self.parametersLabel.setText(QCoreApplication.translate("ComputationWidget", u"Parameters", None))
        self.addParametersBtn.setText(QCoreApplication.translate("ComputationWidget", u"+", None))
        self.removeParametersBtn.setText(QCoreApplication.translate("ComputationWidget", u"-", None))

        __sortingEnabled = self.parametersTableWidget.isSortingEnabled()
        self.parametersTableWidget.setSortingEnabled(False)
        ___qtablewidgetitem = self.parametersTableWidget.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ComputationWidget", u"Param name", None));
        ___qtablewidgetitem1 = self.parametersTableWidget.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ComputationWidget", u"Param Num", None));
        self.parametersTableWidget.setSortingEnabled(__sortingEnabled)

        self.nameLabel.setText(QCoreApplication.translate("ComputationWidget", u"nameLabel", None))
        pass
    # retranslateUi
