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


chrome = webdriver.Chrome(executable_path='./chromedriver')

wait = WebDriverWait(chrome,600)
chrome.implicitly_wait(20) # da una espera implícita de 20 segundos



#Se Carga el archivo Excel
excel = load_workbook('modulo2.xlsx')
#Selecciona la hoja dentro del excel
ws = excel['modulo2']
#Selecciona el rango de la tabla
cell_range = ws['A2':'R500']


contador = -1

for i in cell_range:

        contador += 1

        if(cell_range[contador][11].value != None and cell_range[contador][12].value != None):

            enlace = str(cell_range[contador][11].value)
            nombreDeGrupo = str(cell_range[contador][12].value)
            chrome.get(enlace)
            
            
            nombreDegrupo = chrome.find_element_by_xpath('//*[@id="main_block"]/div[1]/h2')
            retornarnombreDegrupo = nombreDegrupo.get_attribute("textContent")


            if(retornarnombreDegrupo == nombreDeGrupo):

                cell_range[contador][15].value = "Verificado"

            elif(retornarnombreDegrupo != nombreDeGrupo):
                
                cell_range[contador][15].value = "NO COINCIDE"
                cell_range[contador][16].value = retornarnombreDegrupo
            else:
                cell_range[contador][15].value = "Else"
                print("Else")

        elif(cell_range[contador][3].value != None):
            cell_range[contador][15].value = "Crear Grupo"


chrome.close()
excel.save('modulo2.xlsx')





