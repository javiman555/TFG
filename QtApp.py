#To modify layout $ designer
# $ cd Documents/GitHub/TFG/src/view
#To save changes $ python -m PyQt5.uic.pyuic -x QtApp.ui -o QtApp_ui.py


from src.view.QtApp_ui import *
from pyqtgraph import PlotWidget, plot
from src.controller.plot import PlotController
from src.controller.input import InputController
from src.controller.execution import ExecutionController
from PyQt5.QtWidgets import QMessageBox

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
        self.updateStocks()
        
    def updateStocks(self):
        try:
            print('outdated for stats 29/5/2022')
            #self.executionController.saveStoks()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Warning")
            msg.setInformativeText('The stock info migth be outdated but you can still use the app')
            msg.setWindowTitle("Warning")
            msg.exec_()
        
    def execute(self):
        
        #Get the current inputs
        dateStart = self.inputController.getDate(self.dateEdit_startDate)
        dateEnd = self.inputController.getDate(self.dateEdit_endDate)
        tickerList = self.inputController.getStockNamesFromListWidget(self.listWidget_stock)
        money = self.inputController.getMoney(self.plainTextEdit_money)
        k = self.inputController.getNumberStocks(self.plainTextEdit_k)
        
        #Chose execution
        if self.radioButton_fast.isChecked():
            [resultA,result] = self.executionController.executeFast(tickerList,dateStart,dateEnd,money,k)
        elif self.radioButton_standar.isChecked():
            [resultA,result] = self.executionController.executeStandar(tickerList,dateStart,dateEnd,money,k)
        elif self.radioButton_slow.isChecked():
            [resultA,result] = self.executionController.executeSlow(tickerList,dateStart,dateEnd,money,k)
        
        #Recover the results
        plot = self.plotController.getPlot(result,dateEnd)
        self.chartView.setHtml(plot.getvalue())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

