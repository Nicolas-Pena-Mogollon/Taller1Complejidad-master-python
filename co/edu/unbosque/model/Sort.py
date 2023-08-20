"""
Created on August 19,2023

@author: Nicolás Peña Mogollón - María Camila Lozano Gutiérrez
"""
import time

from co.edu.unbosque.model.ArrayGenerator import ArrayGenerator
from co.edu.unbosque.model.BinaryTreeSort import BinaryTree


class Sort:
    def __init__(self):
        self.arrayGenerator = ArrayGenerator()
        self.binaryTree = BinaryTree()
        pass

    def quickSortTimer(self, arr):
        """
        Mide el tiempo de ejecución del algoritmo
        :param arr: lista de númerps
        :return: tiempo de ejecución
        """
        before_time = time.time()
        self.doQuickSort(arr)
        return time.time() - before_time

    def doQuickSort(self, arr):
        """
        Ordena el arreglo, dividiendolo en tres sub listas, donde el pivote es el primer número del arreglo.
        Las sublistas se llenan con los números menores que el pivote a la lista izquierda, mayores a la lista derecha
        e iguales a la lista centro, luego, hace una llamada recursiva con la lista de la izquierda y la derecha,
        concatenandolas con la del centro

        :param arr: array de números a ordenar
        :return: array de números ordenados
        """
        if len(arr) <= 1:
            return arr
        left = []
        equal = []
        right = []
        pivot = arr[int(len(arr) / 2)]

        for x in arr:
            if x > pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                right.append(x)

        right = self.doQuickSort(right)
        left = self.doQuickSort(left)

        final = right + equal + left
        return final

    def doCocktailSort(self, arr):
        """
        Realiza el ordenamiento de tipo Cocktail Sort en una lista de enteros.Itera
        desde el inicio hasta el final comparando elementos adyacentes. Intercambia
        los elementos si están desordenados. Itera desde el final hasta el inicio
        comparando los elementos y vuelve a intercambiar los valores si estan
        desordenados
        :param arr: Lista de números
        :return: tiempo de ejecución del algoritmo
        """
        before_time = time.time()
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble sort
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            # if nothing moved, then array is sorted.
            if not swapped:
                break

            # reduce the range of the next left-to-right pass
            end -= 1

            # loop from right to left, doing the same comparison
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            # increase the starting point for the next right-to-left pass
            start += 1
        return time.time() - before_time

    def doBinaryTreeSort(self, arr):
        """
        mide el tiempo de ejecución de arbol binario
        @param arr lista de números
        return
        :param arr: lista de números
        :return: tiempo de ejecución
        """
        root = None
        before_time = time.time()
        for item in arr:
            root = self.binaryTree.insert(root, item)

        self.binaryTree.in_order_traversal(root)
        return time.time() - before_time
