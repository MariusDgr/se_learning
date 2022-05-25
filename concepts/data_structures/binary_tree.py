
class Node():
   def __init__(self, data=None):
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

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

            
    def _insert(self, val, cur_node):
        if val < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(val)
            else:
                self._insert(val, cur_node.left)

        elif val > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(val)
            else:
                self._insert(val, cur_node.right)

        else:
            print("Value already in tree")
    
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_h = self._height(cur_node.left, cur_height+1)
        right_h = self._height(cur_node.right, cur_height+1)
        return max(left_h, right_h)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.data:
            return True
        elif value < cur_node.data and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.data and cur_node.right is not None:
            return self._search(value, cur_node.right)
        return False
        
        
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

    def mirror_tree(self):
        if self.root is None:
            return None
        else:
            self._mirror_tree(self.root)

    def _mirror_tree(self, cur_node):
        if cur_node:
            aux = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = aux
            self._mirror_tree(cur_node.left)
            self._mirror_tree(cur_node.right)




if __name__ == "__main__":

    my_bst = BST()
    my_bst.insert(5)
    my_bst.insert(3)
    my_bst.insert(4)
    my_bst.insert(2)
    my_bst.insert(7)
    my_bst.insert(6)
    my_bst.insert(8)

    print("Inorder traversal: ", my_bst.inorder_traversal(my_bst.root))
    print()

    print("Preorder traversal: ", my_bst.preorder_traversal(my_bst.root))
    print()

    print("Postorder traversal: ", my_bst.postorder_traversal(my_bst.root))
    print()

    my_bst.mirror_tree()
    print("Mirrored inorder: ", my_bst.inorder_traversal(my_bst.root))
    print()




