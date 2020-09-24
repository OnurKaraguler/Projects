import sys
from PyQt5.QtWidgets import QApplication
from OK_Functions import Functions

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Functions()
    app.exit(app.exec_())
