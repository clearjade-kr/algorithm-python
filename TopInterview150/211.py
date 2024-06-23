class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for i in word:
            if i not in cur_node.children:
                cur_node.children[i] = TrieNode()
            cur_node = cur_node.children[i]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.isEnd
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False

        return dfs(self.root, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)