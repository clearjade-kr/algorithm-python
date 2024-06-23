from typing import List
from collections import defaultdict


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#
#         def dfs(node, i, j, path):
#             if node.isEnd:
#                 res.add(path)
#                 # node.isEnd = False
#
#             if i < 0 or i >= m or j < 0 or j >= n:
#                 return
#
#             tmp = board[i][j]
#             node = node.children.get(tmp)
#             if not node:
#                 return
#
#             board[i][j] = "#"
#             for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 dfs(node, i + x, j + y, path + tmp)
#             board[i][j] = tmp
#
#         class TrieNode:
#             def __init__(self):
#                 self.children = {}
#                 self.isEnd = False
#
#         class Trie:
#             def __init__(self):
#                 self.root = TrieNode()
#
#             def insert(self, word: str) -> None:
#                 cur_node = self.root
#                 for i in word:
#                     if i not in cur_node.children:
#                         cur_node.children[i] = TrieNode()
#                     cur_node = cur_node.children[i]
#                 cur_node.isEnd = True
#
#             def search(self, word: str) -> bool:
#                 cur_node = self.root
#                 for i in word:
#                     if i not in cur_node.children:
#                         return False
#                     cur_node = cur_node.children[i]
#                 return cur_node.isEnd
#
#             def startsWith(self, prefix: str) -> bool:
#                 cur_node = self.root
#                 for i in prefix:
#                     if i not in cur_node.children:
#                         return False
#                     cur_node = cur_node.children[i]
#                 return True
#
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
#
#         res = set()
#         m, n = len(board), len(board[0])
#         for i in range(m):
#             for j in range(n):
#                 dfs(trie.root, i, j, "")
#
#         return list(res)


def tree():
    return defaultdict(tree)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = tree()
        for word in words:
            t = trie
            for char in word:
                t = t[char]

            t[None] = word

        results = []

        m = len(board)
        n = len(board[0])

        def delete_word_from_trie(t, word):
            if word:
                delete_word_from_trie(t[word[0]], word[1:])
                if not t[word[0]]:
                    del t[word[0]]
            else:
                del t[None]

        def helper(y, x, curr_trie):
            char = board[y][x]
            if char in curr_trie:

                curr_trie = curr_trie[char]

                board[y][x] = "-"
                if None in curr_trie:
                    word = curr_trie[None]
                    results.append(word)

                    delete_word_from_trie(trie, word)
                if y > 0:
                    helper(y - 1, x, curr_trie)
                if y < m - 1:
                    helper(y + 1, x, curr_trie)

                if x > 0:
                    helper(y, x - 1, curr_trie)
                if x < n - 1:
                    helper(y, x + 1, curr_trie)

                board[y][x] = char

        for i in range(m):
            for j in range(n):
                helper(i, j, trie)

        return results
