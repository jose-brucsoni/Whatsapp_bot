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

    contador = -1

    (arregloNombres,arregloGrupo,arregloHorario,arregloSiglaMateria,arregloTurno,arregloModalidad,arregloMateriaSinAbreviar) = extraerDatosDelExcel()


    for i in arregloNombres:

        contador += 1

        #obteniendo los datos
        nombreDelGrupo = arregloNombres[contador]
        grupo = arregloGrupo[contador]
        horario = arregloHorario[contador]
        siglaMateria = arregloSiglaMateria[contador]
        turno = arregloTurno[contador]
        modalidad = arregloModalidad[contador]
        materiaSinAbreviar = arregloMateriaSinAbreviar[contador]
        #CreandoGrupo
        obtenerEnlace = CrearGrupoDeWhatsapp(str(nombreDelGrupo),str(grupo),str(horario),str(siglaMateria),str(turno),str(modalidad),str(materiaSinAbreviar),wait,chrome,contador)
        time.sleep(1)


        #insertar enlace y nombre a excel
        insertarDatosDelExcel(nombreDelGrupo,obtenerEnlace,contador)
        time.sleep(5)

        
