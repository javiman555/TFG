from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults


class InputController:
    def __init__(self):
        self.API =yf.YahooFinanceAPI(debug=False) 
    
    def getStockNamesFromSource(self,source):
        return self.API.stocks
    
    def getStockNamesFromListWidget(self,listWidget):
        tickerList = []
        for x in range(listWidget.count()-1):
            if listWidget.item(x).isSelected():
                tickerList.append(listWidget.item(x).text())
        return tickerList
    
    def getDate(self,dateEdit):
        return dateEdit.date().toString("yyyy-MM-dd")
    
    def getMoney(self,plainTextEdit):
        try:
            money = int(plainTextEdit.toPlainText())
        except TypeError:
            print("Only integers are allowed, using default value 1000")
            money = 1000
        return money
    
    def getNumberStocks(self,plainTextEdit):
        try:
            k = int(plainTextEdit.toPlainText())
        except TypeError:
            print("Only integers are allowed, using default value 4")
            k = 4
        return k
    
            