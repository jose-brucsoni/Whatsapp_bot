from openpyxl  import Workbook
from openpyxl import load_workbook


#Funcion para Insertar los datos en la hoja excel
def insertarDatosDelExcel(nombre,link,filadeExcelAinsertar):
    
    #Carga el Archivo Excel
    wb = load_workbook('modulo2.xlsx')
    #Carga la hoja del Archivo Excel
    ws = wb['modulo2']
    #Rango de la tabla
    cell_range = ws['A2':'M500']

    cell_range[filadeExcelAinsertar][11].value=link
    cell_range[filadeExcelAinsertar][12].value=nombre

        
    #Confirma el guardado de los datos en Excel
    wb.save('modulo2.xlsx')
