import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


chrome = webdriver.Chrome(executable_path='./chromedriver')

wait = WebDriverWait(chrome,600)

chrome.get('https://web.whatsapp.com/')


def eliminarGrupoSeleccionado(nombreDelGrupo):
    
    time.sleep(5)

    x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    nameFieldGroup = wait.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
    nameFieldGroup.send_keys(nombreDelGrupo)
    time.sleep(5)
    x_encontrarElemento = '//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div/div[2]/div[1]/div[1]/span'
    x_encontrarElemento.__getattribute__("title")

    if(str(x_encontrarElemento) == None or str(x_encontrarElemento) == ""):

        nameFieldGroup.send_keys("")
        time.sleep(1)
        nameFieldGroup.send_keys(nombreDelGrupo)
        time.sleep(5)
        print("Buscó ELEMENTO")
        nameFieldGroup.send_keys(Keys.ENTER)

    elif(x_encontrarElemento == nombreDelGrupo):
        encontrarElemento = wait.until(ec.presence_of_element_located((By.XPATH,x_encontrarElemento)))
        encontrarElemento.click()
        



    nameFieldGroup.send_keys(Keys.ENTER)

    try:
        #Click en el boton de los 3 puntos
        x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
        buttonthreePoints = wait.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
        buttonthreePoints.click()

        #Click en Salir del Grupo
        x_botonSalirDelGrupo = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[5]/div[1]'
        botonSalirDelGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonSalirDelGrupo)))
        botonSalirDelGrupo.click()

        #Click en Confirmar Salida
        x_botonConfirmarSalidaDelGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div'
        botonConfirmarSalidaDelGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonConfirmarSalidaDelGrupo)))
        botonConfirmarSalidaDelGrupo.click()

        time.sleep(5)

        #Click en el boton de los 3 puntos
        x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
        buttonthreePoints = wait.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
        buttonthreePoints.click()

        #Click en Boton Eliminar Grupo
        x_botonoEliminarGrupo = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[4]/div[1]'
        botonoEliminarGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_botonoEliminarGrupo)))
        botonoEliminarGrupo.click()

        #Click en Confirmar Eliminacion de grupo
        x_botonConfirmarEliminacion = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div'
        botonConfirmarEliminacion = wait.until(ec.presence_of_element_located((By.XPATH,x_botonConfirmarEliminacion)))
        botonConfirmarEliminacion.click()

        print("GRUPO ELIMINADO")
        nameFieldGroup.send_keys("")

    except:

        nameFieldGroup.send_keys("")
        