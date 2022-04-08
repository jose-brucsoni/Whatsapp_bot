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
import sesion as keepSession

with open('./resource/session.log','r') as f:
    sesion=f.read().split(',')
    id=sesion[0]
    url=sesion[1]
    print(id+url)
chrome = keepSession.openSession(id,url)
driver = WebDriverWait(chrome,600)

groupName = "SIMULACION.NEGOCIOS_FA"

x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
nameFieldGroup = driver.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
nameFieldGroup.clear()
chrome.implicitly_wait(10) # da una espera implícita de 10 segundos
nameFieldGroup.send_keys(groupName)
time.sleep(1)
nameFieldGroup.send_keys(Keys.ENTER)


#Click a Boton De 3 puntos
x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
buttonthreePoints = driver.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
buttonthreePoints.click()

time.sleep(1)

#Click en Info Grupo
x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
buttonInfoGrupo = driver.until(ec.presence_of_element_located((By.XPATH,x_InfoGrupoButton)))
buttonInfoGrupo.click()

time.sleep(1)


#Click integrantes
x_integrantesButton = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[1]/div/div/div[1]'
buttonintegrantes = driver.until(ec.presence_of_element_located((By.XPATH,x_integrantesButton)))
buttonintegrantes.click()

time.sleep(3)

celdaDeUsuario = './/div[@class="_3m_Xw"]//div[div[div[div[div[span[@data-testid="default-user"]]]]] and div[div[div[span[span[@title]]]]]]'
                    
# pscroll = chrome.find_element_by_xpath('//div[@class="nne8e"]//div[@class="_3Bc7H KPJpj"]')
# print("LLEGO AQUI")
# heightY = chrome.execute_script("return arguments[0].scrollHeight;",pscroll)
# print("hola horror0")
# for i in range (0,int((heightY/72)/17)+1):
#     print("hola horror")
#     busquedacelda=pscroll.find_elements_by_xpath('.//div[@class="_3m_Xw"]')
#     encontrado=False
#     busquedanombre='+'
#     for oso in busquedacelda:
#         try:
#             print("hola error")
#             busquedanombre= oso.find_element_by_xpath('.//div[div[div[div[div[span[@data-testid="default-user"]]]]] and div[div[div[span[span[@title]]]]]]//div[@class="zoWT4"]').get_attribute('textContent')
#         except:
#             print("espacio en blanco")
#         if (busquedanombre[0] != '+') or (busquedanombre!='Celular 2') or (busquedanombre!='Tú'):
#             print(str(busquedanombre))
#             print ("se encontro a docente")
#             oso.click()
#             admin=driver.until(ec.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/span[4]/div/ul/div/li[1]/div[1]')))
#             admin.click()
#             cerrarVentanaDeIntegrantes=driver.until(ec.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div/header/div/div[1]/button/span')))
#             cerrarVentanaDeIntegrantes.click()
#             #---------------------------------------------------------------------------------------
#             #Click en Salir del grupo
#             x_botonParaSalirDelGrupo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div[1]/div[2]/div/span'
#             botonParaSalirDelGrupo = driver.until(ec.presence_of_element_located((By.XPATH,x_botonParaSalirDelGrupo)))
#             botonParaSalirDelGrupo.click()

#             time.sleep(2)

#             #Click en confirmar salida
#             x_botonParaConfirmarSalidaDelGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div'
#             botonParaConfirmarSalidaDelGrupo = driver.until(ec.presence_of_element_located((By.XPATH,x_botonParaConfirmarSalidaDelGrupo)))
#             botonParaConfirmarSalidaDelGrupo.click()

#             time.sleep(4)

#             #Aqui empieza a Buscar el grupo
#             x_nameFieldGroup = '//*[@id="side"]/div[1]/div/label/div/div[2]'
#             nameFieldGroup = driver.until(ec.presence_of_element_located((By.XPATH,x_nameFieldGroup)))
#             nameFieldGroup.clear()
#             nameFieldGroup.send_keys(groupName)
#             nameFieldGroup.send_keys(Keys.ENTER)
#             #Click a Boton De 3 puntos
#             x_threePointsButton = '//*[@id="main"]/header/div[3]/div/div[2]/div/div'
#             buttonthreePoints = driver.until(ec.presence_of_element_located((By.XPATH,x_threePointsButton)))
#             buttonthreePoints.click()

#             time.sleep(2)

#             #Click en Info Grupo
#             x_InfoGrupoButton = '//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]'
#             buttonInfoGrupo = driver.until(ec.presence_of_element_located((By.XPATH,x_InfoGrupoButton)))
#             buttonInfoGrupo.click()
#             time.sleep(2)

#             #Click en Salir del grupo
#             x_botonEliminarGrupo = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[1]/div[2]/div/span'
#             botonEliminarGrupo = driver.until(ec.presence_of_element_located((By.XPATH,x_botonEliminarGrupo)))
#             botonEliminarGrupo.click()
#             time.sleep(2)

#             #Click  confirmar en Salir del grupo
#             x_botonConfirmarEliminacionDeGrupo = '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]'
#             botonConfirmarEliminacionDeGrupo = driver.until(ec.presence_of_element_located((By.XPATH,x_botonConfirmarEliminacionDeGrupo)))
#             botonConfirmarEliminacionDeGrupo.click()

#             #Confirma el guardado de los datos en Excel
            
#             print("El GRUPO: '", groupName,"', SE PUDO BORRAR")
#             encontrado=True
#             break
#     if encontrado == True:
#         break
#         # chrome.execute_script("arguments[0].scroll(0,arguments[1]);",pscroll,(i*1224))
#         # print("Aca termino")
#         # #driver.execute_script("arguments[0].scrollIntoView();",panel,)
#     cont=i*1224
#     chrome.execute_script("arguments[0].scroll(0,arguments[1]);",pscroll,cont)
print("hola")
pscroll = driver.until(ec.presence_of_element_located((By.XPATH,'//div[@class="nne8e"]//div[@class="_3Bc7H KPJpj"]')))
userlist = pscroll.find_element_by_xpath('.//div[@class="_3uIPm WYyr1" and @style]')
sizelist = chrome.execute_script("return arguments[0].scrollHeight;",userlist)
sizelist = int(sizelist/72)
for reco in range (0,sizelist):
    reco = reco*72
    try:
        print(reco)
        recoUserEle=userlist.find_element_by_xpath(f'.//div[@class="_3m_Xw" and contains(@style,"translateY({reco}px)")]')
        contUser= recoUserEle.find_element_by_xpath('.//div[div[div[div[div[span[@data-testid="default-user"]]]]] and div[div[div[span[@title]]]]]')
        nombreUser=contUser.find_element_by_xpath('.//span[@dir and @title and @class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"]')
        nombreUser=nombreUser.get_attribute("textContent")
    except:
        print("Contenedor vacio")
    else:
        if ("+" not in nombreUser) or ("Celular 2" not in nombreUser):
            print ("Docente encontrado:")
            print (nombreUser)
            break
        print("Buscando...." + nombreUser)
    finally:
        chrome.execute_script("arguments[0].scroll(0,arguments[1]);",pscroll,reco)