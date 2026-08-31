class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(node, i, j, path):
            if node.isEnd:
                res.add(path)
                # node.isEnd = False

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return

            board[i][j] = "#"
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(node, i + x, j + y, path + tmp)
            board[i][j] = tmp

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

        trie = Trie()
        for word in words:
            trie.insert(word)

        res = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j, "")
                
        return list(res)
