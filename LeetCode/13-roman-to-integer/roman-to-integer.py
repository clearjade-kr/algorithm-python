class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        # dict_roman[char] = (size,
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            if s[i] == 'I':
                if i != len(s) - 1 and s[i + 1] in 'VX':
                    res -= dict_roman[s[i]]
                else:
                    res += dict_roman[s[i]]
            elif s[i] == 'X':
                if i != len(s) - 1 and s[i + 1] in 'LC':
                    res -= dict_roman[s[i]]
                else:
                    res += dict_roman[s[i]]
            elif s[i] == 'C':
                if i != len(s) - 1 and s[i + 1] in 'DM':
                    res -= dict_roman[s[i]]
                else:
                    res += dict_roman[s[i]]
            else:
                res += dict_roman[s[i]]

        return res
