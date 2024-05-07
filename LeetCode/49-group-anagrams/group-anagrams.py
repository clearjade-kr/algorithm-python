class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_sort = {}
        for s in strs:
            c = "".join(sorted(s))
            if c in dict_sort:
                dict_sort[c].append(s)
            else:
                dict_sort[c] = [s]

        return list(dict_sort.values())