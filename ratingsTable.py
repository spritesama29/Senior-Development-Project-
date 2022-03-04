from PySide6.QtWidgets import QWidget, \
    QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout



import main
import windowsData
import tvTable

class ratingsTable(QWidget):
    def __init__(self):
        super().__init__()

        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):

        self.setWindowTitle("tvTable")
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.getUserRatings(tvTable.id)


        self.setGeometry(300, 100, 400, 500)
        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumWidth(500)
        self.tableWidget.setMinimumHeight(500)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(23)
        self.tableWidget.setHorizontalHeaderLabels(["1","2","3","4"])
        for i in range(100):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(tv[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(tv[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(tv[i][2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(tv[i][3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(tv[i][4]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(tv[i][5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(tv[i][6]))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(tv[i][7]))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(tv[i][8]))

        #self.show()
        self.tableWidget.show()
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.currentItemChanged.connect(self.yeet)

    def yeet(self):
        message_box = QMessageBox(self)
        ratings = main.getUserRatings(self.tableWidget.currentItem().text())
        ratingsStr = ""
        for i in range(10):
            ratingsStr += ratings.get("ratings")[i].get('rating') + ratings.get("ratings")[i].get('percent')  + ratings.get("ratings")[i].get('votes') + "\n"


        message_box.setText(ratingsStr)
        message_box.setWindowTitle("Comp490 Demo")
        message_box.show()