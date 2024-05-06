class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_st = {}
        dict_ts = {}
        for i in range(len(t)):
            if s[i] not in dict_st and t[i] not in dict_ts:
                dict_st[s[i]] = t[i]
                dict_ts[t[i]] = s[i]
            elif s[i] in dict_st and t[i] in dict_ts:
                if not (dict_ts[t[i]] == s[i] and dict_st[s[i]] == t[i]):
                    return False
            else:
                return False

        return True