import imp
import sys
from tkinter import N
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from buscarGrupo import buscarGrupo
from datetime import datetime

def CrearGrupoDeWhatsapp(groupName,grupo,horario,siglaMateria,turno,modalidad,materia,wait,chrome,contador):

        
        
    #Click Boton de 3 puntos
    x_menuButton = '//div[@title="Menú"]'
    menuButton = wait.until(ec.presence_of_element_located((By.XPATH, x_menuButton)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    menuButton.click()


    #Click en Boton "Nuevo Grupo"
    x_newGroup = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[1]/div[1]'
    newGroup = wait.until(ec.presence_of_element_located((By.XPATH, x_newGroup)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    newGroup.click()


    #Ingresa nombre en el 'TextBox' de buscar contactos
    x_name = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div/div[1]/div/div/input'
    nameField = wait.until(ec.presence_of_element_located((By.XPATH,x_name)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    time.sleep(1)
    nameField.clear()
    nameField.send_keys('77365280') #Celular 2 actualmente
    time.sleep(1)
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    nameField.send_keys(Keys.ENTER)

    time.sleep(1)    #Click en añadir Contacto
    x_name = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div/span/div/span'
    buttonSaveContact = wait.until(ec.presence_of_element_located((By.XPATH,x_name)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    buttonSaveContact.click()



    #Añade nombre del grupo y lo Crea
    x_group = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]'
    nameField = wait.until(ec.presence_of_element_located((By.XPATH,x_group)))
    nameField.send_keys(groupName + Keys.ENTER)


    # try:
    #     x_AvisoDeBloqueo = '//*[@id="app"]/div[1]/span[1]/div/div/span'
    #     AvisoDeBloqueo = wait.until(ec.presence_of_element_located((By.XPATH,x_AvisoDeBloqueo)))
        
    #     time.sleep(1.5)
    #     textoDeAviso = str(AvisoDeBloqueo.get_attribute("textContent"))

    #     if(textoDeAviso == "No se pudo crear el grupo. Creaste demasiados grupos en muy poco tiempo. Vuelve a intentarlo más tarde."):
            
    #         print("********************************************---NOS BLOQUEO WHATSAPP---********************************************\n")
    #         print("AVISO DE WHATSAPP    "+textoDeAviso,"\n")
    #         print("Se detuvo en: \n Materia:", materia ,"_",grupo,"\n Con el contador a:", contador,"\n")
    #         print("Nos bloquearon a la siguiente fecha y hora: "+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),"\n")
    #         sys.exit("********************************************---NOS BLOQUEO WHATSAPP---********************************************\n")
    # except:
        
    time.sleep(1)

    #Aqui empieza a enviar el enlace del grupo----------------------------------------------------------------------------------------------
    x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    nameFieldGroup = wait.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
    nameFieldGroup.clear()
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    nameFieldGroup.send_keys(groupName)
    time.sleep(1)
    nameFieldGroup.send_keys(Keys.ENTER)

    # buscarGrupo.buscarGrupoEntextBox(x_encontrarElemento,groupName,nameFieldGroup,wait)


    #Click a Boton De 3 puntos
    x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
    buttonthreePoints = wait.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    buttonthreePoints.click()

    #Click en Info Grupo
    x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
    buttonInfoGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_InfoGrupoButton)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    time.sleep(1)
    buttonInfoGrupo.click()

    #Click Enlace de invitacion del grupo
    x_EnlaceInvitacioButton = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[2]/div[2]'
    buttonEnlaceInvitacio = wait.until(ec.presence_of_element_located((By.XPATH,x_EnlaceInvitacioButton)))
    time.sleep(1)
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    buttonEnlaceInvitacio.click()

    time.sleep(3)

    #Copia el Enlace de invitacion del grupo
    link = chrome.find_element_by_xpath('//*[@id="group-invite-link-anchor"]')
    retornarlink = link.get_attribute("href")

    #Fase de Añadir Descripcion del Grupo


    #click en botono para atras
    x_botonParaAtras = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button'
    botonParaAtras = wait.until(ec.presence_of_element_located((By.XPATH,x_botonParaAtras)))
    chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
    time.sleep(1)
    botonParaAtras.click()


    #Añadir Descripcion del Grupo
    x_textoDeingresarDescripcion = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[2]/div[1]/div/div/div'
    textoDeingresarDescripcion = wait.until(ec.presence_of_element_located((By.XPATH,x_textoDeingresarDescripcion)))
    textoDeingresarDescripcion.click()

    #Click en icono de lapiz de añadir descripcion
    x_botonGuardarDescripcion = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[2]/div[1]/div/div/span[2]/button'
    botonGuardarDescripcion = wait.until(ec.presence_of_element_located((By.XPATH,x_botonGuardarDescripcion)))
    botonGuardarDescripcion.click()


    x_Bienvenida = "UTEPSA - Modulo(3)"
    x_separador = "-----------------------"
    x_materia = "Materia: " + materia
    x_grupo = "Grupo: " + grupo
    x_horario = "Horario: " + horario
    x_turno = "Turno: " + turno
    x_modalidad = "Modalidad: " + modalidad
    x_siglaMateria = "Sigla de Materia: " + siglaMateria
    x_docente = "Docente: "
    x_Enlace = "Enlace: "

    #ingresar descripcion y guardar
    x_TextBoxIngresarDescripcion = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[2]/div[1]/div/div[1]/div/div/div[2]'
    TextBoxIngresarDescripcion = wait.until(ec.presence_of_element_located((By.XPATH,x_TextBoxIngresarDescripcion)))
    TextBoxIngresarDescripcion.clear()
    TextBoxIngresarDescripcion.send_keys(x_Bienvenida+ (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT) + x_separador + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_materia + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_grupo + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_horario + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_turno + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_modalidad + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_siglaMateria + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_docente + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_Enlace)

    TextBoxIngresarDescripcion.send_keys(Keys.ENTER)


    #ingresar descripcion y guardar
    x_textBoxDeChat = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    textBoxDeChat = wait.until(ec.presence_of_element_located((By.XPATH,x_textBoxDeChat)))
    textBoxDeChat.send_keys(x_Bienvenida+ (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT) + x_separador + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_materia + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_grupo + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_horario + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_turno + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_modalidad + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_siglaMateria + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_docente + (Keys.LEFT_SHIFT + Keys.ENTER) + (Keys.LEFT_SHIFT)+ x_Enlace)

    textBoxDeChat.send_keys(Keys.ENTER)

    print("CONTEO DE PROCESOS = ",contador)
    print("Materia = ", materia,"_",grupo)

    return retornarlink