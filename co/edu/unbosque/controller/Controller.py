"""
Created on August 19,2023

@author: Nicolás Peña Mogollón - María Camila Lozano Gutiérrez
"""

from co.edu.unbosque.model.Sort import Sort
from co.edu.unbosque.view.View import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Sort()
        self.coordinateMenu()

    def coordinateMenu(self):
        """
        Coordina el menú de acuerdo a los datos de ingreso, primero pide el tipo de entrada, luego pide la cantidad
        de números a generar si se escogió números aleatorios o pide que se ingresen los números manuales y por
        último, el ingreso de la opción del tipo de algoritmo para ordenar

        :return: None
        """

        entry_option = "3"
        while entry_option != "0":
            array = self.manageOrderOption()
            if len(array) == 0:
                self.view.printData("Gracias!")
                break
            time_taken = self.manageSortOption(array)
            if time_taken == -1:
                entry_option = "0"

    def manageSortOption(self, numbers_array):
        """
        De acuerdo con la opción escogida para el algoritmo de ordenamiento, envia el array de números para que sea
        ordenado y lo regresa ya ordenado
        :param numbers_array: array ingresado
        :return: array ordenado de acuerdo al algoritmo de ordenamiento
        """
        sort_option = ""
        while sort_option != "0":
            sort_option = self.view.askSortOption()
            #  Opciones de ordenamiento
            if sort_option == "0":
                self.view.printData("Gracias!")
                return -1
            elif sort_option == "1":
                self.view.printData("Espere mientras se organizan los valores")
                self.view.printTime(self.model.doCocktailSort(numbers_array))
                return 0
            elif sort_option == "2":
                self.view.printData("Espere mientras se organizan los valores")
                self.view.printTime(self.model.quickSortTimer(numbers_array))
                return 0
            elif sort_option == "3":
                self.view.printData("Espere mientras se organizan los valores")
                self.view.printTime(self.model.doBinaryTreeSort(numbers_array))
                return 0
            else:
                self.view.printData("Opción incorrecta")

    def manageRandomNumOption(self):
        """
        Valida que al ingresar la opción de la longitud de los números aleatorios esta sea escogida para que se
        generen

        :return: opción escogida
        """
        rand_num_option = ""
        while rand_num_option != "0":
            rand_num_option = self.view.askNumberQuantity()
            if rand_num_option == "0":
                return 0
            elif rand_num_option == "1":
                return 3000
            elif rand_num_option == "2":
                return 30000
            elif rand_num_option == "3":
                return 300000
            elif rand_num_option == "4":
                return 3000000
            elif rand_num_option == "5":
                return 30000000
            else:
                self.view.printData("Opción incorrecta")

    def manageOrderOption(self):
        """
        Consulta el tipo de orden del arreglo a generar
        :return: Arreglo de los números en el orden solicitado
        """
        order_option = ""
        while order_option != "0":
            order_option = self.view.askNumbersOrder()

            if order_option == "0":
                return []
            elif order_option == "1":
                quantity = self.manageRandomNumOption()
                if quantity == 0:
                    return []
                print("Espere mientras se generan los números")
                return self.model.arrayGenerator.createAscendingList(quantity)
            elif order_option == "2":
                quantity = self.manageRandomNumOption()
                if quantity == 0:
                    return []
                print("Espere mientras se generan los números")
                return self.model.arrayGenerator.createDescendingList(quantity)
            elif order_option == "3":
                quantity = self.manageRandomNumOption()
                if quantity == 0:
                    return []
                print("Espere mientras se generan los números")
                return self.model.arrayGenerator.createRandomList(quantity)
            else:
                self.view.printData("Opción incorrecta")
