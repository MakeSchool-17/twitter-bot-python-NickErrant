import sys
import string
from collections import defaultdict

word_to_anagram = sys.argv[1].lower()

alphabet = string.ascii_lowercase
binmap = {letter: 1 << index for (index, letter) in enumerate(alphabet)}


def to_alphaset(word):
    start = 0
    for char in word:
        start |= binmap.get(char, 0)
    return start


def main():
    anagram_dict = defaultdict(list)
    word_list = open("/usr/share/dict/words", "r").read().split("\n")
    for word in word_list:
        fixed_word = word.lower()
        anagram_dict[to_alphaset(fixed_word)].append(fixed_word)
    possible = anagram_dict.get(to_alphaset(word_to_anagram), [])
    sorted_gram = sorted(word_to_anagram)
    anagrams = [word for word in possible if sorted(word) == sorted_gram]
    print("\n".join(anagrams))


if __name__ == '__main__':
    main()
