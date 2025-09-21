# Linked list implementation.
# Use this file to understand how to do linked_list operations
class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data


class LinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, d=None):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove_node(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()

        return None


linkedList = LinkedList()
linkedList.add_node(1)
linkedList.add_node(2)
linkedList.add_node(3)
print(linkedList.find(2))
linkedList.remove_node(2)
print(linkedList.find(2))

# This should return 2 & None, because we show this node after adding it & after deleting it
