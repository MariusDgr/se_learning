def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
    def dfs(root): 
        nonlocal diameter
        if root is None: 
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        
        diameter = max(left + right, diameter)
        
        return max(left, right) + 1
        
                
    diameter = 0
    dfs(root)
    return diameter