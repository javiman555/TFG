# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:28:55 2022

@author: Javier
"""

from tkinter import *
from tkinter import messagebox
from tkinterhtml import HtmlFrame
import altair as alt
import pandas as pd
from pandas_datareader import data
import urllib

def start():
    response = messagebox.askokcancel("Aproximated wait time","It seems the proccess could take up to infinity seconds. Continue?")
    if response == 1:
        #We call the proccess
        pass
  
alt.renderers.enable('altair_viewer')

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
chart.save('filename.html')
HtmlFile = open("filename.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
  
root = Tk()
root.title("App")
root.resizable(False,False)
root.iconbitmap('../resources/App.ico')

inputframe = LabelFrame(root,text="Input")
inputframe.grid(column=0, row=0,rowspan=10, sticky=(N, W, E, S))

graphframe = LabelFrame(root,text="Graph")
graphframe.grid(column=1,row=0,columnspan=6,rowspan=4, sticky=(N, W, E, S))

resultframe = LabelFrame(root,text="Results")
resultframe.grid(column=1, row=5,columnspan=6,rowspan=4, sticky=(N, W, E, S))

tickerTitle = Label(inputframe,text="Tickers")
tickerTitle.grid(column=0,row=0)

tick = StringVar()
tick.set("IBEX35")

ticker = OptionMenu(inputframe, tick, "IBEX35")
ticker.grid(column=0,row=1)

moneyTitle = Label(inputframe,text="Money")
moneyTitle.grid(column=0,row=2)
moneyEntry = Entry(inputframe)
moneyEntry.grid(column=0,row=3)
moneyEntry.insert(0,"1000")

startButton = Button(root,text="Start",command=start)
startButton.grid(column=0,row=5)

graphTitle = Label(graphframe,text="Graph")
graphTitle.grid(column=0,row=0)
graphFrame = HtmlFrame(graphframe,horizontal_scrollbar="auto")
graphFrame.grid(column=0,row=1,columnspan=6,rowspan=4)
graphFrame.set_content("<html></html>")

resultTitle = Label(resultframe,text="Results")
resultTitle.grid(column=0,row=0)
resultButton = Button(resultframe,text="Results",padx=60,pady=40)
resultButton.grid(column=0,row=1,columnspan=6,rowspan=4)

root.mainloop()