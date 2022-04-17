from src.controller.plot import AltairPlot
from io import StringIO


class PlotController:
    def __init__(self):
        self.plotType = "altair"
        self.plot = AltairPlot.AltairPlot()
    
    def getPlot(self):
        chart = self.plot.getPlot()
        output = StringIO()
        chart.save(output, "html")
        return output
    