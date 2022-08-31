import paraview.simple as pvsimple
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

def getParaViewWidget():
    # setup render widget
    render_view = pvsimple.CreateRenderView()
    render_widget = QVTKRenderWindowInteractor(rw=render_view.GetRenderWindow(),
                                               iren=render_view.GetInteractor())
    render_widget.Initialize()

    # add paraview simple sources/filters
    sphere = pvsimple.Sphere(ThetaResolution=16, PhiResolution=32)
    shrink = pvsimple.Shrink(sphere)
    pvsimple.Show(shrink, render_view)
    return render_widget
