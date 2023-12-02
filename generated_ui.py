import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('PROJECT.ui', self)

        # Accessing pushButton_3 by its object name
        self.pushButton_3.setObjectName("pushButton")

        # Connect the button click event to a function
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        second_page = loadUi('SWDFJ.ui')
        self.setCentralWidget(second_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
