class SortedLinkedList():
    def __init__(self, iterable=None):
        self.head = None
        self.count = 0
        if iterable:
            for item in iterable:
                self.add(item)

    def _insert(self, prev_node, new_node):
        new_node.next_node = prev_node.next_node
        prev_node.next_node = new_node

    def add(self, item):
        self.count += 1
        new_node = Node(item)
        current = self.head
        if (not current) or new_node.data < current.data:
            new_node.next_node = current
            self.head = new_node
            return
        last = current
        while current.next_node:
            current = current.next_node
            if new_node.data <= current.data:
                break
            last = current
        self._insert(last, new_node)

    def remove(self, item):
        current = self.head
        if current.data == item:
            self.head = current.next_node
            del current
            self.count -= 1
            return
        last = current
        while current.next_node:
            current = current.next_node
            if current.data == item:
                break
            last = current
        else:
            return
        last.next_node = current.clear()
        self.count -= 1

    def __iter__(self):
        self._curr_node = self.head
        return self

    def __next__(self):
        current = self._curr_node
        if not current:
            raise StopIteration
        self._curr_node = current.next_node
        return current

    def __str__(self):
        return "["+", ".join(str(node) for node in self)+"]"

    def __len__(self):
        return self.count


class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def clear(self):
        link = self.next_node
        self.next_node = None
        return link

    def __str__(self):
        return str(self.data)


def main():
    ll = SortedLinkedList()
    ll.add(6)
    ll.add(1)
    ll.add(3)
    ll.add(2)
    print(ll, len(ll))
    ll.remove("l")
    ll.remove(1)
    print(ll, len(ll))
    ll.remove(3)
    print(ll)
    ll.remove(6)
    print(ll)
    print(SortedLinkedList(["lol", "a", "gt"]))

if __name__ == '__main__':
    main()
