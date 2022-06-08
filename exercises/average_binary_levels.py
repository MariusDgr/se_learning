"""637. Average of Levels in Binary Tree"""
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if root is None:
            return res
        
        que = []
        que.append(root)
        
        while len(que) > 0:
            level_sum = 0
            
            size = len(que)
            for i in range(size):
                current = que.pop(0)
                level_sum += current.val
                    
                if current.left is not None:
                    que.append(current.left)
                    
                if current.right is not None:
                    que.append(current.right)
            
            level_avg = level_sum / size
            res.append(level_avg)
        
        return res