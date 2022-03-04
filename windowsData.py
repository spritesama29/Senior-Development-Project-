from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox
import pyqtgraph as pg

import main
import tvTable

import windowsData
import movieWindow


class dataWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("Data window")
        # display_list = QListWidget(self)
        # self.list_control = display_list
        # self.put_data_in_list(self.data)

        self.setGeometry(300, 200, 500, 500)
        tvButton = QPushButton("I'd like to see TV information", self)
        tvButton.move(50, 25)
        movieButton = QPushButton("I'd like to see Movie information", self)
        movieButton.move(50, 125)
        graphButton = QPushButton("I'd like to see a graph comparing TV and Movie rankUpDowns", self)
        graphButton.move(50, 225)
        tvMerge = QPushButton("I'd like to see how many shows are in both popularTV and the top 250 shows",self)
        tvMerge.move(25, 325)
        movieMerge = QPushButton("I'd like to see how many movies are both in popularMovies and the top 250 "
                                 "movies", self)
        movieMerge.move(25,425)
        tvMerge.clicked.connect(self.tvMerge)
        movieMerge.clicked.connect(self.movMerge)
        tvButton.clicked.connect(self.tvTime)
        movieButton.clicked.connect(self.movieTime)
        graphButton.clicked.connect(self.graph)
        self.show()

    def tvMerge(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.getTVjoin(self.cursor)
        tvString = ""
        for tvNum in range(len(tv)):
            tvString+='ImDbId: %s   Title: %s \n' % (tv[tvNum][0],tv[tvNum][1])
        messageBox = QMessageBox(self)
        messageBox.setText(tvString)
        messageBox.setMinimumWidth(400)
        messageBox.setWindowTitle("Relatable tv titles")
        messageBox.show()

    def movMerge(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        mov = main.getMOVjoin(self.cursor)
        tvString = ""
        for tvNum in range(len(mov)):
            tvString+='ImDbId: %s   Title: %s \n' % (mov[tvNum][0],mov[tvNum][1])
        messageBox = QMessageBox(self)
        messageBox.setText(tvString)
        messageBox.setMinimumWidth(400)
        messageBox.setWindowTitle("Relatable tv titles")
        messageBox.show()


    def tvTime(self):
        self.tvWindows = tvTable.tvTable()

    def movieTime(self):
        self.movieWindows = movieWindow.movieWindow()

    def graph(self):
        self.graphWidget = pg.PlotWidget()
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        tv = main.orderByASCTV(self.cursor)
        mov = main.orderByASCMOV(self.cursor)

        posTV = main.posAndNegSort(tv, mov, "posTV")
        negTV = main.posAndNegSort(tv, mov, "negTV")
        posMOV = main.posAndNegSort(tv, mov, "posMOV")
        negMOV = main.posAndNegSort(tv, mov, "negMOV")

        posTVAxis = main.getGraphCoords(self.cursor, posTV, mov, "posTVAxis")
        negTVAxis = main.getGraphCoords(self.cursor, negTV, mov, "negTVAxis")
        posMOVAxis = main.getGraphCoords(self.cursor, posTV, posMOV, "posMOVAxis")
        negMOVAxis = main.getGraphCoords(self.cursor, tv, negMOV, "negMOVAxis")
        posTVlen = main.getGraphCoords(self.cursor, posTV, posTV, "posTVlen")
        negTVlen = main.getGraphCoords(self.cursor, negTV, negTV, "negTVlen")
        posMOVlen = main.getGraphCoords(self.cursor, posTV, posMOV, "posMOVlen")
        negMOVlen = main.getGraphCoords(self.cursor, tv, negMOV, "negMOVlen")
        pen = pg.mkPen(color=(255, 0, 0))
        bluePen = pg.mkPen(color=(0, 255, 0))
        self.graphWidget.plot(posTVAxis, posTVlen, pen=pen)
        self.graphWidget.plot(negTVAxis, negTVlen, bluePen=bluePen)
        self.graphWidget.plot(posMOVAxis, posMOVlen, pen=pen)
        self.graphWidget.plot(negMOVAxis, negMOVlen, bluePen=bluePen)
        self.graphWidget.setLabel("left", "Number of tv shows/movies")
        self.graphWidget.setLabel("bottom", "TV Shows(went up)--------------TV Shows(went down)----------Movies(going "
                                            "up)----------Movies(going down)")
        self.graphWidget.setLabel("top", "Red lines = Going up-------------------White lines = Going down")
        self.graphWidget.show()
