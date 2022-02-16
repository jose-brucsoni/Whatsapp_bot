
def abreviacionParaNombre(materia,horario,grupo):

    inicialesMateria = "".join([palabra[0] for palabra in materia.split()])
    abreviacionFinal = inicialesMateria+ "-" + horario + "-" + grupo
    return abreviacionFinal