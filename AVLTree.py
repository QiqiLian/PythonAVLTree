from node import Node

class AVLTree:
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateRight(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)

        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search(root.right, key)

        return self.search(root.left, key)

    def printTree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key))
            self.printTree(root.left, level + 1, "L--- ")
            self.printTree(root.right, level + 1, "R--- ")


avl = AVLTree()
root = None
