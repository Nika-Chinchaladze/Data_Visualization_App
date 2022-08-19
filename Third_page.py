from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic
import pandas as pd

class AquaMan(QMainWindow):
    def __init__(self):
        super(AquaMan, self).__init__()

        uic.loadUi("THREE.ui", self)

        # define content:
        self.hello_label = self.findChild(QLabel, "hello_label")
        self.secret_label_3 = self.findChild(QLabel, "secret_label_3")
        self.open_file_button = self.findChild(QPushButton, "open_file_button")
        self.return_button = self.findChild(QPushButton, "return_button")
        self.cross_line = self.findChild(QFrame, "cross_line")
        self.table_widget = self.findChild(QTableWidget, "table_widget")

        # call defined methods from here:
        self.open_file_button.clicked.connect(self.Open_File)
        self.return_button.clicked.connect(self.Come_Back)

        self.show()

# ------------------------------------------ logic -------------------------------------- #
    # define methof for open file button:
    def Open_File(self):
        file_name = self.secret_label_3.text()
        self.upload_file = pd.read_csv(f"{file_name}")
        
        RowNumber = len(self.upload_file.index)
        ColumnNumber = len(self.upload_file.columns)

        self.table_widget.setColumnCount(ColumnNumber)
        self.table_widget.setRowCount(RowNumber)
        self.table_widget.setHorizontalHeaderLabels(self.upload_file.columns)

        for rows in range(RowNumber):
            for columns in range(ColumnNumber):
                self.table_widget.setItem(rows, columns, QTableWidgetItem(str(self.upload_file.iat[rows, columns])))
        
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
    
    # define method for return button:
    def Come_Back(self):
        from Second_page import BatMan
        file_name = self.secret_label_3.text()
        self.window2 = QMainWindow()
        self.boy = BatMan()
        self.boy.secret_label_2.setText(f"{file_name}")
        self.close()


# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    water = AquaMan()
    sys.exit(app.exec_())