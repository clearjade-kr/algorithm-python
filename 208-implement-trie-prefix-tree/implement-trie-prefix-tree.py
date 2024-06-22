class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for i in word:
            if i not in cur_node.children:
                cur_node.children[i] = TrieNode()
            cur_node = cur_node.children[i]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for i in word:
            if i not in cur_node.children:
                return False
            cur_node = cur_node.children[i]
        return cur_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for i in prefix:
            if i not in cur_node.children:
                return False
            cur_node = cur_node.children[i]
        return True