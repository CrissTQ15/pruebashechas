import xml.etree.ElementTree as ET
from ListaMatrices import ListaMatrices
from ListaMatrizVal import ListaMatrizVal
from NodoMatrizContenido import NodoMatrizContenido

Matrices = ListaMatrices() #lista de matrices globales
def menu():
    while True:
        print("")
        print("Menu principal")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar grafica")
        print("6. Salir")
        opcion = input("Ingrese la opcion que desea: ")
        if opcion == "1":
            print(" ")
            print("1. Cargar Archivos")
            ruta = input("Ingrese la ruta del archivo: ")
            print(f"La ruta del archivo es: {ruta}")

        elif opcion == "2":
            print(" ")
            print("2. Procesar Archivos")
            ProcesarArchivo(ruta)
            Matrices.imprimirMatrices()
        elif opcion == "3":
            print(" ")
            print("3. Escribir Archivo de Salida")
        elif opcion == "4":
            print(" ")
            print("Mostrar datos del estudiante")
            print("Nombre: Cristian Gerardo Tun Quill")
            print("Carnet: 202300500")
            print("Curso: Introduccion a la Programacion y Computacion 2")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre 2024")
        elif opcion =="5":
            print(" ")
            print("5. generando grafica")
            Matrices.generarGrafica()
        elif opcion == "6":
            print(" ")
            print("Saliendo del programa, hasta pronto")
            break

def ProcesarArchivo(ruta):
    try:
        #analizando xml
        tree =ET.parse(ruta)
        root = tree.getroot() #obtener las matrices
        if root.tag != "matrices":
            raise ValueError("Error: El archivo no contiene la etiqueta matrices")
        matrices = root.findall("matriz")

        for matriz in matrices:
            nombre = matriz.get("nombre")
            n = int(matriz.get("n"))
            m = int(matriz.get("m"))
            datos = matriz.findall("dato")
            #}
            listaValores = ListaMatrizVal()
            #print(f"Matriz: {nombre} de dimensiones {n}x{m}")
            #

            for dato in datos:
                #print("añadienedo valores ")
                valor=int(dato.text) #creo que el problema surge aqui al no detectar el valor de las etiquetas <dato>
                x= int(dato.get("x"))
                y=int(dato.get("y"))
                listaValores.insertar(x,y,valor)

                if x<1 or x>n or y<1 or y>m:
                    print("error")
                    raise ValueError("Error: Las coordenadas de la matriz no son validas")
                    
                #else:
                    #print("Genial ")
                    #print("la matriz detectada contiene las dimensiones correctas ")
                    #lista_valores=ListaMatrizVal() #
                    #Matrices.valor = lista_valores
            Matrices.agregarMatriz(nombre,n,m,listaValores)    
                    
            #ListaMatrizVal.imprimirMatriz(listaValores)        
    except Exception as e: 
        print("")
        print("Surgio un error detectado por el try catch: ")
        print(e)   
        print(" ")

def escribirArchivoSalida():
    #ESCRIBIR LOS ARCHIVOS DE ENTRADAS COMO UNA MATRIZ DE SALIDA
    print("Escribiendo archivo de salida")
    
     

if __name__ == "__main__":
    menu()