from traceback import print_tb
from openpyxl import load_workbook
import time

wb = load_workbook('modulo2.xlsx')
wb2 = load_workbook('modulo2 v2.xlsx')
ws=wb['modulo2']
ws2=wb2['Hoja1']
cell = ws['A2':'O500']
cell2 = ws2['A2':'Y443']
cont=0
materiaFaltantes = 0

for x in range(0,len(cell2)):
    #a=cell2[x][11].value+cell2[x][3].value
    
    for c in range (0,len(cell)):
        #print(a)
        if(cell2[x][11].value==cell[c][3].value and cell2[x][3].value==cell[c][1].value and cell2[x][13].value==cell[c][5].value and cell2[x][14].value==cell[c][6].value ):
            print("verdadero")
            print(cell2[x][11].value + ' ' + cell2[x][3].value + ' == ' +  cell[c][3].value + ' ' + cell[c][1].value)
            codigoDeMateria = cell2[x][2].value
            cell[c][13].value = codigoDeMateria
            cell[c][14].value = "Encontrado"
            cont+=1
        
            
print(cont)
wb.save('modulo2.xlsx')