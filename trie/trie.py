from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.terminating = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.terminating

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
