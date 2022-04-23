#To modify layout $ designer
# $ cd Documents/GitHub/TFG/src/view
#To save changes $ python -m PyQt5.uic.pyuic -x QtApp.ui -o QtApp_ui.py


from QtApp_ui import *
from pyqtgraph import PlotWidget, plot
from src.controller.plot import PlotController
from src.controller.input import InputController
from src.controller.execution import ExecutionController

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    #Controllers
    inputController = InputController.InputController()
    executionController = ExecutionController.ExecutionController()
    plotController = PlotController.PlotController()

    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        stockSource = str(self.comboBox_source.currentText())
        
        tickerList = self.inputController.getStockNamesFromSource(stockSource)
        self.listWidget_stock.addItems(tickerList)
        self.listWidget_stock.selectAll()
        # Conectamos los eventos con sus acciones
        self.startButton.clicked.connect(self.execute)
        
        
    def execute(self):
        
        #Get the current inputs
        dateStart = self.inputController.getDate(self.dateEdit_startDate)
        dateEnd = self.inputController.getDate(self.dateEdit_endDate)
        tickerList = self.inputController.getStockNamesFromListWidget(self.listWidget_stock)
        money = self.inputController.getMoney(self.plainTextEdit_money)
        
        #Chose execution
        if self.radioButton_fast.isChecked():
            result = self.executionController.executeFast(tickerList,dateStart,dateEnd,money)
        elif self.radioButton_standar.isChecked():
            result = self.executionController.executeStandar(tickerList,dateStart,dateEnd,money)
        elif self.radioButton_slow.isChecked():
            result = self.executionController.executeSlow(tickerList,dateStart,dateEnd,money)
        
        #Recover the results
        plot = self.plotController.getPlot(result,dateEnd)
        self.chartView.setHtml(plot.getvalue())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

