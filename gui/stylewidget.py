from PySide2.QtWidgets import QApplication, QStyleFactory, QComboBox, QWidget, QLabel, QHBoxLayout


def style_names():
    """Return a list of styles, default platform style first"""
    default_style_name = QApplication.style().objectName().lower()
    result = []
    for style in QStyleFactory.keys():
        if style.lower() == default_style_name:
            result.insert(0, style)
        else:
            result.append(style)
    return result

class StyleWidget(QWidget):
    def __init__(self):
        super(StyleWidget, self).__init__()
        self._style_combobox = QComboBox()
        self._style_combobox.addItems(style_names())
        style_label = QLabel("Style:")
        style_label.setBuddy(self._style_combobox)
        layout = QHBoxLayout()
        layout.addWidget(style_label)
        layout.addWidget(self._style_combobox)
        self.setLayout(layout)
        self._style_combobox.textActivated.connect(self.change_style)

    def change_style(self, style_name):
        QApplication.setStyle(QStyleFactory.create(style_name))
