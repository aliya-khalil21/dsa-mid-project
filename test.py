import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import pandas as pd
from sorting import callingfunction
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('PROJECT.ui', self)

        # Accessing pushButton_2 by its object name
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.callingfunction)
        self.button_2.clicked.connect(self.trigger_sorting)
    
    def pushButton_clicked(self):
        self.callingfunction()  # Call the function directly

        # Perform your sorting and saving here
        # For example, uncomment and replace with your sorting logic
        # result = merge_sort(a, column_to_sort)
        # a.to_csv(r'C:\Users\Admin\Desktop\midproject\smashwordsorted.csv', index=False)
        print("DataFrame sorted and saved to 123.")

    def bubblesort(self, arr, col_name):  # Added 'self'
        n = len(arr)
        print(len(arr))
        print('mH')
        for i in range(n):
            print(i)
            swapped = False
            for j in range(0, n - i - 1):
                
                if arr.iloc[j][col_name] > arr.iloc[j + 1][col_name]:
                    arr.iloc[j], arr.iloc[j + 1] = arr.iloc[j + 1].copy(), arr.iloc[j].copy()
                    swapped = True
           

    def callingfunction(self):  # Added 'self'
        file_path = r'C:\Users\hp\Downloads\Book1.csv'
        a = pd.read_csv(file_path)
        print(a)
        column_to_sort = 'name'
        self.bubblesort(a, column_to_sort)  # Added 'self'
        a.to_csv(r'C:\Users\hp\OneDrive\Desktop\midproject\resources\smashwordsorted.csv', index=False)
        print("DataFrame sorted and saved to 'smashwordsorted.csv'.")
        exit

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
