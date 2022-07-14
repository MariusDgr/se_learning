"617. Merge Two Binary Trees"
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
        return None
    
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    
    r = TreeNode(v1 + v2)
    
    r.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    r.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    
    return r