from NodoMatrizContenido import NodoMatrizContenido

class ListaMatrizVal:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.size = 0


    def insertar(self, posx, posy,valor): #valor estaba primero 
        nuevaMatriz= NodoMatrizContenido(posx, posy,valor)
        if self.cabeza is None:
            self.cabeza = nuevaMatriz
            self.ultimo = nuevaMatriz
            self.size += 1
        else:
            self.ultimo.next = nuevaMatriz
            self.ultimo = nuevaMatriz
            self.size += 1

        #print(self.size)

    def imprimirMatriz(self):
        auxiliar: NodoMatrizContenido = self.cabeza
        for envio in range(self.size):
            print(f"Posicion X:{auxiliar.posx} Posicion Y:{auxiliar.posy} Valor:{auxiliar.valor}") #imprime el valor cada elemento de la matriz
            auxiiliar = auxiliar.next
