from PySide6.QtWidgets import QWidget, \
    QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout



import main
import windowsData


class movieWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):

        self.setWindowTitle("tvTable")

        self.setGeometry(200, 100, 400, 500)
        movRanking = QPushButton("Make a popular table ordered by ranking", self)
        movRanking.move(50, 100)
        movRankUpDown = QPushButton("Make a popular table ordered by how much their popularity\n"
                                    " fluctuates", self)
        movRankUpDown.move(50, 200)
        quit_button = QPushButton("Go back", self)
        quit_button.clicked.connect(self.hide)
        quit_button.move(50, 300)
        self.show()
        movRanking.clicked.connect(self.movMakerRanking)
        movRankUpDown.clicked.connect(self.movMakerRankDown)

    def ratingsDisplay(self):
        message_box = QMessageBox(self)
        ratings = main.getUserRatings(self.tableWidget.currentItem().text())
        ratingsStr = ""
        ratingsStr += 'Total ratings: %s \n\n' % (ratings.get("totalRatingVotes"))
        for i in range(10):
            ratingsStr += 'rating: %s Percent: %s Votes: %s \n\n' % (ratings.get("ratings")[i].get('rating'),ratings.get("ratings")[i].get('percent'),ratings.get("ratings")[i].get('votes'))

        message_box.setText(ratingsStr)
        message_box.setWindowTitle("Movie Window")
        message_box.show()

    def movMakerRankDown(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.orderBy(self.cursor,"mov")
        self.TableTime(tv)

    def movMakerRanking(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.rankBy(self.cursor,"mov")
        self.TableTime(tv)

    def TableTime(self,tv):
        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumWidth(500)
        self.tableWidget.setMinimumHeight(500)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ranking", "RankUpDown", "Title",
                                                    "fullTitle", "year", "crew", "rating", "total votes"])
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
        self.tableWidget.show()
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.currentItemChanged.connect(self.ratingsDisplay)
