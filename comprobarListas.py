from openpyxl import load_workbook

wb = load_workbook('modulo2-Completo.xlsx')
wb2 = load_workbook('modulo2.xlsx')
ws=wb['modulo2']
ws2=wb2['modulo2']
cell = ws['A2':'AP2469']
cell2 = ws2['A2':'O500']
cont=0
materiaFaltantes = 0

for x in range(0,len(cell2)):
    
    for c in range (0,len(cell)):
        # modulo                     ----Nombre                              || Grupo                               ||   Turno                                || Horario
        if(cell[c][1].value == '2' and cell2[x][3].value==cell[c][25].value and cell2[x][1].value==cell[c][3].value and cell2[x][5].value==cell[c][27].value and cell2[x][4].value==cell[c][26].value and cell[c][11].value == False):
            
            enlaceDeGrupo = cell2[x][11].value
            cell[c][39].value = "VIGENTE"
            cell[c][41].value = enlaceDeGrupo
            cont+=1

        elif(cell[c][1].value == '2' and cell2[x][3].value==cell[c][25].value and cell2[x][1].value==cell[c][3].value and cell2[x][5].value==cell[c][27].value and cell2[x][4].value==cell[c][26].value and cell[c][11].value == True):
            
            enlaceDeGrupo = cell2[x][11].value
            cell[c][40].value = "Contiene Grupo pero Fue Cerrado"
            cell[c][41].value = enlaceDeGrupo


        elif(cell[c][1].value == '2' and cell[c][11].value == True):
    
            cell[c][39].value = "CERRADO"

        elif(cell[c][1].value == '2' and cell[c][13].value == True):
    
            cell[c][39].value = "ANULADO"

        elif(cell[c][1].value == '2' and cell[c][28].value == "EXAMEN DE SUFICIENCIA"):
        
            cell[c][39].value = "NO REQUIERE GRUPO"

        elif(cell[c][1].value == '2' and cell[c][36].value == 'POSTGRADO'):
            
            cell[c][39].value = "NO REQUIERE GRUPO"
        
            
print(cont)
wb.save('modulo2-Completo.xlsx')