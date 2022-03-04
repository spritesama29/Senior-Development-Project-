import openpyxl
import PySide6.QtWidgets
import sys
import windows
import numbers



def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = windows.guiWindow()
    sys.exit(qt_app.exec())
def main():
   # test_data = get_test_data()
    #test_data.sort(key=get_key)
    wa = 0
    display_data(wa)


if __name__ == '__main__':
    main()
