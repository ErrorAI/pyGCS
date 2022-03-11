# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QFrame, QComboBox, QLabel, QFileDialog, QGridLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from ComputationFunctional import ComputationFunctional
from Ui_ComputationWidget import Ui_ComputationWidget

class ComputationWidget(QtWidgets.QWidget):
    def __init__(self, parent, position, name):
        super(ComputationWidget, self).__init__()

        self.fullWidth = 300
        self.fullHeight = 300

        self.name = name
        self.functional = ComputationFunctional(self.name)

        self.ui = Ui_ComputationWidget()
        self.ui.setupUi(self)

        self.ui.binsFileCheckBox.clicked.connect(self._binFileCheckBox_clicked)

        self.setGeometry(position[0], position[1], self.fullWidth, self.fullHeight)
        self.setParent(parent)

    def _runComputation(self):
        self.functional.runComputation()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.pos().y() < self.ui.nameLabel.height():
                self.old_pos = event.pos()

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        self.delta = event.pos() - self.old_pos
        if event.pos().y() < self.ui.nameLabel.height():
            self.move(self.pos() + self.delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def _binFileCheckBox_clicked(self, event):
        if self.ui.binsDeltaLineEdit.isEnabled() == True:
            self.ui.binsDeltaLineEdit.setEnabled(False)
            self.ui.binsNumLineEdit.setEnabled(False)
            self.ui.binsStartLineEdit.setEnabled(False)

            self.ui.BinsFileLineEdit.setEnabled(True)
            self.ui.binsFileBtn.setEnabled(True)
        else:
            self.ui.binsDeltaLineEdit.setEnabled(True)
            self.ui.binsNumLineEdit.setEnabled(True)
            self.ui.binsStartLineEdit.setEnabled(True)

            self.ui.BinsFileLineEdit.setEnabled(False)
            self.ui.binsFileBtn.setEnabled(False)
        pass
