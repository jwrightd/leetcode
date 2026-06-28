class WordDictionary(object):
    # okay so we definitely need some hashset to store our words
    # trick is the words with '.' 
    # how to handle this?
    # i have an idea, how about we just add all possible "." when we add a word?
    # is there anyhting better?
    # maybe like trie?
    # let's set it up as so: * at end of word, at every node we add "." as we are processing each letter
    def __init__(self):
        self.trie = dict()

    def addWord(self, word):
        #two branches per letter, the letter and '.'
        #Let's trace out adding "hi"

        # we want first level to have "h" and "."
        # second level to have "i" and "."
        length = len(word)
        node = self.trie
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["*"] = {}
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length = len(word)
        def recur(node, word, idx):
            if idx == length:
                return "*" in node
            current = word[idx]
            if current == ".":
                results = []
                for possibility in node:
                    if recur(node[possibility], word, idx + 1):
                        return True
                return False
            else:
                if current not in node:
                    return False
                return recur(node[current], word, idx + 1)
        return recur(self.trie, word, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
