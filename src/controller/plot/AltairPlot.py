import altair as alt
from pandas_datareader import data
import pandas as pd

class AltairPlot:
    def __init__(self):
        pass
    
    def getPlot(self):
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
        return chart
    