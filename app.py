# Text editor app

# import modules
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox, QSplashScreen
from PyQt6 import QtWidgets, QtGui, QtCore
import sys

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Text Editor")

        # set window icon
        self.setWindowIcon(QIcon("icons/icon.png"))

        # set window size
        self.setGeometry(100, 100, 1200, 800)

        # create text editor
        self.textEdit = QTextEdit(self)

        # set text editor font
        self.textEdit.setFont(QtGui.QFont("Times", 14))

        # set text editor tab width
        self.textEdit.setTabStopDistance(33)

        # set text editor background color
        self.textEdit.setStyleSheet("background-color: #fff")

        # set text editor text color
        self.textEdit.setStyleSheet("color: #000")

        # set text editor text alignment
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # set text editor text cursor
        self.textEdit.setTextCursor(QtGui.QTextCursor())

        # set text editor text cursor color
        self.textEdit.setStyleSheet("QTextEdit { selection-background-color: #000; selection-color: #fff; }")
        
        # set text editor as central widget
        self.setCentralWidget(self.textEdit)

        # create status bar
        self.statusBar = self.statusBar()

        # set status bar text
        self.statusBar.showMessage("Text Editor")

        # create menu bar
        self.menuBar = self.menuBar()

        # create file menu
        self.fileMenu = self.menuBar.addMenu("File")

        # create edit menu
        self.editMenu = self.menuBar.addMenu("Edit")

        # create view menu
        self.viewMenu = self.menuBar.addMenu("View")

        # create help menu
        self.helpMenu = self.menuBar.addMenu("Help")

        # create file menu actions
        # create new file action
        self.newFileAction = QtGui.QAction(QIcon("icons/new.png"), "New File", self)
        self.newFileAction.setShortcut("Ctrl+N")
        self.newFileAction.triggered.connect(self.newFile)

        # create open file action
        self.openFileAction = QtGui.QAction(QIcon("icons/open.png"), "Open File", self)
        self.openFileAction.setShortcut("Ctrl+O")
        self.openFileAction.triggered.connect(self.openFile)

        # create save file action
        self.saveFileAction = QtGui.QAction(QIcon("icons/save.png"), "Save File", self)
        self.saveFileAction.setShortcut("Ctrl+S")
        self.saveFileAction.triggered.connect(self.saveFile)

        # create exit action
        self.exitAction = QtGui.QAction(QIcon("icons/exit.png"), "Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(self.exit)

        # add file menu actions
        self.fileMenu.addAction(self.newFileAction)
        self.fileMenu.addAction(self.openFileAction)
        self.fileMenu.addAction(self.saveFileAction)
        self.fileMenu.addAction(self.exitAction)

        # create edit menu actions
        # create cut action
        self.cutAction = QtGui.QAction(QIcon("icons/cut.png"), "Cut", self)
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.textEdit.cut)

        # create copy action
        self.copyAction = QtGui.QAction(QIcon("icons/copy.png"), "Copy", self)
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.textEdit.copy)

        # create paste action
        self.pasteAction = QtGui.QAction(QIcon("icons/paste.png"), "Paste", self)
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.textEdit.paste)

        # create select all action
        self.selectAllAction = QtGui.QAction(QIcon("icons/selectAll.png"), "Select All", self)
        self.selectAllAction.setShortcut("Ctrl+A")
        self.selectAllAction.triggered.connect(self.textEdit.selectAll)

        # create clear all action
        self.clearAllAction = QtGui.QAction(QIcon("icons/clearAll.png"), "Clear All", self)
        self.clearAllAction.setShortcut("Ctrl+Shift+A")
        self.clearAllAction.triggered.connect(self.textEdit.clear)

        # add edit menu actions
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.selectAllAction)
        self.editMenu.addAction(self.clearAllAction)

        # create view menu actions
        # create dark theme action
        self.darkThemeAction = QtGui.QAction(QIcon("icons/darkTheme.png"), "Dark Theme", self)
        self.darkThemeAction.setShortcut("Ctrl+D")
        self.darkThemeAction.triggered.connect(self.darkTheme)

        # create light theme action
        self.lightThemeAction = QtGui.QAction(QIcon("icons/lightTheme.png"), "Light Theme", self)
        self.lightThemeAction.setShortcut("Ctrl+L")
        self.lightThemeAction.triggered.connect(self.lightTheme)

        # add view menu actions
        self.viewMenu.addAction(self.darkThemeAction)
        self.viewMenu.addAction(self.lightThemeAction)

        # create help menu actions
        # create about action
        self.aboutAction = QtGui.QAction(QIcon("icons/about.png"), "About", self)
        self.aboutAction.setShortcut("Ctrl+H")
        self.aboutAction.triggered.connect(self.about)

        # add help menu actions
        self.helpMenu.addAction(self.aboutAction)

        # create tool bar and add actions
        self.toolBar = self.addToolBar("Tool Bar")

        # add tool bar actions
        self.toolBar.addAction(self.newFileAction)
        self.toolBar.addAction(self.openFileAction)
        self.toolBar.addAction(self.saveFileAction)
        self.toolBar.addAction(self.cutAction)
        self.toolBar.addAction(self.copyAction)
        self.toolBar.addAction(self.pasteAction)
        self.toolBar.addAction(self.selectAllAction)
        self.toolBar.addAction(self.clearAllAction)

        # set window title
        self.setWindowTitle("Text Editor")

        # set window icon
        self.setWindowIcon(QIcon("icons/icon.png"))

        # show window
        self.show()

    # create new file method
    def newFile(self):
        # clear text
        self.textEdit.clear()

    # create open file method
    def openFile(self):
        # get file path
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py);;All Files (*.*)")

        # open file
        try:
            with open(filePath, "r") as file:
                # read file
                self.textEdit.setText(file.read())
        except Exception as e:
            print(e)

    # create save file method
    def saveFile(self):
        # get file path
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;Python Files (*.py);;All Files (*.*)")

        # save file
        try:
            with open(filePath, "w") as file:
                # write to file
                file.write(self.textEdit.toPlainText())
        except Exception as e:
            print(e)

    # create exit method
    def exit(self):
        # exit
        sys.exit()

    # create cut method
    def cut(self):
        # cut text
        self.textEdit.cut()

    # create copy method
    def copy(self):
        # copy text
        self.textEdit.copy()

    # create paste method
    def paste(self):
        # paste text
        self.textEdit.paste()

    # create select all method
    def selectAll(self):
        # select all text
        self.textEdit.selectAll()

    # create clear all method
    def clearAll(self):
        # clear all text
        self.textEdit.clear()

    # create dark theme method
    def darkTheme(self):
        # set dark theme stylesheet
        style = open("themes/dark.css", "r")
        style = style.read()
        self.setStyleSheet(style)

    # create light theme method
    def lightTheme(self):
        # set light theme stylesheet
        style = open("themes/light.css", "r")
        style = style.read()
        self.setStyleSheet(style)

    # create about method
    def about(self):
        # open about file and show in new window
        # create dialog window
        self.aboutDialog = QtWidgets.QDialog(self)
        self.aboutDialog.setWindowTitle("About")
        self.aboutDialog.setWindowIcon(QIcon("icons/icon.png"))
        self.aboutDialog.setFixedSize(300, 300)
        
        # read about file
        try:
            with open("about.txt", "r") as file:
                
                # read file
                aboutText = file.read()
        except Exception as e:
            print(e)

        # create label
        self.aboutLabel = QtWidgets.QLabel()
        self.aboutLabel.setText(aboutText)

        # create ok button
        self.okButton = QtWidgets.QPushButton("OK")
        self.okButton.clicked.connect(self.aboutDialog.close)

        # create vertical box layout
        self.aboutVBoxLayout = QtWidgets.QVBoxLayout()
        self.aboutVBoxLayout.addWidget(self.aboutLabel)
        self.aboutVBoxLayout.addWidget(self.okButton)

        # set dialog layout
        self.aboutDialog.setLayout(self.aboutVBoxLayout)

        # show dialog
        self.aboutDialog.exec()


# load empty.txt before start the app
try:
    with open("empty.rdv", "r") as file:
        # read file
        window.textEdit.setText(file.read())
        # black color text
        self.textEdit.setStyleSheet("color: #000")
except Exception as e:
    print(e)

# start the app
    app = QApplication(sys.argv)
    
    # Show the splash screen
    splash = QSplashScreen()

    # Create the main window
    window = MainWindow()

    # Show the main window
    window.show()

    # Close the splash screen after the main window is shown
    splash.close()

    sys.exit(app.exec())









        




