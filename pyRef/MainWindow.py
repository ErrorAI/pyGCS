from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QToolBar, QAction, QMenu
from PyQt5.QtGui import QPalette

from ComputationWidget import ComputationWidget

class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("ECS")
        self.resize(500, 500)
        self._createCentralWidget()

        self._createActions()
        self._connectActions()
        self._createMenuBar()
        self._createToolBars()

        self.listOfComputationWidget = []

    def _createCentralWidget(self):
        self.centralWidget = QWidget(self)

        palete = QPalette();
        palete.setColor(QPalette.Background, Qt.lightGray);
        self.centralWidget.setAutoFillBackground(True);
        self.centralWidget.setPalette(palete);

        self.setCentralWidget(self.centralWidget)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        # Edit menu
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction(self.findAction)
        findMenu.addAction(self.replaceAction)
        # Help menu
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        # Using a QToolBar object
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)
        helpToolBar.addAction(self.helpContentAction)
        helpToolBar.addAction(self.aboutAction)

    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction("New",self)
        self.newComputationAction = QAction("New Computation",self)
        # Creating actions using the second constructor
        self.openAction = QAction("Open...", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.helpContentAction = QAction("Help Content", self)
        self.aboutAction = QAction("About", self)
        self.findAction = QAction("Find...",self)
        self.replaceAction = QAction("Replace...",self)

    def _connectActions(self):
        # Connect File actions
        self.newAction.triggered.connect(self.newFile)
        self.newComputationAction.triggered.connect(self.newComputation)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        # Connect Edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        # Connect Help actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

    def contextMenuEvent(self, event):
        #tmpEventPose = [event.pos().x(),event.pos().y()]
        self.tmpEventPoseInCentralWidget = [event.pos().x()-self.centralWidget.pos().x(), event.pos().y()-self.centralWidget.pos().y()]
        # Creating a menu object with the central widget as parent
        menu = QMenu(self.centralWidget)
        # Populating the menu with actions
        menu.addAction(self.newComputationAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        separator = QAction(self)
        separator.setSeparator(True)
        menu.addAction(separator)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.cutAction)
        # Launching the menu
        menu.exec(event.globalPos())

    def newComputation(self):
        comp = ComputationWidget(self.centralWidget, self.tmpEventPoseInCentralWidget, "comp"+str(len(self.listOfComputationWidget)))
        comp.show()
        self.listOfComputationWidget.append(comp)
        pass

    def newFile(self):
        # Logic for creating a new file goes here...
        pass

    def openFile(self):
        # Logic for opening an existing file goes here...
        pass

    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Pate</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        # Logic for launching help goes here...
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        # Logic for showing an about dialog content goes here...
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.listOfComputationWidget != []:
                self.old_pos = event.pos()

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.old_pos = event.pos()
        for comp in self.listOfComputationWidget:
            comp.move(comp.pos() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None
