from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults
import src.model.modules.Wavelete as Wavelete

class ExecutionController:
    
    def __init__(self):
        self.proccess = ValueResults.ValueResults()
        self.wavelete = Wavelete.Wavelete()
    
    def executeFast(self,tickerList,dateStart,dateEnd,money):
        
        inputWaves = self.proccess.createWave(tickerList,dateStart,dateEnd,debug=False)
        
        realwaves = self.proccess.createRealWave(tickerList,dateStart,debug=False)
        
        simplifiedInputWaves = self.wavelete.simplificationComplexWaveList(inputWaves)
        simplifiedInputWaves = self.wavelete.simplificationComplexWaveList(simplifiedInputWaves)
        simplifiedInputWaves = self.wavelete.simplificationComplexWaveList(simplifiedInputWaves)

        return self.proccess.executeStandar(simplifiedInputWaves,realwaves,money)
    
    def executeStandar(self,tickerList,dateStart,dateEnd,money):
        inputWaves = self.proccess.createWave(tickerList,dateStart,dateEnd,debug=False)
        
        realwaves = self.proccess.createRealWave(tickerList,dateStart,debug=False)
        
        return self.proccess.executeStandar(inputWaves,realwaves,money)
    
    def executeSlow(self,tickerList,dateStart,dateEnd,money):
        inputWaves = self.proccess.createWave(tickerList,dateStart,dateEnd,debug=False)
        
        waves = self.proccess.createWaveGraph(tickerList,debug=False)
        
        realwaves = self.proccess.createRealWave(tickerList,dateStart,debug=False)
        
        return self.proccess.executeFull(inputWaves,waves,realwaves,money)
        
        
    
    
            