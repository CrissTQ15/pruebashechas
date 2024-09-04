#Nodo que contiene la posicion de la matriz y su valor


class NodoMatrizContenido:
    #guardar la matriz  ysu nombre
    #va tener apuntadores a la lista de datos de las matrices
    def __init__(self, posx, posy, valor):
        self.posx = posx
        self.posy = posy
        self.valor = valor
        #apuntadores
        self.next = None 
