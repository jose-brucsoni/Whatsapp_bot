from openpyxl  import Workbook
from openpyxl import load_workbook
from remove import remove

def extraerDatosDelExcel():
    #----------------------------------------------------------------------

    
    #Se Carga el archivo Excel --3
    excel_3 = load_workbook('modulo3_enlaces_actualizado.xlsx')
    #Selecciona la hoja dentro del excel --3
    ws_3 = excel_3['modulo3 - Filtrado']
    #Selecciona el rango de la tabla --3
    cell_range = ws_3['A2':'AA500']
    contador = -1
    arregloNombres = []
    arregloGrupo = []
    arregloHorario = []
    arregloSiglaMateria = []
    arregloTurno = []
    arregloModalidad = []
    arregloMateriaSinAbreviar = []
    arregloFilasDeExcel=[]



    for i in cell_range:
            contador += 1

            
            if(cell_range[contador][18].value == None and cell_range[contador][19].value == None and cell_range[contador][3].value != None):

                if(i[0].value != None):

                    
                    modalidad = cell_range[contador][5].value
                    turno = cell_range[contador][4].value
                    horario = cell_range[contador][7].value
                    materia = cell_range[contador][3].value
                    siglamateria = cell_range[contador][13].value
                    grupo = cell_range[contador][2].value

                    nombreAbreviado = remove.abreviar(materia, grupo)

                    arregloNombres.append(nombreAbreviado)
                    arregloGrupo.append(grupo)
                    arregloHorario.append(horario)
                    arregloSiglaMateria.append(siglamateria)
                    arregloTurno.append(turno)
                    arregloModalidad.append(modalidad)
                    arregloMateriaSinAbreviar.append(materia)
                    arregloFilasDeExcel.append(contador)


    return (arregloNombres,arregloGrupo,arregloHorario,arregloSiglaMateria,arregloTurno,arregloModalidad,arregloMateriaSinAbreviar,arregloFilasDeExcel)

