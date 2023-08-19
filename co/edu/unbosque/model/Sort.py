"""
Created on Sept 6,2021

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
        before_time = time.time()
        print(self.doQuickSort(arr))
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
        print(arr)
        return time.time() - before_time

    def doBinaryTreeSort(self, arr):
        before_time = time.time()
        print(self.binaryTree.binarySort(arr))
        return time.time() - before_time
