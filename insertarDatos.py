from json import load
from typing import final
from openpyxl  import Workbook
from openpyxl import load_workbook

#Carga el Archivo Excel
wb = load_workbook('Modulo 1.xlsx')
#Carga la hoja del Archivo Excel
ws = wb['Hoja1']

#Funcion para Insertar los datos en la hoja excel
def insertarDatosDelExcel(nombre,link,cont2):
    
    #Rango de la tabla
    cell_range = ws['J2':'K39']
    #Inserta los datos en la tabla
    cell_range[cont2][0].value=link
    cell_range[cont2][1].value=nombre
    #Confirma el guardado de los datos en Excel
    wb.save('Modulo 1.xlsx')
