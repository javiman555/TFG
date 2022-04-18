from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf

class PlotController:
    def __init__(self):
        self.plotType = "altair"
        self.plot = AltairPlot.AltairPlot()
    
    def getPlot(self):
        waves = self.getWaves()
        chart = self.plot.getPlot(waves)
        output = StringIO()
        chart.save(output, "html")
        return output
    
    def getWaves(self):
        yf1=yf.YahooFinanceAPI(debug=True) 
        
        waves =[]

        
        for element in yf1.stocks:
            
            complexWave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            complexWave.normalice()
            waves.append(complexWave)
        return waves