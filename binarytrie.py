class BinaryTrie:
    """
    Trie that maps binary keys (in the form of non-negative ints) to values

    Keys must be a subset of the natural numbers (0, 1, 2, 3 ... n)
    Values can be anything

    The binary trie is basically a hybrid of a trie and a binary search tree

    @Instructors: Invented (more likely reinvented) this just for fun. I know
    it's not particularly practical, but it has some cool properties.

    Not too sure about space complexity, but I think it should be something
    like O(n*k), where n is the # of values stored and k is the average
    length of the binary representation of the keys.
    Can I say O(n*log(k)) where k is the average of the keys?

    WRT time complexity: I believe get, add, and remove are all Theta(log(n));
    where n is the key
    """

    def __init__(self, item_iter=None):
        self.binary_trie = [None, None, None]
        self._last_max_key = 0
        self._max_key = 0
        self._shifts = 0

    def __contains__(self, key):
        return self.get(key) is not None

    def __str__(self):
        return repr(self.binary_trie)

    def _get_shifts(self, key):
        shifts = 0
        while key != 0:
            key >>= 1
            shifts += 1
        return shifts

    def _set_max(self, key):
        self._last_max_key = self._max_key
        self._max_key = key
        shifts = self._get_shifts(key)
        if shifts != self._shifts:
            self._resize_trie(shifts - self._shifts)
            self._shifts = shifts

    def _resize_trie(self, step):
        trie = self.binary_trie
        times = abs(step)
        if step > 0:
            for _ in range(times):
                trie = [trie, None, None]
        elif step < 0:
            for _ in range(times):
                trie = trie[0]
        self.binary_trie = trie

    def get(self, key):
        if key > self._max_key:
            return None
        node = self.binary_trie
        depth = 1 << self._shifts
        while key & (depth - 1) != 0:
            direction = 1 if key & (depth >> 1) != 0 else 0
            if not node[direction]:
                return None
            node = node[direction]
            depth >>= 1
        return node[2]

    def add(self, key, value):
        if key > self._max_key:
            self._set_max(key)
        node = self.binary_trie
        depth = 1 << self._shifts
        while key & (depth - 1) != 0:
            direction = 1 if key & (depth >> 1) != 0 else 0
            if not node[direction]:
                node[direction] = [None, None, None]
            node = node[direction]
            depth >>= 1
        node[2] = value

    def remove(self, key):
        if key > self._max_key:
            return
        node = self.binary_trie
        last_filled = self.binary_trie
        last_dir = -1
        depth = 1 << self._shifts
        while key & (depth - 1) != 0:
            direction = 1 if key & (depth >> 1) != 0 else 0
            if not node[direction]:
                return
            elif node[2]:
                last_filled = node
                last_dir = direction
            node = node[direction]
            depth >>= 1
        if (not node[0]) and (not node[1]):
            last_filled[last_dir] = None
            self._set_max(self._last_max_key)


def main():
    # About those unit tests...
    iset = BinaryTrie()
    for i in range(1, 10):
        iset.add(i, i)
    print(iset)
    iset.add(0, 0)
    print(iset)
    print(iset.get(0))
    iset.remove(2)
    print(iset)
    print(iset.get(2))
    iset.remove(7)
    iset.remove(8)
    print(iset)
    print(iset.get(11))
    print(iset.get(8))
    iset.remove(9)
    print(iset)
    iset.add(100, 100)
    print(iset)
    print(iset.get(100), iset.get(99), iset.get(101))
    aset = BinaryTrie()
    aset.add(4, 4)
    print(aset)
    aset.remove(4)
    print(aset)
    aset.add(0, 0)
    aset.add(4, 4)
    aset.remove(4)
    print(aset)
    print(aset.get(0))


if __name__ == '__main__':
    main()
