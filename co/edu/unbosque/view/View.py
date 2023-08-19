"""
Created on Sept 6,2021

@author: Nicolás Peña Mogollón - María Camila Lozano Gutiérrez
"""


class View:
    def __init__(self):
        pass

    def askSortOption(self):
        """
        Pide el tipo de algoritmo de ordenamiento

        :return: opción del menú escogida
        """
        option = input(
            "Escoja el algoritmo que quiere usar\n0. Salir\n1. Cocktail Sort\n2. QuickSort\n3. Binary Tree Sort")
        return option

    def askNumberQuantity(self):
        """
        Pide la cantidad de números a generar en aleatorio

        :return: opción del menú escogida
        """
        option = input("Escoja la cantidad de numeros a generar\n0. Salir\n1. 3000\n2. 30000" +
                       "\n3. 300000 \n4. 3000000\n5. 30000000")
        return option

    def askNumbersOrder(self):
        """
        Pide el tipo de orden que se quiera usar

        :return: opción del menú escogida
        """
        option = input("¿Qué orden desea?\n0. Salir\n1. Ascendente\n2. Descendente" +
                       "\n3. Aleatorio")
        return option

    def printData(self, data):
        """
        Imprime la información ingresada

        :param data: la información a imprimir
        """
        print(data)

    def printTime(selfself, time):
        print("El tiempo obtenido fue: " + str(time))
