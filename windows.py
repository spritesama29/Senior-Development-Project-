from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox

import main
import windowsData

class guiWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("Epic Database")
        #display_list = QListWidget(self)
        #self.list_control = display_list
       # self.put_data_in_list(self.data)

        self.setGeometry(300, 100, 400, 500)
        updateButton = QPushButton("Update data", self)
        updateButton.move(125, 200)
        dataVisualization = QPushButton("data Visualization", self)
        dataVisualization.move(125, 300)

        updateButton.clicked.connect(self.updateData)
        dataVisualization.clicked.connect(self.dataMenu)
        self.show()

    #def put_data_in_list(self, data: list[dict]):
      # for item in data:
        #   display_text = f"{item['state_name']}\t\t{item['median_income']}"
          #  list_item = QListWidgetItem(display_text, listview=self.list_control)

    def updateData(self):
        message_box = QMessageBox(self)
        message_box.setText("Data sucessfully updated")
        main.main()
        message_box.setWindowTitle("Update Data")
        message_box.show()

    def dataMenu(self):
        self.conn, self.cursor = main.open_db("demo_db.sqlite")
        try:
            main.orderBy(self.cursor,"tv")
            self.windows = windowsData.dataWindow()
            self.windows.show()
        except:
            messageBox=QMessageBox(self)
            messageBox.setText("Seems like there is no data! \n Have you tried pressing the update data Button?")
            messageBox.show()