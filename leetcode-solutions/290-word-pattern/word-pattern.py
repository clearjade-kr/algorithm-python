class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        dict_char = {}
        dict_word = {}
        for i in range(len(pattern)):
            if pattern[i] in dict_char:
                if dict_char[pattern[i]] != words[i]:
                    return False
            elif words[i] in dict_word:
                if dict_word[words[i]] != pattern[i]:
                    return False
            else:
                dict_char[pattern[i]] = words[i]
                dict_word[words[i]] = pattern[i]
        return True