#To modify layout designer
#cd Documents/GitHub/TFG/src
#To save changes python -m PyQt5.uic.pyuic -x QtApp.ui -o QtApp_ui.py


from QtApp_ui import *
from pyqtgraph import PlotWidget, plot
from AltairWebView import WebEngineView
import altair as alt
from vega_datasets import data
from io import StringIO
import pandas as pd
from pandas_datareader import data

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.label.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)
        
        start = '2020-1-1'
        end = '2020-12-31'
        source = 'yahoo'
        apple = data.DataReader("AAPL", start=start ,end=end, data_source=source).reset_index()[["Date", "Close"]]
        ibm = data.DataReader("IBM", start=start ,end=end, data_source=source).reset_index()[["Date", "Close"]]
        microsoft = data.DataReader("MSFT", start=start ,end=end, data_source=source).reset_index()[["Date", "Close"]]
        apple["Stock"] = "apple"
        ibm["Stock"] = "ibm"
        microsoft["Stock"] = "msft"
        
        stocks = pd.concat([apple, ibm, microsoft])
        stocks["Month"] = stocks.Date.dt.month
        selection = alt.selection_multi(fields=["Stock"], bind="legend")
        chart = alt.Chart(stocks).mark_line().encode(
           x="Date",
           y="Close",
           color="Stock",
           opacity=alt.condition(selection, alt.value(1), alt.value(0.1))
        ).properties(
           height=300, width=500
        ).add_selection(
           selection
        )
        
        output = StringIO()
        chart.save(output, "html")
        self.webEngineView.setHtml(output.getvalue())
        '''
        HtmlFile = open("filename.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        self.webEngineView.setHtml(source_code)
        '''
        
        self.graphWidget.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
