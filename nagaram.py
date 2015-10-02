class Anagram_Dict:

    def __init__(self, dict_file):
        self.index = 0
        self.search_list = [None, None]
        # alphabet ordered by frequency in english
        self._alphabet = ["z", "j", "q", "x", "k", "v", "b", "p", "g", "w",
                          "y", "f", "m", "c", "u", "l", "d", "h", "r", "s",
                          "n", "i", "o", "a", "t", "e"]
        self._binmap = {letter: 1 << i
                        for (i, letter)
                        in enumerate(self._alphabet)}
        with open(dict_file, "r") as corpus:
            self.words = corpus.read().split()
        for word in self.words:
            self.add(word.lower())

    def _to_bitset_key(self, word):
        bit_set = 0
        for char in word:
            bit_set |= self._binmap.get(char, 0)
        return bit_set

    def add(self, word):
        compact = self._to_bitset_key(word)
        current = self.search_list
        letter_index = 1 << 25
        while compact & (letter_index - 1) != 0:
            direction = 1 if letter_index & compact != 0 else 0
            if not current[direction]:
                current[direction] = [None, None]
            current = current[direction]
            letter_index >>= 1
        if len(current) == 2:
            current.append([self.index])
        else:
            current[2].append(self.index)
        self.index += 1

    def _get_bucket(self, word):
        if word == "":
            return []
        compact = self._to_bitset_key(word)
        current = self.search_list
        letter_index = 1 << 25
        while compact & (letter_index - 1) != 0:
            direction = 1 if letter_index & compact != 0 else 0
            if not current[direction]:
                return []
            current = current[direction]
            letter_index >>= 1
        return current[2]

    def get_anagrams(self, word):
        possible = []
        for index in self._get_bucket(word.lower()):
            possible.append(self.words[index])
        sorted_word = sorted(word.lower())
        return [x for x in possible if sorted(x.lower()) == sorted_word]


def main():
    a = Anagram_Dict("/usr/share/dict/words")
    print(a.get_anagrams(""))
    print(a.get_anagrams("a"))
    print(a.get_anagrams("huyhjkjg"))
    print(a.get_anagrams("orb"))


if __name__ == '__main__':
    main()
