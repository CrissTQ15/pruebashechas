from  NodoMatriz import NodoMatriz 
import os 
import webbrowser
# #Clase que se encarga de almacenar las matrices en una lista
# esta es una lista circular

class ListaMatrices:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.size = 0 #tamaño de la lista

    #metodo que se encarga de insertar una matriz en la lista
    def agregarMatriz(self, matriz, n, m, listaValores):
        nuevaMatriz = NodoMatriz(matriz, n, m, listaValores) #crea un nuevo nodo de matriz con el nombre y las dimensiones
        nuevaMatriz.valor = listaValores #le asigna la lista de valores a la matriz, apuntando
        if self.cabeza is None: #si la lista de matrices esta vacia
            self.cabeza = nuevaMatriz 
            self.ultimo = nuevaMatriz
            self.ultimo.next = nuevaMatriz#modificado 04/09/24
            self.size += 1
            print("cabeza none, size: ",self.size)
        else:
            self.ultimo.next = nuevaMatriz #si la lista no esta vacia, se le asigna el nuevo nodo al ultimo nodo
            self.ultimo = nuevaMatriz #se actualiza el ultimo nodo
            self.ultimo.next = self.cabeza
            self.size += 1
            print("cabeza llena, size: ",self.size)
    
    def imprimirMatrices(self):
        #print(" ")
        auxiliar: NodoMatriz = self.cabeza
        print("Imprimiendo matrices, esta es la funcion imprimirmatrices")
        if self.cabeza is None:
            print("No hay matrices")          
        
        #auxiliar.valor.size
        for j in range(self.size):
            #extra el atributo de la matriz como nombre, filas y columnas
            print(" ")
            print("Tamaño: ",j,auxiliar.valor.size)
            print(f"----Matriz: {auxiliar.matriz}, filas: {auxiliar.n}, columnas: {auxiliar.m}")
            aux = auxiliar.valor.cabeza #revisa la lista de valores de la matriz
            
            while aux is not None:
                print(f"Valor: {aux.valor} en posicion X: {aux.posx} Y: {aux.posy}")
                #print("imprimiendo valores de la matriz")              
                aux = aux.next

            auxiliar = auxiliar.next

    