from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults


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
        valueResults = ValueResults.ValueResults(debug=True)
        inputWaves = valueResults.inputStocks
        
        waves = valueResults.inputStocksByGraph
        
        
        realwaves = valueResults.actualizedStocks
        
        k= len(realwaves)//3
        [valueListGD,valueListGDP] = valueResults.valueProcess(k,inputWaves,inputWaves,realwaves,0)        
        
        [valueListC,valueListCP] = valueResults.valueProcess(k,inputWaves,inputWaves,realwaves,1)        
        
        [valueListCV,valueListCVP] = valueResults.valueProcess(k,inputWaves,inputWaves,realwaves,2)        

        
        waves =[valueListGD,valueListGDP,valueListC,valueListCP,valueListCV,valueListCVP]


        return waves