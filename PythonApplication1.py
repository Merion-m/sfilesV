from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton 
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        button = QPushButton('Button')
        self.setCentralWidget(button)
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()