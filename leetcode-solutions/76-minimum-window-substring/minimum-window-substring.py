class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        start, end = 0, 0
        ret = ""
        dict_count = defaultdict(int)
        for c in t:
            dict_count[c] += 1

        dict_target = defaultdict(int)
        flag_first = True
        while end < len(s):
            if flag_first:
                # move end to front till all char in t are in substr
                dict_target[s[end]] += 1
                end += 1
            else:
                next_end = s.find(s[start], end)
                if next_end != -1:
                    for i in range(end, next_end + 1):
                        dict_target[s[i]] += 1
                    end = next_end + 1
                else:
                    break

            if end - start < len(t):
                continue

            # check count of each char in t and target
            flag_check = True
            for c in t:
                if c not in dict_target or dict_target[c] < dict_count[c]:
                    flag_check = False
                    break

            if flag_check:
                while start < len(s):
                    if s[start] in dict_count and \
                            dict_count[s[start]] >= dict_target[s[start]]:
                        break
                    dict_target[s[start]] -= 1
                    start += 1

                if not ret or len(ret) > end - start:
                    ret = s[start: end]
                flag_first = False

        return ret