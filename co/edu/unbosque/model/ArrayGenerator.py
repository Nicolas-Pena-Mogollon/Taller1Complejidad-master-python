"""
Created on August 19,2023

@author: Nicolás Peña Mogollón - María Camila Lozano Gutiérrez
"""
import random


class ArrayGenerator:

    def __init__(self):
        pass

    def createRandomList(self, quantity):
        """
        Genera una lista de números aleatorios de acuerdo a la cantidad que se pida

        :param quantity: tamaño de la lista de número aleatorios
        :return: lista de números aleatorios
        """
        randomList = []
        for i in range(quantity):
            randomList.append(random.randint(0, quantity))
        return randomList

    def createAscendingList(self, quantity):
        """
        Genera una lista de números ordenados ascendentemente, de acuerdo a la cantidad que se pida

        :param quantity: tamaño de la lista
        :return: lista de números
        """
        array = []
        for i in range(quantity):
            array.append(i)
        return array

    def createDescendingList(self, quantity):
        """
        Genera una lista de números ordenados descendentemente, de acuerdo a la cantidad que se pida

        :param quantity: tamaño de la lista
        :return: lista de números
        """
        array = []
        for i in range(quantity, 0, -1):
            array.append(i)
        return array
