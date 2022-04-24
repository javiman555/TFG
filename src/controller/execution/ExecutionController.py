from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults
import src.model.modules.Wavelete as Wavelete
import src.model.modules.YahooFinanceAPI as yf
from config.definitions import TODAY_DATE

class ExecutionController:
    
    def __init__(self):
        self.proccess = ValueResults.ValueResults()
        self.wavelete = Wavelete.Wavelete()
    
    def saveStoks(self):
        yf1=yf.YahooFinanceAPI(debug=False)
        yf1.saveStocksStartEnd('2000-01-01',TODAY_DATE,'1d',True,'DataStocks.csv')
        
    
    def executeFast(self,tickerList,dateStart,dateEnd,money):
        
        inputWaves = self.proccess.createWave(dateStart,dateEnd,tickerList,debug=False)
        
        realwaves = self.proccess.createWave(dateStart,TODAY_DATE,tickerList,debug=False)
        
        simplifiedInputWaves = self.wavelete.simplificationComplexWaveList(inputWaves)
        simplifiedInputWaves = self.wavelete.simplificationComplexWaveList(simplifiedInputWaves)
        simplifiedInputWaves = self.wavelete.simplificationComplexWaveList(simplifiedInputWaves)

        return self.proccess.executeStandar(simplifiedInputWaves,realwaves,money)
    
    def executeStandar(self,tickerList,dateStart,dateEnd,money):
        inputWaves = self.proccess.createWave(dateStart,dateEnd,tickerList,debug=False)
        
        realwaves = self.proccess.createWave(dateStart,TODAY_DATE,tickerList,debug=False)
        
        return self.proccess.executeStandar(inputWaves,realwaves,money)
    
    def executeSlow(self,tickerList,dateStart,dateEnd,money):
        inputWaves = self.proccess.createWave(dateStart,dateEnd,tickerList,debug=False)
                
        waves = self.proccess.createWaveGraph(dateStart,dateEnd,tickerList,debug=False)
        
        realwaves = self.proccess.createWave(dateStart,TODAY_DATE,tickerList,debug=False)
        
        return self.proccess.executeFull(inputWaves,waves,realwaves,money)
        
        
    
    
            