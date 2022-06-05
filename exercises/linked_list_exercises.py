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
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

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


"""21. Merge Two Sorted Lists"""


def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    blank = ListNode()
    end = blank

    while list1 and list2:
        if list1.val <= list2.val:
            end.next = list1
            list1 = list1.next
        else:
            end.next = list2
            list2 = list2.next
        end = end.next

    if list1:
        end.next = list1
    if list2:
        end.next = list2

    return blank.next


"""21. Merge Two Sorted Lists, My version for INPLACE"""


def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list2.val < list1.val:
        merged_h = list2
    else:
        merged_h = list1

    c1 = list1
    c2 = list2

    while c1 is not None and c2 is not None:
        if c2.val >= c1.val:
            c1, c2, br = self.merge_list(c1, c2)
            if br:
                break
        else:
            c1, c2, br = self.merge_list(c2, c1)
            if br:
                break

    return merged_h


def merge_list(self, c1, c2):
    br = False
    if c1.next is not None:
        if c2.val < c1.next.val:
            tmp = c2.next
            c2.next = c1.next
            c1.next = c2
            c2 = tmp
        else:
            c1 = c1.next
    else:
        c1.next = c2
        br = True
    return c1, c2, br
