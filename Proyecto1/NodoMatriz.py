#Nodo que se encarga de obtener el nombre y las dimensiones
#la matriz 
class NodoMatriz:
    def __init__(self, matriz, n, m, valor):
        self.matriz = matriz
        self.n = n
        self.m = m
        #apuntadores
        self.valor = None #apuntador al contenido de la matriz correspondiente, aqui era valor
        self.next = None

