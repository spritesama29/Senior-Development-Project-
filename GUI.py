
import PySide6.QtWidgets
import sys
import windows


def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    windows.guiWindow()
    sys.exit(qt_app.exec())


def main():

    wa = 0
    display_data(wa)


if __name__ == '__main__':
    main()
