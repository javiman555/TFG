from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults


class PlotController:
    def __init__(self):
        self.plotType = "altair"
        self.plot = AltairPlot.AltairPlot()
    
    def getPlot(self,result):
        waves = self.getWaves(result)
        chart = self.plot.getPlot(waves)
        output = StringIO()
        chart.save(output, "html")
        return output
    
    def getWaves(self,result):
        return result