import random


class WordFinder:

    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Initialize instance with a given path and populate words list"""
        print("WordFinder __init__")
        self.path = path
        self.words = self.get_words()
        print (f"{len(self.words)} words read")

    def __repr__(self):
        """Display word count of instance"""
        print("WordFinder __repr__")
        return f"There are {len(self.words)} words"

    def random(self):
        """Pick random word from list of words"""
        print("WordFinder random")
        return random.choice(self.words)

    def get_words(self):
        """Parse file and populates words list"""
        print("WordFinder get_words")
        words = []
        with open(self.path) as file:
            for line in file:
                words.append(line.rstrip())
        file.close()
        return words

"""Filter for blank lines and #"""
class SpecialWordFinder(WordFinder):
    """Initialize instance with a given path and populate words list"""
    
    #only need __init__ if new params

    def get_words(self):
        """Parse file and populates words list"""
        print("SpecialWordFinder get_words")
        words = super().get_words()
        return [word for word in words if len(word)!=0 and word[0]!='#']