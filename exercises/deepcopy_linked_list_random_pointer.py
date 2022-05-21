"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy_hash_map = {None: None}
        
        current = head
        
        # build copies
        while current:
            copy = Node(current.val)
            copy_hash_map[current] = copy
            current = current.next
            
        # add pointers in copies
        current = head
        while current:
            copy = copy_hash_map[current]
            copy.next = copy_hash_map[current.next]
            copy.random = copy_hash_map[current.random]
            current = current.next
            
        return copy_hash_map[head]