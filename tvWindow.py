from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox

import main
import windowsData
import tvTable
import movieWindow


class tvWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("Epic Database")
        # display_list = QListWidget(self)
        # self.list_control = display_list
        # self.put_data_in_list(self.data)

        self.setGeometry(300, 100, 400, 500)
        tvButton = QPushButton("tv visuals", self)
        tvButton.move(25, 400)
        movieButton = QPushButton("movie visuals", self)
        movieButton.move(125, 400)
        tvButton.clicked.connect(self.tvMenu)
        movieButton.clicked.connect(self.MovieMenu)
        self.show()

    # def put_data_in_list(self, data: list[dict]):
    # for item in data:
    #   display_text = f"{item['state_name']}\t\t{item['median_income']}"
    #  list_item = QListWidgetItem(display_text, listview=self.list_control)

    def tvMenu(self):
        self.tvTable = tvTable.tvTable()

    def MovieMenu(self):
        conn, cursor = main.open_db("demo_db.sqlite")
        tv = main.orderBy(cursor)
        print(tv)