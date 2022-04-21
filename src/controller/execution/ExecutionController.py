from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults


class ExecutionController:
    
    def __init__(self):
        self.proccess = ValueResults.ValueResults()
    
    def executeFast(self,tickerList,dateStart,dateEnd,money):
        return self.proccess.executeFast(tickerList,dateStart,dateEnd,money)
    def executeStandar(self):
        pass
    def executeSlow(self):
        pass
    
    
            