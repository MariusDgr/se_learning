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