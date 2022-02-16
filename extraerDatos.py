from json import load
from typing import final
from openpyxl  import Workbook
from openpyxl import load_workbook
from remove import remove

def extraerDatosDelExcel():
    
        

    #----------------------------------------------------------------------

    #Se Carga el archivo Excel
    excel = load_workbook('modulo2.xlsx')
    #Selecciona la hoja dentro del excel
    ws = excel['modulo2']
    #Selecciona el rango de la tabla
    cell_range = ws['A2':'M500']
    contador = -1
    arregloNombres = []
    arregloGrupo = []
    arregloHorario = []
    arregloSiglaMateria = []
    arregloTurno = []
    arregloModalidad = []
    arregloMateriaSinAbreviar = []



    for i in cell_range:
            contador += 1
            if(i[0].value != None):

                modalidad = cell_range[contador][6].value
                turno = cell_range[contador][5].value
                horario = cell_range[contador][4].value
                materia = cell_range[contador][3].value
                siglamateria = cell_range[contador][2].value
                grupo = cell_range[contador][1].value

                nombreAbreviado = remove.abreviar(materia, grupo)

                arregloNombres.append(nombreAbreviado)
                arregloGrupo.append(grupo)
                arregloHorario.append(horario)
                arregloSiglaMateria.append(siglamateria)
                arregloTurno.append(turno)
                arregloModalidad.append(modalidad)
                arregloMateriaSinAbreviar.append(materia)


    return (arregloNombres,arregloGrupo,arregloHorario,arregloSiglaMateria,arregloTurno,arregloModalidad,arregloMateriaSinAbreviar)