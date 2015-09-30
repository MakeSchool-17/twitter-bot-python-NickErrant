class DoubleNode:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class DoubleAssocNode(DoubleNode):
    def __init__(self, data=None, value=1, prev_node=None, next_node=None):
        super().__init__(data, prev_node, next_node)
        self.value = value

    def __str__(self):
        return str((self.data, self.value))


class DoublyLinkedList:
    def __init__(self, iterable=None, node_type=DoubleNode):
        self.node_type = node_type
        # set sentinel nodes
        head = node_type()
        tail = node_type()
        head.next_node = tail
        tail.prev_node = head
        self.head = head
        self.tail = tail
        #
        self.count = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __iter__(self):
        return self.forward_iterator()

    def __str__(self):
        return "["+", ".join(str(node) for node in self)+"]"

    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self._find(key) is not None

    def _insert_before(self, node, new_node):
        new_node.prev_node = node.prev_node
        new_node.next_node = node
        node.prev_node.next_node = new_node
        node.prev_node = new_node
        self.count += 1

    def _insert_after(self, node, new_node):
        new_node.next_node = node.next_node
        new_node.prev_node = node
        node.next_node.prev_node = new_node
        node.next_node = new_node
        self.count += 1

    def _find(self, key):
        current = self.head.next_node
        while current != self.tail:
            if current.data == key:
                return current
            current = current.next_node

    def _remove_node(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        node.next_node = None
        node.prev_node = None
        self.count -= 1

    def append(self, item):
        node = self.node_type(item)
        self._insert_before(self.tail, node)

    def prepend(self, item):
        node = self.node_type(item)
        self._insert_after(self.head, node)

    # only removes first instance of item found
    def remove(self, item):
        node_to_remove = self._find(item)
        if node_to_remove:
            self._remove_node(node_to_remove)

    def forward_iterator(self):
        current = self.head.next_node
        while current != self.tail:
            yield current
            current = current.next_node

    def backward_iterator(self):
        current = self.tail.prev_node
        while current != self.head:
            yield current
            current = current.prev_node


class HistogramWithDLL(DoublyLinkedList):
    def __init__(self, iterable=None):
        super().__init__(None, DoubleAssocNode)
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        node = self._find(item)
        if node:
            node.value += 1
        else:
            super().append(item)

    def frequency(self, item):
        node = self._find(item)
        if node:
            return node.value
        return 0

    def subtract(self, item):
        node = self._find(item)
        if node:
            node.value -= 1
            if node.value < 1:
                self._remove_node(node)


def main():
    pass

if __name__ == '__main__':
    main()
