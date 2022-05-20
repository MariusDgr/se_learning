# TODO: work in progress 
"""
You are given a linked list where the node has two pointers.
The first is the regular next pointer. 
The second pointer is called arbitrary_pointer and it can point to any node in the linked list.
Your job is to write code to make a deep copy of the given linked list. 
Here, deep copy means that any operations on the original list (inserting, modifying and removing) should not affect the copied list.
"""
class Node():

    def __init__(self, data=None) -> None:
        self.data = data 
        self.next = None
        self.arbitrary = None


class LinkedListArb():

    def __init__(self, *args, **kwargs) -> None:
        if len(args) == 0:
            self.head = None
        else:
            in_list = args[0]
            self.head = Node(in_list[0])
            for el in in_list[1:]:
                self.append(el)

    def get_end(self):
        current = self.head
        prev = current
        while current is not None:
            prev = current
            current = current.next
        return prev

    def append(self, value):
        node = Node(value)
        last_node = self.get_end()
        if last_node == None:
            # case where this si the first node added
            self.head = node
            return
        last_node.next = node

    def get_as_list(self):
        sl_list = []
        current = self.head
        while current is not None:
            sl_list.append(current.data)
            current = current.next
        return sl_list

    def list_print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete_key(self, key):
        """
        Runtime complexity: O(n)
        Space complexity: O(1)
        """
        if self.head is None:
            return None

        current = self.head
        if current.data == key:
            self.head = current.next
            return current 
            
        while current is not None:
            if current.data == key:
                # delete node
                prev.next = current.next
                return current
            else:
                prev = current
                current = current.next

        return None


if __name__ == "__main__":

    newlist = SingleLinkedList()
    newlist.append(1)
    newlist.list_print()

    print()

    newlist = SingleLinkedList([1, 2, 4, 5])
    newlist.list_print()
    