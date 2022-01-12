"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """
    Class for choosing a random word from a dictionary

    >>> n = WordFinder('words.txt')
    235886 words read
    """

    def __init__(self, file):
        """Read a file and return the number of words"""
        dict_file = open(file)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Create a list of words from read file"""
        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word from read file"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    >>> n = SpecialWordFinder('words2.txt')
    4 words read
    """

    def parse(self, dict_file):
        """Create a list of words from read file, ignoring blanks and comments"""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]
