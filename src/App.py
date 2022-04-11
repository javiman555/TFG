from tkinter import *
from tkinter import messagebox


def start():
    response = messagebox.askokcancel("Aproximated wait time","It seems the proccess could take up to infinity seconds. Continue?")
    if response == 1:
        #We call the proccess
        pass
    
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
graphButton = Button(graphframe,text="Graph",padx=60,pady=40)
graphButton.grid(column=0,row=1,columnspan=6,rowspan=4)

resultTitle = Label(resultframe,text="Results")
resultTitle.grid(column=0,row=0)
resultButton = Button(resultframe,text="Results",padx=60,pady=40)
resultButton.grid(column=0,row=1,columnspan=6,rowspan=4)

root.mainloop()