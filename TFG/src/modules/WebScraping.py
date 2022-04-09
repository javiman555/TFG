from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import requests
from fake_useragent import UserAgent
import os

class WebScraping():
    
    
    def __init__(self,graphic):
        
        self.url='https://finance.yahoo.com/quote/'
        self.ua_str = UserAgent().chrome
        if graphic:
            path = '/Users/javier/Desktop/chromedriver' # write the path here
        
            self.driver = webdriver.Chrome(path)
        else:
            path = '/Users/javier/Desktop/chromedriver' # write the path here
        
            self.driver = webdriver.Chrome(path)
        
        self.stocks =['SAB.MC', 'SAN.MC', 'AENA.MC', 'ELE.MC', 'NTGY.MC', 'PHM.MC', 'ENG.MC', 'GRF.MC', 'CABK.MC', 'ITX.MC', 'BKT.MC', 'VIS.MC', 'REE.MC', 'CLNX.MC', 'BBVA.MC', 'MRL.MC', 'FER.MC', 'MTS.MC', 'MAP.MC', 'COL.MC', 'ACX.MC', 'ACS.MC', 'IBE.MC', 'FDR.MC', 'TEF.MC', 'ANA.MC', 'IAG.MC', 'AMS.MC', 'SGRE.MC', 'MEL.MC']

    def scrapeNameStocks(self):

        self.driver.get(self.url+'%5EIBEX/components?p=%5EIBEX')
        # locate a button
        cookie_button1 = self.driver.find_element_by_xpath('//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button')
        # click on a button
        cookie_button1.click()
        
        
        matches = self.driver.find_elements_by_css_selector('tr')
        
        # storage in a list
        all_stock_data = [match.text for match in matches]
        
        self.stocks=[]
        all_stock_data.pop(0)
        for element in all_stock_data:
            self.stocks.append(element[0: element.find(" ")])

    def scrapeDataStocks(self):

        for element in self.stocks:
            url ='https://query1.finance.yahoo.com/v7/finance/download/'+element+'?period1=946857600&period2=1634688000&interval=1d&events=history&includeAdjustedClose=true'
            r = requests.get(url, headers={"User-Agent": self.ua_str})
            
            filepath = os.path.join('./db', element+'.csv')
            if not os.path.exists('./db'):
                os.makedirs('./db')
            
            open(filepath, 'wb').write(r.content)