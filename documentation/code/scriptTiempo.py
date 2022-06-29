import numpy as np
import matplotlib.pyplot as plt 
import operator
from datetime import datetime, timedelta
import matplotlib.dates as mdates
myFmt = mdates.DateFormatter('%m')
########################################################
#                        Fase 1                        #
########################################################

inicio = datetime(2021,9,28)
fin    = datetime(2021,12,18)

lista_fechas = [inicio + timedelta(days=d) for d in range((fin - inicio).days + 1)] 
x=lista_fechas


inv =[0]*len(x)

prog =[0]*len(x)

mem = [0]*len(x)

org = [0]*len(x)

fix = [0]*len(x)

i =[inv]#investigacion

p =[prog]#programacion

m = [mem]#memoria

o = [org]#organizacion

f = [fix]#Fixes

n = [[0]*len(x)]#Null




time =[[2],[0],[0],[0],[1,2],[1],[4],[5],[3],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [3],[2,2],[0],[2],[6,1],[5],[4,1],[8],[8],[0],[4],[0],[0],[0],[0],[0],[0],
       [0],[0],[0],[0],[4,6],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[4],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[6]
       
       
       ]
category=[i,n,n,n,[inv,prog],p,p,p,p,n,n,n,n,n,n,n,n,n,
          p,[prog,mem],n,i,[prog,org],p,[inv,mem],p,o,n,i,n,n,n,n,n,n,
          n,n,n,n,[inv,prog],n,n,n,n,n,n,n,n,n,n,n,n,n,
          n,i,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,
          n,n,n,n,n,n,n,n,n,n,o
          
          
          
          
          
          ]

for day in range(len(time)):
    for cat in range(len(time[day])):
        category[day][cat][day:] = [y+time[day][cat] for y in category[day][cat][day:]]


plt.plot(x,fix,label="Fixes")
plot1 =list(map(operator.add, inv,mem ))
plt.plot(x,plot1,label="Memoria")
plot1 =list(map(operator.add, plot1, org))
plt.plot(x,plot1,label="Organizacion")
plot1 =list(map(operator.add, plot1,inv ))
plt.plot(x,plot1,label="Investigacion")
plot1 =list(map(operator.add, plot1,prog))
plt.plot(x,plot1,label="Programacion")

plt.title("Horas de trabajo Fase 1 (Acumulacion)",fontsize=15)
plt.xlabel("Mes",fontsize=13)
plt.ylabel("Horas",fontsize=13)
plt.legend(loc="upper left")
plt.gca().xaxis.set_major_formatter(myFmt)
plt.show()

########################################################
#                        Fase 2                        #
########################################################

inicio = datetime(2022,1,27)
fin    = datetime(2022,3,29)

lista_fechas = [inicio + timedelta(days=d) for d in range((fin - inicio).days + 1)] 
x=lista_fechas


inv =[0]*len(x)

prog =[0]*len(x)

mem = [0]*len(x)

org = [0]*len(x)

fix = [0]*len(x)

i =[inv]#investigacion

p =[prog]#programacion

m = [mem]#memoria

o = [org]#organizacion

f = [fix]#Fixes

n = [[0]*len(x)]#Null




time =[[6],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[0],[4,3],[4,3],[0],[3],[1,2.5],[1,2],
       [4],[0],[3],[6],[8],[5,4],[4],[2],[2],[4,7],[0],[4],
       [0],[0],[6],[0],[0],[0],[3],[10],[6,6],[8],[9],[4,3],
       [10],[3,9],[4,6],[4,2],[2,5,2],
       [3,1,2],[1,2,1],[2,7],[6,2],
       [13],[8],[4],[4,2],[8],[4,4],[6,2],[4,2]
       ]
category=[o,n,n,n,n,n,n,n,n,n,n,n,n,
          n,n,[org,inv],[org,prog],n,p,[org,prog],[inv,prog],
          p,n,p,p,p,[fix,prog],m,m,m,[org,fix],n,i,
          n,n,i,n,n,n,i,p,[org,prog],p,p,[prog,inv],
          m,[fix,prog],[prog,inv],[prog,inv],[inv,prog,fix],
          [org,inv,prog],[org,inv,prog],[inv,prog],[prog,fix],
          p,p,p,[fix,prog],p,[prog,inv],[fix,prog],[prog,fix]
          ]

for day in range(len(time)):
    for cat in range(len(time[day])):
        category[day][cat][day:] = [y+time[day][cat] for y in category[day][cat][day:]]


plt.plot(x,fix,label="Fixes")
plot1 =list(map(operator.add, inv,mem ))
plt.plot(x,plot1,label="Memoria")
plot1 =list(map(operator.add, plot1, org))
plt.plot(x,plot1,label="Organizacion")
plot1 =list(map(operator.add, plot1,inv ))
plt.plot(x,plot1,label="Investigacion")
plot1 =list(map(operator.add, plot1,prog))
plt.plot(x,plot1,label="Programacion")

plt.title("Horas de trabajo Fase 2 (Acumulacion)",fontsize=15)
plt.xlabel("Mes",fontsize=13)
plt.ylabel("Horas",fontsize=13)
plt.legend(loc="upper left")
plt.gca().xaxis.set_major_formatter(myFmt)
plt.show()

########################################################
#                        Fase 3                        #
########################################################

inicio = datetime(2022,4,9)
fin    = datetime(2022,6,28)

lista_fechas = [inicio + timedelta(days=d) for d in range((fin - inicio).days + 1)] 
x=lista_fechas


inv =[0]*len(x)

prog =[0]*len(x)

mem = [0]*len(x)

org = [0]*len(x)

fix = [0]*len(x)

i =[inv]#investigacion

p =[prog]#programacion

m = [mem]#memoria

o = [org]#organizacion

f = [fix]#Fixes

n = [[0]*len(x)]#Null




time =[[6],[6],[2,6],[0],[0],[4,6],[10],[0],[5],[2,2],[4],
       [8],[4],[3,2],[4,2],[4,2],[2.5],[0],[2],[0],[2],[2],
       [2],[2],[2],[2],[2],[2],[0],[2],[2],[2],[2],[2],[2],
       [2],[2],[2],[2],[0],[2],[2],[2],[2],[2],[2],[2],
       [4,2],[3,2],[5,2],[2],[2],[0],[2],[2],[2],[2],[2],
       [2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],
       [2],[2],[2],[2],[2],[2],[2],[2],[6],[8]
       

       ]
category=[o,p,[prog,inv],n,n,[prog,inv],i,n,o,[org,prog],p,
          p,p,[fix,prog],[prog,org],[prog,inv],i,n,m,n,m,m,
          m,m,m,m,m,m,n,m,m,m,m,m,m,
          m,m,m,m,n,m,m,m,m,m,m,m,
          [prog,mem],[prog,mem],[prog,mem],m,m,n,m,m,m,m,m,
          m,m,m,m,m,m,m,m,m,m,m,m,m,
          m,m,m,m,m,m,m,m,m,m
          
    ]

for day in range(len(time)):
    for cat in range(len(time[day])):
        category[day][cat][day:] = [y+time[day][cat] for y in category[day][cat][day:]]


plt.plot(x,fix,label="Fixes")
plot1 =list(map(operator.add, inv,mem ))
plt.plot(x,plot1,label="Memoria")
plot1 =list(map(operator.add, plot1, org))
plt.plot(x,plot1,label="Organizacion")
plot1 =list(map(operator.add, plot1,inv ))
plt.plot(x,plot1,label="Investigacion")
plot1 =list(map(operator.add, plot1,prog))
plt.plot(x,plot1,label="Programacion")

plt.title("Horas de trabajo Fase 3 (Acumulacion)",fontsize=15)
plt.xlabel("Mes",fontsize=13)
plt.ylabel("Horas",fontsize=13)
plt.legend(loc="upper left")
plt.gca().xaxis.set_major_formatter(myFmt)
plt.show()

########################################################
#                        Total                         #
########################################################

inicio = datetime(2021,9,28)
fin    = datetime(2022,6,28)

lista_fechas = [inicio + timedelta(days=d) for d in range((fin - inicio).days + 1)] 
x=lista_fechas


inv =[0]*len(x)

prog =[0]*len(x)

mem = [0]*len(x)

org = [0]*len(x)

fix = [0]*len(x)

i =[inv]#investigacion

p =[prog]#programacion

m = [mem]#memoria

o = [org]#organizacion

f = [fix]#Fixes

n = [[0]*len(x)]#Null



time =[
       #Fase 1
       [2],[0],[0],[0],[1,2],[1],[4],[5],[3],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [3],[2,2],[0],[2],[6,1],[5],[4,1],[8],[8],[0],[4],[0],[0],[0],[0],[0],[0],
       [0],[0],[0],[0],[4,6],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[4],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[6],
       #Parada
       [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       #Fase 2
       [6],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       [0],[0],[4,3],[4,3],[0],[3],[1,2.5],[1,2],
       [4],[0],[3],[6],[8],[5,4],[4],[2],[2],[4,7],[0],[4],
       [0],[0],[6],[0],[0],[0],[3],[10],[6,6],[8],[9],[4,3],
       [10],[3,9],[4,6],[4,2],[2,5,2],
       [3,1,2],[1,2,1],[2,7],[6,2],
       [13],[8],[4],[4,2],[8],[4,4],[6,2],[4,2],
       #Parada
       [0],[0],[0],[0],[0],[0],[0],[0],[0],[0],
       #Fase 3
       [6],[6],[2,6],[0],[0],[4,6],[10],[0],[5],[2,2],[4],
       [8],[4],[3,2],[4,2],[4,2],[2.5],[0],[2],[0],[2],[2],
       [2],[2],[2],[2],[2],[2],[0],[2],[2],[2],[2],[2],[2],
       [2],[2],[2],[2],[0],[2],[2],[2],[2],[2],[2],[2],
       [4,2],[3,2],[5,2],[2],[2],[0],[2],[2],[2],[2],[2],
       [2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],
       [2],[2],[2],[2],[2],[2],[2],[2],[6],[8]
       ]
category=[
          #Fase 1
          i,n,n,n,[inv,prog],p,p,p,p,n,n,n,n,n,n,n,n,n,
          p,[prog,mem],n,i,[prog,org],p,[inv,mem],p,o,n,i,n,n,n,n,n,n,
          n,n,n,n,[inv,prog],n,n,n,n,n,n,n,n,n,n,n,n,n,
          n,i,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,
          n,n,n,n,n,n,n,n,n,n,o,
          #Parada
          n,n,n,n,n,n,n,n,n,n,n,n,n,
          n,n,n,n,n,n,n,n,n,n,n,n,n,
          n,n,n,n,n,n,n,n,n,n,n,n,n,
          #Fase 2
          o,n,n,n,n,n,n,n,n,n,n,n,n,
          n,n,[org,inv],[org,prog],n,p,[org,prog],[inv,prog],
          p,n,p,p,p,[fix,prog],m,m,m,[org,fix],n,i,
          n,n,i,n,n,n,i,p,[org,prog],p,p,[prog,inv],
          m,[fix,prog],[prog,inv],[prog,inv],[inv,prog,fix],
          [org,inv,prog],[org,inv,prog],[inv,prog],[prog,fix],
          p,p,p,[fix,prog],p,[prog,inv],[fix,prog],[prog,fix],
          #Parada
          n,n,n,n,n,n,n,n,n,n,
          #Fase 3
          o,p,[prog,inv],n,n,[prog,inv],i,n,o,[org,prog],p,
          p,p,[fix,prog],[prog,org],[prog,inv],i,n,m,n,m,m,
          m,m,m,m,m,m,n,m,m,m,m,m,m,
          m,m,m,m,n,m,m,m,m,m,m,m,
          [prog,mem],[prog,mem],[prog,mem],m,m,n,m,m,m,m,m,
          m,m,m,m,m,m,m,m,m,m,m,m,m,
          m,m,m,m,m,m,m,m,m,m
          
          
          ]

for day in range(len(time)):
    for cat in range(len(time[day])):
        category[day][cat][day:] = [y+time[day][cat] for y in category[day][cat][day:]]


plt.plot(x,fix,label="Fixes")
plot1 =list(map(operator.add, inv,mem ))
plt.plot(x,plot1,label="Memoria")
plot1 =list(map(operator.add, plot1, org))
plt.plot(x,plot1,label="Organizacion")
plot1 =list(map(operator.add, plot1,inv ))
plt.plot(x,plot1,label="Investigacion")
plot1 =list(map(operator.add, plot1,prog))
plt.plot(x,plot1,label="Programacion")

plt.title("Horas de trabajo Totales (Acumulacion)",fontsize=15)
plt.xlabel("Mes",fontsize=13)
plt.ylabel("Horas",fontsize=13)
plt.legend(loc="upper left")
plt.gca().xaxis.set_major_formatter(myFmt)
plt.show()
