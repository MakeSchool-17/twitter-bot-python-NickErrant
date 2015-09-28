from collections import Counter
import re


class Histogram(Counter):
    def __init__(self, file_name):
        with open(file_name, "r") as corpus:
            word_arr = re.split("\W+", corpus.read())
            cleaned = [word.lower() for word in word_arr if not word == ""]
            super().__init__(cleaned)

    def unique_words(self):
        return len(super().keys())

    def frequency(self, word):
        return super().get(word.lower(), 0)


def main():
    gram = Histogram("Eastern_Standard_Tribe.txt")
    print("Unique words:", gram.unique_words())
    print("How many times does 'the' appear:", gram.frequency("the"))


if __name__ == '__main__':
    main()
