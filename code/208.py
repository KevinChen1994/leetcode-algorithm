# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/18 21:58

class Trie_1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_ = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.list_.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.list_

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.list_:
            if prefix == word[:len(prefix)]:
                return True
        return False


class Trie_2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    obj = Trie_2()
    word = 'apple'
    obj.insert(word)
    obj.insert('chen')
    param_2 = obj.search(word)
    prefix = 'app'
    param_3 = obj.startsWith(prefix)
    obj.insert('app')
