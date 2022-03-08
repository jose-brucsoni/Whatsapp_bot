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

groupName = "Grupo Para pruebas"




#Aqui empieza a enviar el enlace del grupo
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


#Click Lupa para buscar participante
x_lupaBuscarParticipante = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[1]/div/div/div[2]/span'
lupaBuscarParticipante = wait.until(ec.presence_of_element_located((By.XPATH,x_lupaBuscarParticipante)))
lupaBuscarParticipante.click()

time.sleep(2)


try:
    link = chrome.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/span/span')
    retornarlink = str(link.get_attribute("textContent"))

    if(retornarlink[0] != "+" or retornarlink[0] != "6" or retornarlink[0] != "7"):

        print("hay Conocidos---------------------------------")
        #click en el contacto, en el primero
        x_clickEnContacto = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/span/span'
        clickEnContacto = wait.until(ec.presence_of_element_located((By.XPATH,x_clickEnContacto)))
        clickEnContacto.click()


        #Click en "Designar como admin del grupo"
        x_buttonDesignarAdministrador = '//*[@id="app"]/div[1]/span[4]/div/ul/div/li[1]/div[1]'
        buttonDesignarAdministrador = wait.until(ec.presence_of_element_located((By.XPATH,x_buttonDesignarAdministrador)))
        buttonDesignarAdministrador.click()


        #Salir de la ventana participantes
        x_salirDelaVentanaParticipantes = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div/header/div/div[1]/button/span'
        salirDelaVentanaParticipantes = wait.until(ec.presence_of_element_located((By.XPATH,x_salirDelaVentanaParticipantes)))
        salirDelaVentanaParticipantes.click()
except:
        print("No hay Conocidos-------------------------------")
        #Salir de la ventana participantes
        x_salirDelaVentanaParticipantes = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div/header/div/div[1]/button/span'
        salirDelaVentanaParticipantes = wait.until(ec.presence_of_element_located((By.XPATH,x_salirDelaVentanaParticipantes)))
        salirDelaVentanaParticipantes.click()

