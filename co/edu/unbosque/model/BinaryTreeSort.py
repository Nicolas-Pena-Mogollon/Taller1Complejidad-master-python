from co.edu.unbosque.model.TreeNode import TreeNode


class BinaryTree:
    def insert(self, root, key):
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
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, z):
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
        result = []
        if root:
            result += self.in_order_traversal(root.left)
            result.append(root.val)
            result += self.in_order_traversal(root.right)
        return result
