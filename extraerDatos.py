from json import load
from typing import final
from openpyxl  import Workbook
from openpyxl import load_workbook


def extraerDatosDelExcel(filas_ingresadas):
        
    #Se Carga el archivo Excel
    excel = load_workbook('MATERIAS-1.xlsx')
    #Selecciona la hoja dentro del excel
    ws = excel['final']
    #Se elige la cantidad de filas a trabajar
    cantidad_de_filas = "J"+ str(filas_ingresadas)
    #Selecciona el rango de la tabla
    cell_range = ws['A2':cantidad_de_filas]
    #Selecciona la columna
    filas_producto = ws['J2':'J39']
    #Variable array para devolver los resultados de la columna
    arreglo = []

    contador = -1
    for i in filas_producto:
        contador += 1
        if(i[0].value != None):
            #Se añade los datos al array devuelto
            arreglo.append(cell_range[contador][9].value)
        else:
            arreglo = ""

    return arreglo

