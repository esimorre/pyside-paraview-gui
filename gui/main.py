import sys, os

sys.path.append(
    os.path.join(os.path.dirname(__file__),
    'ParaView-5.10.1','bin','Lib','site-packages')
)
sys.path.append(
    os.path.join(os.path.dirname(__file__),
    'dockwidgets')
)

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QDockWidget
from dockwidgets import MainWindow
from stylewidget import StyleWidget
from pvwidget import getParaViewWidget

class MyWindow(MainWindow):


    def createToolBars(self):
        super().createToolBars()
        self.addToolBar("Style").addWidget(StyleWidget())

    def createDockWindows(self):
        super().createDockWindows()
        dock = QDockWidget("Paraview", self)
        dock.hide()
        dock.setWidget(getParaViewWidget())
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWin = MyWindow()
    mainWin.show()
    sys.exit(app.exec_())
