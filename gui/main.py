import sys, os

sys.path.append(
    os.path.join(os.path.dirname(__file__),
    'ParaView-5.10.1','bin','Lib','site-packages')
)

from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
