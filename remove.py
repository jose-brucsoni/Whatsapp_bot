from blackList import blackList

class remove:

    def comprueba(cadena):
        if (len(cadena)<23):
            return True
        else:
            return False

    def abreviar(cadena,grupo):
        for i in blackList.List:
            cadena = cadena.replace(i, ' ')
        cadena = cadena.strip()
        cadenal = cadena.split(' ')

        if (remove.comprueba(cadena)):
            cadena == cadena.strip()
            cadenal = cadena.replace(' ','.')+'_'+grupo
            return cadenal
        else:
            for x in range(0,len(cadenal)):
                if (len(cadenal[x]) > 3):
                    cadenal[x] = cadenal[x][0:3]
                    if  (remove.comprueba('.'.join(cadenal))):
                        break
            cadenal = '.'.join(cadenal)+'_'+grupo
        return cadenal