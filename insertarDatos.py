from json import load
from typing import final
from openpyxl  import Workbook
from openpyxl import load_workbook


#Funcion para Insertar los datos en la hoja excel
def insertarDatosDelExcel(nombre,link,cont2):
    
    #Carga el Archivo Excel
    wb = load_workbook('modulo2.xlsx')
    #Carga la hoja del Archivo Excel
    ws = wb['modulo2']
    #Rango de la tabla
    cell_range = ws['A2':'M500']
    #Inserta los datos en la tabla
    # cell_range[cont2][12].value=link
    cell_range[cont2][11].value=nombre
    cell_range[cont2][12].value=link
    #Confirma el guardado de los datos en Excel
    wb.save('modulo2.xlsx')
