from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout
from PyQt5 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from Third_page import AquaMan

class BatMan(QMainWindow):
    def __init__(self):
        super(BatMan, self).__init__()

        uic.loadUi("TWO.ui", self)

        # define content:
        self.data_label = self.findChild(QLabel, "data_label")
        self.chart_label = self.findChild(QLabel, "chart_label")
        self.x_label = self.findChild(QLabel, "x_label")
        self.y_label = self.findChild(QLabel, "y_label")
        self.color_label = self.findChild(QLabel, "color_label")
        self.info_label = self.findChild(QLabel, "info_label")
        self.secret_label_2 = self.findChild(QLabel, "secret_label_2")
        self.x_rename = self.findChild(QLabel, "x_rename")
        self.y_rename = self.findChild(QLabel, "y_rename")
        self.title_label = self.findChild(QLabel, "title_label")
        self.size_label = self.findChild(QLabel, "size_label")

        self.check_button = self.findChild(QPushButton, "check_button")
        self.back_button = self.findChild(QPushButton, "back_button")
        self.exit_button = self.findChild(QPushButton, "exit_button")
        self.display_button = self.findChild(QPushButton, "display_button")

        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.Down_frame = self.findChild(QFrame, "Down_frame")
        self.Up_frame = self.findChild(QFrame, "Up_frame")

        self.box_1 = self.findChild(QComboBox, "box_1")
        self.box_2 = self.findChild(QComboBox, "box_2")
        self.box_4 = self.findChild(QComboBox, "box_4")

        self.x_line = self.findChild(QLineEdit, "x_line")
        self.y_line = self.findChild(QLineEdit, "y_line")
        self.x_rename_line = self.findChild(QLineEdit, "x_rename_line")
        self.y_rename_line = self.findChild(QLineEdit, "y_rename_line")
        self.title_line = self.findChild(QLineEdit, "title_line")

        # define layout:
        self.First_Layout = QHBoxLayout(self.Up_frame)
        self.First_Layout.setObjectName("First_Layout")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.First_Layout.addWidget(self.diagramm)

        # call defined method from here:
        self.exit_button.clicked.connect(lambda: self.close())
        self.back_button.clicked.connect(self.Return_Back)
        self.check_button.clicked.connect(self.Check_File)
        self.display_button.clicked.connect(self.plotOnCanvas)

        self.show()

# ---------------------------------------- logic -------------------------------------- #
    # define clean method:
    def Clean_written(self):
        self.title_line.setText("")
        self.x_line.setText("")
        self.y_line.setText("")
        self.x_rename_line.setText("")
        self.y_rename_line.setText("")

    # define background color:
    def Red_Color(self):
        self.info_label.setStyleSheet("background-color: rgb(255, 80, 83);")

    # define method for back button:
    def Return_Back(self):
        from First_page import SpiderMan
        self.window1 = QMainWindow()
        self.man = SpiderMan()
        self.close()
    
    # define method for check button:
    def Check_File(self):
        file_name = self.secret_label_2.text()
        self.window3 = QMainWindow()
        self.water = AquaMan()
        self.water.secret_label_3.setText(f"{file_name}")
        self.close()
    
    # define method for display button:
    def plotOnCanvas(self):
        # variables:
        chart = self.box_1.currentText()
        chart_title = self.title_line.text()
        x_column = self.x_line.text()
        y_column = self.y_line.text()
        x_name = self.x_rename_line.text()
        y_name = self.y_rename_line.text()
        color_type = self.box_2.currentText()
        bar_size = self.box_4.currentText()
        # clear diagramm and read file:
        self.figure.clear()
        file_name = self.secret_label_2.text()
        df = pd.read_csv(f"{file_name}")
        # draw diagram:
        if chart == "scatter":
            if x_column in df.columns and y_column in df.columns:
                plt.scatter(df[f"{x_column}"], df[f"{y_column}"], color = f"{color_type}")
                plt.xlabel(f"{x_name}")
                plt.ylabel(f"{y_name}")
                plt.title(f"{chart_title}")
                plt.grid()
                plt.colorbar()
                self.diagramm.draw()
                self.Clean_written()
            else:
                self.info_label.setText("Column Names are not defined correctly, change it!")
                self.Red_Color()
        
        if chart == 'histogram':
            if x_column in df.columns and len(y_column) == 0:
                plt.hist(df[f"{x_column}"], color=f"{color_type}")
                plt.xlabel(f"{x_name}")
                plt.ylabel(f"{y_name}")
                plt.title(f"{chart_title}")
                plt.grid()
                self.diagramm.draw()
                self.Clean_written()
            else:
                self.info_label.setText("Parameters are not defined correctly, histogram needs only one column - xlabel!")
                self.Red_Color()
        
        if chart == "pie":
            if x_column in df.columns and len(y_column) == 0:
                if df[f"{x_column}"].dtype == 'int64' or df[f"{x_column}"].dtype == 'float64':
                    
                    check_point = list(df[f"{x_column}"].notnull())
                    if False in check_point:   
                        df[f"{x_column}"].fillna(1, inplace=True)
                        df.to_csv(f"{file_name}", index=False)

                    Arr = df[f"{x_column}"]
                    Par = np.array([])
                    my_legend = np.array([])
                    for i in Arr:
                        if i in Par:
                            pass
                        else:
                            my_legend = np.append(my_legend, [str(i)])
                            Par = np.append(Par, [i])
                            
                    plt.pie(Par, labels = my_legend, startangle=90, shadow=True)
                    plt.title(f"{chart_title}")
                    plt.legend(title = "Legend")
                    self.diagramm.draw()
                else:
                    self.info_label.setText("Column data type should be int or float!")
                    self.Red_Color()
            else:
                self.info_label.setText("Parameters are not defined correctly, pie needs only one column - xlabel!")
                self.Red_Color()
            
        if chart == "bar":
            if x_column in df.columns and y_column in df.columns:
                plt.bar(df[f"{x_column}"], df[f"{y_column}"], width=float(bar_size), color = f"{color_type}")
                plt.xlabel(f"{x_name}")
                plt.ylabel(f"{y_name}")
                plt.title(f"{chart_title}")
                plt.grid()
                self.diagramm.draw()
            else:
                self.info_label.setText("Column Names are not defined correctly, change it!")
                self.Red_Color()
        
        if chart == "barh":
            if x_column in df.columns and y_column in df.columns:
                plt.barh(df[f"{x_column}"], df[f"{y_column}"], height=float(bar_size), color = f"{color_type}")
                plt.xlabel(f"{y_name}")
                plt.ylabel(f"{x_name}")
                plt.title(f"{chart_title}")
                plt.grid()
                self.diagramm.draw()
                self.Clean_written()
            else:
                self.info_label.setText("Column Names are not defined correctly, change it!")
                self.Red_Color()
        
# ------------------------------------------ end -------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    boy = BatMan()
    sys.exit(app.exec_())