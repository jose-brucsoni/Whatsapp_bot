import imp
import sys
from tkinter import N
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import datetime


class buscarGrupo:

    def buscarGrupoEntextBox(x_encontrarElemento,groupName,nameFieldGroup,wait):
    
        if(str(x_encontrarElemento) == None or str(x_encontrarElemento) == ""):

            nameFieldGroup.send_keys("")
            time.sleep(1)
            nameFieldGroup.send_keys(groupName)
            time.sleep(5)
            print("Buscó ELEMENTO")
            nameFieldGroup.send_keys(Keys.ENTER)
            buscarGrupo.buscarGrupoEntextBox(x_encontrarElemento,groupName,nameFieldGroup,wait)


        elif(x_encontrarElemento == groupName):
            encontrarElemento = wait.until(ec.presence_of_element_located((By.XPATH,x_encontrarElemento)))
            encontrarElemento.click()
