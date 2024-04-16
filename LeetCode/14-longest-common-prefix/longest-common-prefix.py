class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur_prefix = strs[0]
        for cur_str in strs:
            if not cur_prefix:
                break
            for i in range(len(cur_prefix)):
                if i >= len(cur_str) or cur_prefix[i] != cur_str[i]:
                    cur_prefix = cur_str[:i]
                    break

        return cur_prefix