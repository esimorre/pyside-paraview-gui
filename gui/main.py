import sys, os

sys.path.append(
os.path.join(os.path.dirname(__file__), 'ParaView-5.10.1','bin','Lib','site-packages')
)

import paraview.simple as pvsimple
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])

# setup render widget
render_view = pvsimple.CreateRenderView()
render_widget = QVTKRenderWindowInteractor(rw=render_view.GetRenderWindow(),
                                           iren=render_view.GetInteractor())
render_widget.Initialize()

# add paraview simple sources/filters
sphere = pvsimple.Sphere(ThetaResolution=16, PhiResolution=32)
shrink = pvsimple.Shrink(sphere)
pvsimple.Show(shrink, render_view)

# show widget
#render_widget.show()


window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
layout.addWidget(render_widget)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())