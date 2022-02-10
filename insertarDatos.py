from json import load
from typing import final
from openpyxl  import Workbook
from openpyxl import load_workbook

wb = load_workbook('Modulo 1.xlsx')
ws = wb['Hoja1']

def insertarDatosDelExcel(nombre,link,cont2):
    
    cell_range = ws['A1':'K39']
    cell_range[cont2][9].value=link
    cell_range[cont2][10].value=nombre
    wb.save('Modulo 1.xlsx')
