from crearGrupos import CrearGrupoDeWhatsapp
from extraerDatos import extraerDatosDelExcel
from insertarDatos import insertarDatosDelExcel
import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class principal:

    
    chrome = webdriver.Chrome(executable_path='./chromedriver')

    wait = WebDriverWait(chrome,600)

    chrome.get('https://web.whatsapp.com/')

    cantidad_de_filas = 39
    contador = -1
    contador2 = 1


    for i in range(cantidad_de_filas):

        contador += 1

        #obteniendo Nombre de Grupo
        arreglo = extraerDatosDelExcel(cantidad_de_filas)
        nombreDelGrupo = arreglo[contador]
        #CreandoGrupo
        obtenerEnlace = CrearGrupoDeWhatsapp(str(nombreDelGrupo),wait,chrome,contador)
        time.sleep(1)
        #insertar enlace y nombre a excel
        insertarDatosDelExcel(nombreDelGrupo,obtenerEnlace,contador2)
        contador2 += 1
        
