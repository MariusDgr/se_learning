def hasCycle(self, head) -> bool:
    if head is None:
            return False
        
    node = head
    nodes = set([node])
    
    while node.next is not None:
        node = node.next
        if node in nodes:
            return True
        else:
            nodes.add(node)
        
    return False

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    new_head = None
    prev = None
    cur = head
    
    while cur:
        if cur.val == val:
            if prev:
                prev.next = cur.next
                
        else:
            if not new_head:
                new_head = cur

            prev = cur
        cur = cur.next
            
    return new_head

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

"""83. Remove Duplicates from Sorted List"""
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    if head is None or head.next is None:
        return head
    
    prev = head
    cur = head.next
    
    while cur:
        if cur.val == prev.val:
            prev.next = cur.next
            
        else:
            prev = cur
            
        cur = cur.next
        
    return head



def deleteDuplicatesHash(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    unique_vals = set()
    
    while cur:
        if cur.val in unique_vals:
            prev.next = cur.next
            
        else:
            unique_vals.add(cur.val)
            prev = cur
            
        cur = cur.next
        
    return head