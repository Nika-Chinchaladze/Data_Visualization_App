from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import uic
import pandas as pd
from Second_page import BatMan

class SpiderMan(QMainWindow):
    def __init__(self):
        super(SpiderMan, self).__init__()

        uic.loadUi("ONE.ui", self)

        # define content:
        self.welcome_label = self.findChild(QLabel, "welcome_label")
        self.picture_label = self.findChild(QLabel, "picture_label")
        self.secret_label_1 = self.findChild(QLabel, "secret_label_1")
        self.file_label = self.findChild(QLabel, "file_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        self.upload_button = self.findChild(QPushButton, "upload_button")
        self.go_button = self.findChild(QPushButton, "go_button")
        self.filename = self.findChild(QLineEdit, "filename")

        # call defined method from here:
        self.go_button.setEnabled(False)
        self.upload_button.clicked.connect(self.Upload_method)
        self.go_button.clicked.connect(self.Continue_action)

        self.show()
# ----------------------------------------- logic ------------------------------------- #

    # define method for upload button:
    def Upload_method(self):
        name = self.filename.text() + ".csv"
        try:
            self.file = pd.read_csv(f"{name}")
            self.answer_label.setText(f"{name} has been uploaded Successfully, press Continue!")
            self.answer_label.setStyleSheet("background-color: rgb(170, 255, 127);")
            self.go_button.setEnabled(True)
            self.filename.setText("")
            self.secret_label_1.setText(f"{name}")
        except FileNotFoundError:
            self.answer_label.setText(f"{name} does not Exists in the Directory!")
            self.answer_label.setStyleSheet("background-color: rgb(255, 80, 83);")
    
    # define method for go button:
    def Continue_action(self):
        file_name = self.secret_label_1.text()
        self.window2 = QMainWindow()
        self.boy = BatMan()
        self.boy.secret_label_2.setText(f"{file_name}")
        self.close()




# ------------------------------------------ end -------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    man = SpiderMan()
    sys.exit(app.exec_())