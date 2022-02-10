from json import load
from typing import final
from openpyxl  import Workbook
from openpyxl import load_workbook


def extraerDatosDelExcel(filas_ingresadas):
        
    excel = load_workbook('MATERIAS-1.xlsx')
    ws = excel['final']
    cantidad_de_filas = "J"+ str(filas_ingresadas)
    cell_range = ws['A2':cantidad_de_filas]
    filas_producto = ws['J2':'J39']
    arreglo = []

    contador = -1
    for i in filas_producto:
        contador += 1
        if(i[0].value != None):
            arreglo.append(cell_range[contador][9].value)
        else:
            arreglo = ""

    return arreglo

