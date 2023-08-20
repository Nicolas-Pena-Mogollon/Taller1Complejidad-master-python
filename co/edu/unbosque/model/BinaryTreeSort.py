"""
Created on August 19,2023

@author: Nicolás Peña Mogollón - María Camila Lozano Gutiérrez
"""
from co.edu.unbosque.model.TreeNode import TreeNode


class BinaryTree:
    def insert(self, root, key):
        """
        Crea un nuevo nodo con el valor dado y lo inserta en el árbol en relación al
        nodo actual. Si el nodo actual es nulo, se crea un nuevo nodo con el valor y
        se devuelve. Si el valor es menor que el valor actual del nodo, se llama al
        método recursivamente para el subárbol izquierdo; de lo contrario, para el
        subárbol derecho.

        :param root: raiz del arbol
        :param key: valor entrnate
        :return: raiz del arbol ordenado
        """
        if not root:
            return TreeNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.val:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.val:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def get_height(self, root):
        """
        Metodo que calcula la altura del nodo
        :param root: raiz del arbol
        :return: nodo y
        """
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        """
        Metodo que calcula el factor de balance del arbol
        :param root: raiz del arbol
        :return: nodo y
        """
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, z):
        """
        Realiza una rotación hacia la izquierda en el árbol con el nodo z como pivote.
        El nodo Y se convierte en el nuevo nodo raíz del subárbol, Z pasa a ser el hijo
        izquierdo. El antiguo hijo izquierdo de Y se convierte en el hijo derecho
        de Z. Se actualizan las alturas de z y y para mostrar los cambios, se devuelve
        y, que ahora es el nodo raíz del subárbol.

        :return: nodo y
        """
        if not z:
            return z  # Manejar el caso en que z es None

        y = z.right
        if not y:
            return z  # Manejar el caso en que y es None

        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, y):
        """
        Realiza una rotación hacia la derecha en el árbol con el nodo Y como pivote.
        El nodo X se convierte en el nuevo nodo raíz del subárbol y Y pasa a ser
        su hijo derecho. El antiguo hijo derecho de x se convierte en el nuevo hijo
        izquierdo de y. Luego, se actualizan las alturas de Y y X para mostrar los
        cambios y devuelver x como nuevo nodo raíz del subárbol.

        :param y: y
        """

        if not y:
            return y  # Manejar el caso en que y es None

        x = y.left
        if not x:
            return y  # Manejar el caso en que x es None

        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def in_order_traversal(self, root):
        """
        Realiza un recorrido en orden del árbol y devuelve una lista de valores en
        orden ascendente. Utiliza una pila para realizar el recorrido, comienza en la
        raíz y avanza hacia el nodo de la izquierda mientras apila apilandolos.
        Luego, desapila un nodo, agrega su valor a la lista resultante y se mueve al
        nodo derecho.
        :param root: raiz del nodo
        :return:lista ascendente
        """

        result = []
        if root:
            result += self.in_order_traversal(root.left)
            result.append(root.val)
            result += self.in_order_traversal(root.right)
        return result
