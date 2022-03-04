from PySide6.QtWidgets import QWidget, \
    QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QTableWidget, QTableWidgetItem

import main
import windowsData


class tvTable(QWidget):
    def __init__(self):
        super().__init__()

        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):

        self.setWindowTitle("tvTable")

        self.setGeometry(200, 100, 400, 500)
        tvRanking = QPushButton("Make a popular table ordered by ranking", self)
        tvRanking.move(50, 100)
        tvRankUpDown = QPushButton("Make a popular table ordered by how much their popularity \n fluctuates", self)
        tvRankUpDown.move(50, 200)
        tv250Table = QPushButton("Make a table showing the top 250 TV Shows!",self)
        tv250Table.move(50,300)
        quit_button = QPushButton("Go back", self)
        quit_button.clicked.connect(self.hide)
        quit_button.move(50, 400)
        self.show()
        tvRanking.clicked.connect(self.tvTableTimeRanking)
        tvRankUpDown.clicked.connect(self.tvTableTimeUpDown)
        tv250Table.clicked.connect(self.tv250)


        #self.show()


    def ratingsDisplay(self):
        message_box = QMessageBox(self)
        ratings = main.getUserRatings(self.tableWidget.currentItem().text())
        ratingsStr = ""
        ratingsStr += 'Total ratings: %s \n\n' % (ratings.get("totalRatingVotes"))
        for i in range(10):
            ratingsStr += 'rating: %s Percent: %s Votes: %s \n\n' % (ratings.get("ratings")[i].get('rating'),ratings.get("ratings")[i].get('percent'),ratings.get("ratings")[i].get('votes'))

        message_box.setText(ratingsStr)
        message_box.setWindowTitle("TV Window")
        message_box.show()


    def tvTableTimeUpDown(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.orderBy(self.cursor,"tv")
        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumWidth(500)
        self.tableWidget.setMinimumHeight(500)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ranking", "RankUpDown", "Title","fullTitle","year","crew","rating","total votes"])
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

    def tvTableTimeRanking(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.rankBy(self.cursor,"tv")
        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumWidth(500)
        self.tableWidget.setMinimumHeight(500)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ranking", "RankUpDown", "Title","fullTitle","year","crew","rating","total votes"])
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

    def tv250(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.get250nice(self.cursor)
        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumWidth(700)
        self.tableWidget.setMinimumHeight(700)
        self.tableWidget.setRowCount(250)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ranking", "Title","fullTitle","year","crew","rating","ratingCount"])
        for i in range(250):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(tv[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(tv[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(tv[i][2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(tv[i][3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(tv[i][4]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(tv[i][5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(tv[i][6]))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(tv[i][7]))

        self.tableWidget.show()
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.currentItemChanged.connect(self.ratingsDisplay)

