from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout
from pvwidget import getParaViewWidget

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton('Top'))
        layout.addWidget(QPushButton('Bottom'))
        layout.addWidget(getParaViewWidget())
        self.setLayout(layout)
