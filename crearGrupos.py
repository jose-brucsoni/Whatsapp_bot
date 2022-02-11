import imp
from tkinter import N
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

def CrearGrupoDeWhatsapp(groupName,wait,chrome,contador):
        
    #Click Boton de 3 puntos
    x_menuButton = '//div[@title="Menú"]'
    menuButton = wait.until(ec.presence_of_element_located((By.XPATH, x_menuButton)))
    menuButton.click()


    #Click en Boton "Nuevo Grupo"
    x_newGroup = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[1]/div[1]'
    newGroup = wait.until(ec.presence_of_element_located((By.XPATH, x_newGroup)))
    newGroup.click()


    #Ingresa nombre en el 'TextBox' de buscar contactos
    x_name = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div/div/input'
    nameField = wait.until(ec.presence_of_element_located((By.XPATH,x_name)))
    nameField.send_keys('Joel Godoy') #Ingresar el nombre del contacto
    nameField.send_keys(Keys.ENTER)


    #Click en añadir Contacto
    x_name = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/span/div/span'
    buttonSaveContact = wait.until(ec.presence_of_element_located((By.XPATH,x_name)))
    buttonSaveContact.click()



    #Añade nombre del grupo y lo Crea
    x_group = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[2]'
    nameField = wait.until(ec.presence_of_element_located((By.XPATH,x_group)))
    nameField.send_keys(groupName + Keys.ENTER)

    time.sleep(10)

    #Aqui empieza a enviar el enlace del grupo

    x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    nameFieldGroup = wait.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
    nameFieldGroup.send_keys(groupName)
    time.sleep(5)
    x_encontrarElemento = '//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div/div[2]/div[1]/div[1]/span'
    x_encontrarElemento.__getattribute__("title")

    if(str(x_encontrarElemento) == None or str(x_encontrarElemento) == ""):

        nameFieldGroup.send_keys("")
        time.sleep(1)
        nameFieldGroup.send_keys(groupName)
        time.sleep(5)
        print("Buscó ELEMENTO")
        nameFieldGroup.send_keys(Keys.ENTER)

    elif(x_encontrarElemento == groupName):
        encontrarElemento = wait.until(ec.presence_of_element_located((By.XPATH,x_encontrarElemento)))
        encontrarElemento.click()



    nameFieldGroup.send_keys(Keys.ENTER)

        


    #Click a Boton De 3 puntos
    x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
    buttonthreePoints = wait.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
    buttonthreePoints.click()

    #Click en Info Grupo
    x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
    buttonInfoGrupo = wait.until(ec.presence_of_element_located((By.XPATH,x_InfoGrupoButton)))
    buttonInfoGrupo.click()

    #Click Enlace de invitacion del grupo
    x_EnlaceInvitacioButton = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[2]/div[2]'
    buttonEnlaceInvitacio = wait.until(ec.presence_of_element_located((By.XPATH,x_EnlaceInvitacioButton)))
    buttonEnlaceInvitacio.click()

    time.sleep(3)
    
    #Copia el Enlace de invitacion del grupo
    link = chrome.find_element_by_xpath('//*[@id="group-invite-link-anchor"]')
    print(contador)
    retornarlink = link.get_attribute("href")
    return retornarlink