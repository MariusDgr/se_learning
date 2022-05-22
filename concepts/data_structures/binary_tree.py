
class Node():
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data


class BST():
    def __init__(self):
        self.root = None

    def print_tree(self) -> str:
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.data) + ' ')
            self._print_tree(node.right)

    def get_root(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
            
    def _add(self, val, node):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)

        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    # Inorder traversal
    # left -> root -> right
    def inorder_traversal(self, node):
        res = []
        if node:
            res = self.inorder_traversal(node.left)
            res.append(node.data)
            res = res + self.inorder_traversal(node.right)
        return res

    # Preorder traversal
    # root -> left -> right
    def preorder_traversal(self, node):
        res = []
        if node:
            res.append(node.data)
            res = res + self.preorder_traversal(node.left)
            res = res + self.preorder_traversal(node.right)

        return res

    # Postorder traversal
    # left -> right -> root
    def postorder_traversal(self, node):
        res = []
        if node:
            res = self.postorder_traversal(node.left)
            res = res + self.postorder_traversal(node.right)
            res.append(node.data)

        return res

if __name__ == "__main__":

    my_bst = BST()
    my_bst.add(1)
    my_bst.add(2)
    my_bst.add(3)
    my_bst.add(4)
    my_bst.add(5)


    print("Inorder traversal: ", my_bst.inorder_traversal(my_bst.root))
    print()

    print("Preorder traversal: ", my_bst.preorder_traversal(my_bst.root))
    print()

    print("Postorder traversal: ", my_bst.postorder_traversal(my_bst.root))




