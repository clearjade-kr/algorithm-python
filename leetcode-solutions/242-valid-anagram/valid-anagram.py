class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False

        if len(set(s)) != len(set(t)):
            return False

        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for i in range(len(s)):
            dict_s[s[i]] += 1
            dict_t[t[i]] += 1

        for k in dict_s:
            if k not in dict_t or dict_s[k] != dict_t[k]:
                return False
        return True