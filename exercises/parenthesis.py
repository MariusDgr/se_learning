
# Backtrack
def generateParenthesis(self, n: int) -> List[str]:
    res = []
    
    def backtrack(s, open_count, close_count):
        if open_count < close_count or open_count > n or close_count > n:
            return

        if open_count == n and close_count == n:
            res.append(s)
        
        backtrack(s + "(", open_count + 1, close_count)
        backtrack(s + ")", open_count, close_count + 1)
        
    backtrack("(", 1, 0)
        
    return res

# iterative
from collections import deque
def generateParenthesis(self, n: int) -> List[str]:
    res = []
    parentheses_stack = deque()
    
    parentheses_stack.append(("(", 1, 0))
    
    while parentheses_stack:
        s, open_count, close_count = parentheses_stack.pop()
        
        if open_count < close_count or open_count > n or close_count > n:
            continue
        
        if open_count == n and close_count == n:
            res.append(s)
        
        parentheses_stack.append((s + "(", open_count + 1, close_count))
        parentheses_stack.append((s + ")", open_count, close_count + 1))
        
    return res