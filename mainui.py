from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from sorting import Sorting
import csv
from newest import main 
import sys
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import datetime
import time
from Search import Search
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.DataTable = QTableWidget()
        loadUi('untitled.ui', self)
        try:
         self.DataTable = self.tableWidget
         self.load_DataFromFile('smashwordsorted1.csv')
        except Exception as e:
            print(f"An error occurred: {e}") 
        self.pushButton_3.setObjectName("pushbutton")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton2_clicked)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.start_scraping)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.stop_scraping)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.close)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.pause)
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.search)

    def convert_columns_to_int(self, data):
        
        for row in data[1:]:
            for i in [2, 3, 5]:
                
                row[i] = float(row[i].replace(',', ''))

        return data
    
        
    def trigger_sorting(self, sorting_algorithm,column_to_sort,ascending):
      try:   
        file_path = r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted1.csv'
        
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
          
          datais = list(csv.reader(file))
        
        datais = self.convert_columns_to_int(datais)       
        header=datais[0]
        indextosort=header.index(column_to_sort)

        start_time = time.time()
        data=self.sorting_instance.callingfunction(sorting_algorithm,datais, indextosort,ascending)

        

        with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        self.load_DataFromFile('smashwordsorted.csv')
        print("Data sorted and saved to 'smashwordsorted.csv'")
        return
      except Exception as e:
            print(f"An error occurred: {e}")  
            
    def load_DataFromFile(self,filename):
        with open(filename, 'r', encoding='iso-8859-1') as fileInput:
            
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.DataTable.setRowCount(len(self.data))
            
            
            for row in self.data:
                
                self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))

                self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                self.DataTable.setItem(tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
                self.DataTable.setItem(tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
                #self.DataTable.setItem(tableRows, 8, QtWidgets.QTableWidgetItem((row[8])))
                tableRows += 1

    def load_Data(self):
        tableRows = 0
        self.DataTable.setRowCount(len(self.data))
        for row in self.data:
            self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
            self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
            self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
            self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
            if int(row[5].split(":")[0]) >= int(24):
                row[5] = row[5][0:len(row[5]) - 1]
            self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            self.DataTable.setItem(tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
            self.DataTable.setItem(tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
            #self.DataTable.setItem(tableRows, 8, QtWidgets.QTableWidgetItem((row[8])))
            tableRows += 1


    

    def pushButton2_clicked(self):
        second_page = loadUi('untitled.ui')
        
        second_page.pushButton_3.setObjectName("pushButton_4")
        second_page.pushButton.clicked.connect(self.start_scraping)
        self.DataTable = second_page.tableWidget
        self.load_DataFromFile('smashwordsorted1.csv')
        
        self.setCentralWidget(second_page)

    def search(self):
     try:
        second_page=loadUi('a.ui')
        self.setCentralWidget(second_page)
        push_button = second_page.findChild(QPushButton, "pushButton")

        push_button.clicked.connect(
            lambda: self.trigger_searching(
                second_page.findChild(QWidget, "widget").findChild(QComboBox, "comboBox_2").currentText(),
                second_page.findChild(QWidget, "widget").findChild(QComboBox, "comboBox_3").currentText(),
                second_page.findChild(QWidget, "widget").findChild(QComboBox, "textEdit").Text()
            ))
        self.searching_instance = Search()
     except Exception as e:
            print(f"An error occurred: {e}")
    def trigger_searching(self, algorithm, column_to_search, value):
     try:
        file_path = r'C:\Users\Admin\Desktop\alia\resources\Book1.csv'

        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            datais = list(csv.reader(file))

        data = self.searching_instance.LinearSearch(datais, algorithm, value, column_to_search)
        print(data)
     except Exception as e:
            print(f"An error occurred: {e}")  
    def pushButton_clicked(self):
      try:  
        second_page = loadUi('PROJECT.ui')  
        self.setCentralWidget(second_page)
        push_button = second_page.findChild(QWidget, "widget_3").findChild(QPushButton, "pushButtonofsingle")
        start_time=time.time()
        push_button.clicked.connect(
        
    lambda: self.handle_button_click(
        second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox").currentText(),
        second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox_2").currentText(),
        second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox_3").currentText()
    )
) 
        self.sorting_instance = Sorting()
        self.DataTable = second_page.tableWidget
        self.load_DataFromFile('smashwordsorted1.csv')
        
        end_time=time.time()
        diff=start_time-end_time
        lable=self.findChild(QWidget, "widget_2").findChild(QLCDNumber, "lcdNumber")
        lable.display(diff)


      except Exception as e:
            print(f"An error occurred: {e}")  

    def handle_button_click(self, combo_1, combo_2, combo_3):
        if combo_1 != "none" and combo_2 != "none" and combo_3 != "none":
            if combo_1 in ["countingsort", "radixsort",'bucketsort']:
                valid_options = ["price", "words", "date"]
                if combo_2 not in valid_options:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText(f"For {combo_1}, valid options for the second combo are: {', '.join(valid_options)}.")
                    msg.setWindowTitle("Invalid Input")
                    msg.exec_()
                else:
                    self.trigger_sorting(combo_1, combo_2, combo_3)

            else:
                self.trigger_sorting(combo_1, combo_2, combo_3)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please choose valid values in all ComboBoxes.")
            msg.setWindowTitle("Invalid Input")
            msg.exec_()


    def start_scraping(self):
        
        thread=Thread(target=main,daemon=True,args=(True,True,'https://www.smashwords.com/books/category/1/newest/0/any/any/95000','https://www.smashwords.com/books/category/1/newest/0/any/any/'))
        thread.start()

    def stop_scraping(self):
        main(False,True,'https://www.smashwords.com/books/category/1/newest/0/any/any/95000','https://www.smashwords.com/books/category/1/newest/0/any/any/')
        self.DataTable = self.tableWidget
        self.load_DataFromFile('smashwordsorted1.csv')
        
        
    def pause(self):
        
        with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'r',encoding='utf-8') as file:
            content=file.read()
        print(content)
        main(True,False,content,'https://www.smashwords.com/books/category/1/newest/0/any/any/')
        self.DataTable = self.tableWidget
        self.load_DataFromFile('smashwordsorted1.csv')
    def resume(self):
            with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'r',encoding='utf-8') as file:
                content=file.read()
            thread=Thread(target=main,daemon=True,args=(True,True,content,'https://www.smashwords.com/books/category/1/newest/0/any/any/'))
            thread.start()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

