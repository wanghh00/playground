# 208. Implement Trie (Prefix Tree)
# Implement a trie with insert, search, and startsWith methods.

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = {}
        self.isWord = False
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return

        cur = self
        for c in word:
            if c not in cur.dct:
                cur.dct[c] = Trie()
            cur = cur.dct[c]
        cur.isWord = True

    def helper(self, word):
        cur = self
        for c in word:
            cur = cur.dct.get(c)
            if not cur:
                break
        return cur

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.helper(word)
        return cur != None and cur.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.helper(prefix)
        return cur != None

        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

obj = Trie()
print obj.insert("apple"), obj.search("apple"), obj.search("app"), obj.startsWith("app")
print obj.insert("app"), obj.search("app")

