from co.edu.unbosque.model.TreeNode import TreeNode


class BinaryTree:
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def in_order_traversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    def binarySort(self, arr):
        if not arr:
            return []

        root = TreeNode(arr[0])
        for i in range(1, len(arr)):
            self.insert(root, arr[i])

        result = self.in_order_traversal(root)
        return result