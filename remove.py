from cgitb import text
from blackList import blackList

class remove:
    def abreviar(cadena, grupo):
        for i in blackList.List:
            cadena = cadena.replace(i, ' ')

        cadenal = cadena.split(' ')
        if (len(cadena)<23):
            cadena = cadena+'_'+grupo

        else:
            cont=-1
            for a in cadenal:
                cont+=1
                if (len(a) > 3):
                    cadenal[cont] = a[0:3]


        retorna = '.'.join(cadenal)+'_'+grupo
        return retorna
