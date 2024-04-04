import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from utils import Utils
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.directory = 'Input Files'
        self.outputFilePath = 'output.txt'
        self.utils = Utils()

        self.utils.getFilesFromDirectory(self.directory)

        self.setWindowTitle("PyQt5 Template")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Hello, PyQt5!", self)
        self.label.setGeometry(50, 50, 300, 100)

        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(150, 150, 100, 30)
        self.button.clicked.connect(self.button_clicked)

    def hideLoadingLabel(self):
        self.label_loading.hide()

    def button_clicked(self):
        filesNames = self.utils.getFilesFromDirectory(self.directory)

        self.label_loading = QLabel("Loading...", self)
        self.label_loading.setGeometry(50, 50, 400, 200)
        self.label_loading.show()

        for file in filesNames:
            print(file)
            if(file != ".DS_Store"):
                barcode = self.utils.getBarcodeFromImage(file)
                self.utils.putNameAndBarecodeIntoTxtFile(file, self.outputFilePath, barcode)
        
        QTimer.singleShot(5000, self.hideLoadingLabel)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
