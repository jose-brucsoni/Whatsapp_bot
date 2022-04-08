from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from buscarGrupo import buscarGrupo
from datetime import datetime
from openpyxl  import Workbook
from openpyxl import load_workbook
from remove import remove

#Se Carga el archivo Excel 2
excel2 = load_workbook('modulo2.xlsx')
#Selecciona la hoja dentro del excel 2
ws2 = excel2['modulo2']
#Selecciona el rango de la tabla 2
cell_range2 = ws2['A2':'P500']

chrome = webdriver.Edge(executable_path='./msedgedriver')

driver = WebDriverWait(chrome,600)
chrome.implicitly_wait(20) # da una espera implícita de 20 segundos

chrome.get('https://web.whatsapp.com/')

groupName = "Grupo Para Pruebas"


panel = driver.find_element_by_xpath("//*[@id='pane-side']")
b=0
a = driver.execute_script("return arguments[0].scrollHeight;",panel)
for i in range (0,a):
        try:
            s=driver.find_element_by_xpath("//span[@title='Diana']")
            if (ec.presence_of_element_located((By.XPATH,s))):
                print ("se encontro a Diana")
                s.click()
                break
        except:
            b=i*10
            driver.execute_script("arguments[0].scroll(0,arguments[1]);",panel,b)
            #driver.execute_script("arguments[0].scrollIntoView();",panel,)