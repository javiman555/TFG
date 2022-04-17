#To modify layout $ designer
# $ cd Documents/GitHub/TFG/src/view
#To save changes $ python -m PyQt5.uic.pyuic -x QtApp.ui -o QtApp_ui.py


from QtApp_ui import *
from pyqtgraph import PlotWidget, plot
from src.controller.plot import PlotController

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.label.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)
        
        plotController = PlotController.PlotController()
        
        output = plotController.getPlot()
        self.webEngineView.setHtml(output.getvalue())
        '''
        HtmlFile = open("filename.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        self.webEngineView.setHtml(source_code)
        '''
        
        self.graphWidget.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
