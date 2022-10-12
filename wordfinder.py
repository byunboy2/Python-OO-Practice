import random


class WordFinder:

    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Initialize variables"""
        self.path = path
        self.words = []
        self.get_words()
        print (f"{len(self.words)} words read")

    def __repr__(self):
        """Display word count"""
        return f"There are {len(self.words)} words"

    def random(self):
        """Pick random word"""
        return random.choice(self.words)

    def get_words(self):
        """Parse file and populates words list"""
        with open(self.path) as file:
            for line in file:
                self.words.append(line.rstrip())
        file.close()
 """Filter for blank lines and #"""
class SpecialWordFinder(WordFinder):
    """Init"""
    def __init__ (self,path):
        super().__init__(path)

    def 