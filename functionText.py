from PyQt5.QtWidgets import QFileDialog, qApp, QMessageBox
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
import datetime
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class Function(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # shortcut
        self.shortcutNew = QShortcut(QKeySequence("Ctrl+N"), self)
        self.shortcutOpen = QShortcut(QKeySequence("Ctrl+O"), self)
        self.shortcutSave = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcutNew.activated.connect(self.NewFile)
        self.shortcutOpen.activated.connect(self.OpenFile)
        self.shortcutSave.activated.connect(self.SaveFile)

        #button action
        self.actionNew.triggered.connect(self.NewFile)
        self.actionOpen.triggered.connect(self.OpenFile)
        self.actionSave.triggered.connect(self.SaveFile)
        self.actionExit.triggered.connect(self.Exit)
        self.actionSave_as.triggered.connect(self.SaveFile)
        self.actionAbout.triggered.connect(self.About)
        self.actionUndo.triggered.connect(self.Undo)
        self.actionTime_Date.triggered.connect(self.Time_Date)
        self.actionPage_Setup.triggered.connect(self.PrintFile)
        self.actionFont.triggered.connect(self.fontOptions)
        #else
        self.textname
    #action
    def NewFile(self):
        self.textEdit.clear()
    def OpenFile(self):
        self.textname = QFileDialog.getOpenFileName(self, "OpenFile")
        if self.textname[0]:
            t = open(self.textname[0], 'r')
            with t:
                text = t.read()
                self.textEdit.setText(text)
    def SaveFile(self):
        self.textname = QFileDialog.getSaveFileName(self, 'SaveFile')
        if self.textname[0]:
            t = open(self.textname[0], "w")
            with t:
                text = self.textEdit.toPlainText()
                t.write(text)
    def About(self):
        QMessageBox.warning(self, 'About',
                            'Created by Marek Synos', QMessageBox.Ok)
    def Undo(self):
        self.textEdit.undo()
    def Time_Date(self):
        a = datetime.datetime.now()
        self.textEdit.insertPlainText(str(a))
    def PrintFile(self):
        p1 = QPrinter(QPrinter.HighResolution)
        p2 = QPrintDialog(p1, self)
        if p2.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(p1)
    def Exit(self):
        qApp.quit()
