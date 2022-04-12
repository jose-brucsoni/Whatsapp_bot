from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from herramientas import agregarAdminyEliminarGrupo_tool
from herramientas import salirDelGrupo
from buscarGrupo import buscarGrupo
from datetime import datetime
from openpyxl import Workbook
from openpyxl import load_workbook
from remove import remove
import sesion as keepSession


with open('./resource/session.log', 'r') as f:
    sesion = f.read().split(',')
    id = sesion[0]
    url = sesion[1]
chrome = keepSession.openSession(id, url)
driver = WebDriverWait(chrome, 600)

action = ActionChains(chrome)

contadorParaContactos = -1
contadorParaNombres = -1
array_nombreIntegrantes = []

# Click a Boton De 3 puntos
x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
buttonthreePoints = driver.until(
ec.presence_of_element_located((By.XPATH, x_threePointsButton)))
buttonthreePoints.click()

time.sleep(1)

# Click en Info Grupo
x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
buttonInfoGrupo = driver.until(
ec.presence_of_element_located((By.XPATH, x_InfoGrupoButton)))
buttonInfoGrupo.click()

time.sleep(1)
#******************************************************************************************************
# Extrae los integrantes del grupo
x_cantidadIntegrantesDelGrupo = chrome.find_element(
By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div/div[3]/span/span/button')
cantidadIntegrantesDelGrupo = x_cantidadIntegrantesDelGrupo.get_attribute(
"textContent")
suma_cantidadDeIntegrantes = int(
cantidadIntegrantesDelGrupo[0] + cantidadIntegrantesDelGrupo[1])
#******************************************************************************************************
#Empieza
time.sleep(2)
if(suma_cantidadDeIntegrantes > 1):
    try:
        if(suma_cantidadDeIntegrantes > 11):
            suma_cantidadDeIntegrantes = 11

        for i in range(suma_cantidadDeIntegrantes+1):
            contadorParaContactos += 1
            try:

                xpathParte1 = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div/div/div['
                xpathCompleto = xpathParte1 + str(contadorParaContactos) + "]"
                x_primerContacto = chrome.find_element(By.XPATH,xpathCompleto.strip())
                xy_primerContacto = str(x_primerContacto.get_attribute("textContent"))
                primerContacto = xy_primerContacto.strip()
                if(primerContacto == None or primerContacto == ""):

                    array_nombreIntegrantes.append("+591 00000000")
                    

                else:
                    array_nombreIntegrantes.append(primerContacto)
                    



            except:
                extraerElNombreDeLosContactos = "+591 00000000"
                array_nombreIntegrantes.append(extraerElNombreDeLosContactos)
                


                
        print("Nombre de Integrantes:")
        for i in array_nombreIntegrantes:
            contadorParaNombres += 1
            textoExtraido = array_nombreIntegrantes[contadorParaNombres]
            textoFiltrado = textoExtraido.strip()

            if(textoFiltrado[0] != "+"):

                if(textoFiltrado[0:2] != "Tú" and textoFiltrado[0:7] != "Celular"):
                    

                    print(textoFiltrado[0:25], "<==> Docente")
                    

                elif(textoFiltrado[0:4] == "Vacio"):
                    print("")
                else:
                    print("Tú eres el Administrador")

            elif(textoFiltrado[0] == "+"):
                print(textoFiltrado[0:13], "<==> Alumno")
            else:
                print("Error de Contacto")
    except:
        print("No dio")