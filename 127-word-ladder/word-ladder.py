class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        bank = set(wordList)
        if endWord not in bank:
            return 0

        cnt_step = 1
        queue = deque([beginWord])
        while queue:
            cnt_step += 1
            for _ in range(len(queue)):
                cur_word = queue.popleft()
                for i in range(len(cur_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == cur_word[i]:
                            continue
                        new_word = cur_word[:i] + c + cur_word[i + 1:]
                        if new_word == endWord:
                            return cnt_step
                        if new_word in bank:
                            bank.remove(new_word)
                            queue.append(new_word)
        return 0
