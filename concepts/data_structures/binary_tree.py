
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

    def is_equal(self, other_tree):
        if self.root is None and other_tree.root is None:
            return True
        else:
            return self._is_equal(self.root, other_tree.root)

    def _is_equal(self, node, other_node):

        if node is None and other_node is None:
            return True
            
        if node is not None and other_node is not None:
            return (node.data == other_node.data and
                self._is_equal(node.left, other_node.left) and
                self._is_equal(node.right, other_node.right))
  
        return False

    def hasPathSum1(self, targetSum):
        return self._hasPathSum1(self.root, targetSum, 0)
        
    def _hasPathSum1(self, node, targetSum, currentSum):
        if node is None:
            return False

        currentSum += node.data
        if node.left is None and node.right is None:
            return currentSum == targetSum
        
        return self._hasPathSum1(node.left, targetSum, currentSum) or self._hasPathSum1(node.right, targetSum, currentSum)

    def minDepth(self):
        return self._minDepth(self.root)

    def _minDepth(self, node) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        if node.left is None:
            return self._minDepth(node.right)+1

        if node.right is None:
            return self._minDepth(node.left) +1

        return min(self._minDepth(node.left), self._minDepth(node.right))+1

if __name__ == "__main__":

    my_bst = BST()
    for val in [5, 3, 4, 2, 7, 6, 8]:
        my_bst.insert(val)
    
    print("Inorder traversal: ", my_bst.inorder_traversal(my_bst.root))
    print()

    print("Preorder traversal: ", my_bst.preorder_traversal(my_bst.root))
    print()

    print("Postorder traversal: ", my_bst.postorder_traversal(my_bst.root))
    print()

    # my_bst.mirror_tree()
    # print("Mirrored inorder: ", my_bst.inorder_traversal(my_bst.root))
    # print()

    # other_tree1 = BST()
    # for val in [5, 3, 4, 2, 7, 6, 8]:
    #     other_tree1.insert(val)
    # print("Same tree answer: ", my_bst.is_equal(other_tree1))

    # other_tree2 = BST()
    # for val in [5, 3, 11, 2, 7, 6, 8]:
    #     other_tree2.insert(val)
    # print("Different tree answer: ", my_bst.is_equal(other_tree2))

    print()
    print(my_bst.hasPathSum1(10))

    print()
    print(my_bst.hasPathSum1(30))





