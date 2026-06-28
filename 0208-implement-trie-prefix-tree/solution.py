class Trie(object):

    def __init__(self):
        self.trie = {}
        #finish word with "*"

    def insert(self, word):
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
        node = self.trie
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "*" in node
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.trie
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return len(node) > 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
