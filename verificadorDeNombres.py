from openpyxl  import Workbook
from openpyxl import load_workbook
from remove import remove


#Se Carga el archivo Excel --3
excel_3 = load_workbook('modulo3_enlaces_actualizado.xlsx')
#Selecciona la hoja dentro del excel --3
ws_3 = excel_3['modulo3 - Filtrado']
#Selecciona el rango de la tabla --3
cell_range = ws_3['A2':'Z500']

contador = -1



for i in cell_range:
        contador += 1

        
        if(cell_range[contador][18].value != None and cell_range[contador][19].value != None):

            if(i[0].value != None):

                
                materia = cell_range[contador][3].value
                grupo = cell_range[contador][2].value

                nombreAbreviado = remove.abreviar(materia, grupo)

                if(cell_range[contador][19].value == nombreAbreviado):

                    cell_range[contador][25].value = "COINCIDE"
                else:
                    cell_range[contador][25].value = "NO COINCIDE"



#Confirma el guardado de los datos en Excel
excel_3.save('modulo3_enlaces_actualizado.xlsx')
