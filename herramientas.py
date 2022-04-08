from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from buscarGrupo import buscarGrupo
from datetime import datetime
from openpyxl import Workbook
from openpyxl import load_workbook
from remove import remove
import sesion as keepSession


def salirDelGrupo(driver, groupName):
        # ---------------------------------------------------------------------------------------
        # Click en Salir del grupo
        x_botonParaSalirDelGrupo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div[1]'
        botonParaSalirDelGrupo = driver.until(
            ec.presence_of_element_located((By.XPATH, x_botonParaSalirDelGrupo)))
        botonParaSalirDelGrupo.click()

        # Click en confirmar salida
        x_botonParaConfirmarSalidaDelGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]'
        botonParaConfirmarSalidaDelGrupo = driver.until(
            ec.presence_of_element_located((By.XPATH, x_botonParaConfirmarSalidaDelGrupo)))
        botonParaConfirmarSalidaDelGrupo.click()

        time.sleep(4)

        # Aqui empieza a Buscar el grupo
        x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        nameFieldGroup = driver.until(
            ec.presence_of_element_located((By.XPATH, x_nameFieldGroup)))
        nameFieldGroup.clear()
        nameFieldGroup.send_keys(groupName)
        nameFieldGroup.send_keys(Keys.ENTER)

        
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

        # Click en Salir del grupo
        x_botonEliminarGrupo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[1]'
        botonEliminarGrupo = driver.until(
            ec.presence_of_element_located((By.XPATH, x_botonEliminarGrupo)))
        botonEliminarGrupo.click()

        # Click  confirmar en Salir del grupo
        x_botonConfirmarEliminacionDeGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]'
        botonConfirmarEliminacionDeGrupo = driver.until(
            ec.presence_of_element_located((By.XPATH, x_botonConfirmarEliminacionDeGrupo)))
        botonConfirmarEliminacionDeGrupo.click()

        # Confirma el guardado de los datos en Excel

        print("El GRUPO: '", groupName, "', BORRADO")


def agregarAdminyEliminarGrupo_tool(driver, chrome, groupName, cell_range, contador, excel, action):

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

        # Extrae los integrantes del grupo
        x_cantidadIntegrantesDelGrupo = chrome.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div/div[3]/span/span/button')
        cantidadIntegrantesDelGrupo = x_cantidadIntegrantesDelGrupo.get_attribute(
            "textContent")
        suma_cantidadDeIntegrantes = int(
            cantidadIntegrantesDelGrupo[0] + cantidadIntegrantesDelGrupo[1])

        time.sleep(2)
        if(suma_cantidadDeIntegrantes > 9):

            try:
                # Extraer el nombre del primer contacto, debajo de "Tú"--------------------------------------------------------------------
                x_primerContacto = chrome.find_element(
                    By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[3]/div/div[9]')
                xy_primerContacto = str(
                    x_primerContacto.get_attribute("textContent"))
                primerContacto = xy_primerContacto.strip()
                try:
                    # Extrae si el primer contacto es admin, si no lo es pasa al "Except"
                    x_primerContactoAdmin = chrome.find_element(
                        By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[3]/div/div[9]/div/div/div[2]/div[1]/div[2]')
                    primerContactoAdmin = str(
                        x_primerContactoAdmin.get_attribute("textContent"))

                    if(primerContactoAdmin.strip() == "Admin. del grupo" or primerContactoAdmin[0].strip() == "A"):
                        print("Ya Contiene Administrador")
                        print("El Grupo: ", groupName)
                        print("El Administrador es: ", primerContacto)
                        cell_range[contador][27].value = "ELIMINADO"
                        cell_range[contador][28].value = primerContacto
                        excel.save('modulo3_enlaces_actualizado.xlsx')
                        salirDelGrupo(driver, groupName)

                except:
                    # Compara si el primer contacto es docente
                    print(primerContacto[0:9])
                    if(primerContacto[0] != "+" and primerContacto[0:9] != "Celular 2" and primerContacto[0:9] != "Celular 1"):

                        agregarPrimerContacto(driver, chrome, groupName, cell_range, contador,
                                            excel, action, cantidadIntegrantesDelGrupo, primerContacto)

                    else:
                        # Extraer el nombre del segundo contacto, debajo de "Tú"----------------------------------------------------------------

                        x_segundoContacto = chrome.find_element(
                            By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[3]/div/div[8]')
                        xy_segundoContacto = str(
                            x_segundoContacto.get_attribute("textContent"))
                        segundoContacto = xy_segundoContacto.strip()

                    # Compara si el segundo contacto es Admin
                    try:
                        x_segundoContactoAdmin = chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[3]/div/div[8]/div/div/div[2]/div[1]/div[2]')
                        segundoContactoAdmin = str(
                            x_segundoContactoAdmin.get_attribute("textContent"))

                        if(segundoContactoAdmin.strip() == "Admin. del grupo" or segundoContactoAdmin[0].strip() == "A"):
                            print("Ya Contiene Administrador")
                            print("El Administrador es: ",
                                segundoContacto)
                            cell_range[contador][27].value = "ELIMINADO"
                            cell_range[contador][28].value = segundoContacto
                            excel.save(
                                'modulo3_enlaces_actualizado.xlsx')
                            salirDelGrupo(driver, groupName)

                    except:
                        # Compara si el segundo contacto es docente
                        if(segundoContacto[0] != "+" and segundoContacto[0:9] != "Celular 2" and segundoContacto[0:9] != "Celular 1"):
                            agregarSegundoContacto(driver, chrome, groupName, cell_range, contador,
                                                excel, action, cantidadIntegrantesDelGrupo, primerContacto)
                        else:
                            print("GRUPO SIN DOCENTE => ", groupName)
                            cell_range[contador][27].value = "GRUPO SIN DOCENTE"
                            excel.save(
                                'modulo3_enlaces_actualizado.xlsx')
            except:

                print("No Encontro contactos")

        elif(suma_cantidadDeIntegrantes <= 2):
            print("RECICLAR EL GRUPO", groupName)
            cell_range[contador][27].value = "RECICLAR"
            excel.save('modulo3_enlaces_actualizado.xlsx')
        else:
            print("GRUPO MENOR A 9 PARTICIPANTES", groupName)
            cell_range[contador][27].value = "CONTIENE MENOS DE 9 INTEGRANTES"
            excel.save('modulo3_enlaces_actualizado.xlsx')


def agregarSegundoContacto(driver, chrome, groupName, cell_range, contador, excel, action, cantidadIntegrantesDelGrupo, primerContacto):
    # Click para Desplegar las opciones de usuario
    button_nameFieldGroup = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[3]/div/div[8]/div/div/div[2]/div[2]/div[2]'
    button_nameFieldGroup = chrome.find_element(
        By.XPATH, button_nameFieldGroup)
    action.move_to_element(
        button_nameFieldGroup).perform()
    button_nameFieldGroup.click()

    x_botonAsignarAdministrador = '//*[@id="app"]/div[1]/span[4]/div/ul/div/li[1]'
    botonAsignarAdministrador = driver.until(ec.presence_of_element_located((By.XPATH, x_botonAsignarAdministrador)))
    botonAsignarAdministrador.click()
    try:
        textoExtraidoDeAsignacion = str(
            x_botonAsignarAdministrador.get_attribute("textContent"))

        if(textoExtraidoDeAsignacion.strip() == "Eliminar" or textoExtraidoDeAsignacion[0].strip() == "E"):
            print("Ya Contiene Administrador")
            print("El Grupo: ", groupName)
            print("Con el Docente: ",
                primerContacto)
            print("Contenia: ",
                cantidadIntegrantesDelGrupo)
            cell_range[contador][27].value = "ELIMINADO"
            cell_range[contador][28].value = primerContacto
            excel.save(
                'modulo3_enlaces_actualizado.xlsx')
            salirDelGrupo(driver, groupName)

    except:

        x_botonConfirmarAdministrador = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]'
        botonConfirmarAdministrador = driver.until(ec.presence_of_element_located((By.XPATH, x_botonConfirmarAdministrador)))
        botonConfirmarAdministrador.click()
        print("El Grupo: ", groupName)
        print("Con el Docente: ",
              primerContacto)
        print("Contenia: ",
              cantidadIntegrantesDelGrupo)
        cell_range[contador][27].value = "ELIMINADO"
        cell_range[contador][28].value = primerContacto
        excel.save(
            'modulo3_enlaces_actualizado.xlsx')
        salirDelGrupo(driver, groupName)


def agregarPrimerContacto(driver, chrome, groupName, cell_range, contador, excel, action, cantidadIntegrantesDelGrupo, primerContacto):

    # Click para Desplegar las opciones de usuario = Asignar Admin // Eliminar
    button_nameFieldGroup = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/div[3]/div/div[9]/div/div/div[2]/div[2]/div[2]'
    button_nameFieldGroup = chrome.find_element(
        By.XPATH, button_nameFieldGroup)
    action.move_to_element(
        button_nameFieldGroup).perform()
    button_nameFieldGroup.click()

    # Elige AsignarAdmin
    x_botonAsignarAdministrador = '//*[@id="app"]/div[1]/span[4]/div/ul/div/li[1]'
    botonAsignarAdministrador = driver.until(
        ec.presence_of_element_located((By.XPATH, x_botonAsignarAdministrador)))
    botonAsignarAdministrador.click()
    
    try:
        # Extrae el texto de Asignar
        textoExtraidoDeAsignacion = str(
            x_botonAsignarAdministrador.get_attribute("textContent"))

        # Condiciona si el texto no es eliminar
        if(textoExtraidoDeAsignacion.strip() == "Eliminar" or textoExtraidoDeAsignacion[0].strip() == "E"):
            print("Ya Contiene Administrador")
            print("El Grupo: ", groupName)
            print("Con el Docente: ", primerContacto)
            print("Contenia: ",
                cantidadIntegrantesDelGrupo)
            cell_range[contador][27].value = "ELIMINADO"
            cell_range[contador][28].value = primerContacto
            excel.save(
                'modulo3_enlaces_actualizado.xlsx')
            salirDelGrupo(driver, groupName)

    except:
        x_botonConfirmarAdministrador = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]'
        botonConfirmarAdministrador = driver.until(ec.presence_of_element_located((By.XPATH, x_botonConfirmarAdministrador)))
        botonConfirmarAdministrador.click()
        print("El Grupo: ", groupName)
        print("Con el Docente: ", primerContacto)
        print("Contenia: ",
              cantidadIntegrantesDelGrupo)
        cell_range[contador][27].value = "ELIMINADO"
        cell_range[contador][28].value = primerContacto
        excel.save(
            'modulo3_enlaces_actualizado.xlsx')
        salirDelGrupo(driver, groupName)
