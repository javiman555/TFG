#To modify layout designer
#cd Documents/GitHub/TFG/src
#To save changes python -m PyQt5.uic.pyuic -x QtApp.ui -o QtApp_ui.py


from QtApp_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.label.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)
        HtmlFile = open("filename.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        self.webEngineView.setHtml(source_code)



    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
