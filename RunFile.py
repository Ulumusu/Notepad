import sys
from PyQt5.QtWidgets import QApplication
from functionText import Function



app = QApplication(sys.argv)
texteditor=Function()
sys.exit(app.exec())