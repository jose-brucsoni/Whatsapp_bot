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


lst=[]


chrome = webdriver.Edge(executable_path='./msedgedriver')

wait = WebDriverWait(chrome,600)
chrome.implicitly_wait(20) # da una espera implícita de 20 segundos

chrome.get('https://web.whatsapp.com/')

groupName = "DIR.ESTRATÉGICA.I_PT"




#Aqui empieza a Buscar el grupo
x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
nameFieldGroup = wait.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
nameFieldGroup.send_keys(groupName + Keys.ENTER)
chrome.implicitly_wait(20) # da una espera implícita de 20 segundos
x_encontrarElemento = '//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div/div[2]/div[1]/div[1]/span'
x_encontrarElemento.__getattribute__("title")

buscarGrupo.buscarGrupoEntextBox(x_encontrarElemento,groupName,nameFieldGroup,wait)

#Click a Boton De 3 puntos
x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
buttonthreePoints = wait.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
buttonthreePoints.click()

#Click en Info Grupo
x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
buttonInfoGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_InfoGrupoButton)))
buttonInfoGrupo.click()



#Click en Salir del grupo
x_botonParaSalirDelGrupo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div[1]/div[2]/div/span'
botonParaSalirDelGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonParaSalirDelGrupo)))
botonParaSalirDelGrupo.click()



#Click en confirmar salida
x_botonParaConfirmarSalidaDelGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]'
botonParaConfirmarSalidaDelGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonParaConfirmarSalidaDelGrupo)))
botonParaConfirmarSalidaDelGrupo.click()

time.sleep(10)

#Aqui empieza a Buscar el grupo
x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
nameFieldGroup = wait.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
nameFieldGroup.send_keys(groupName + Keys.ENTER)
chrome.implicitly_wait(20) # da una espera implícita de 20 segundos
x_encontrarElemento = '//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div/div[2]/div[1]/div[1]/span'
x_encontrarElemento.__getattribute__("title")

buscarGrupo.buscarGrupoEntextBox(x_encontrarElemento,groupName,nameFieldGroup,wait)

#Click a Boton De 3 puntos
x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
buttonthreePoints = wait.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
buttonthreePoints.click()

#Click en Info Grupo
x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
buttonInfoGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_InfoGrupoButton)))
buttonInfoGrupo.click()


#Click en Salir del grupo
x_botonEliminarGrupo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[1]/div[2]/div/span'
botonEliminarGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonEliminarGrupo)))
botonEliminarGrupo.click()

#Click en Salir del grupo
x_botonConfirmarEliminacionDeGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]'
botonConfirmarEliminacionDeGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonConfirmarEliminacionDeGrupo)))
botonConfirmarEliminacionDeGrupo.click()