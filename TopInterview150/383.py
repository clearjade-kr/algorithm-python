class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # from collections import defaultdict
        # dict_mag = defaultdict(int)
        # dict_ransom = defaultdict(int)
        # for ch in magazine:
        #     dict_mag[ch] += 1
        #
        # for ch in ransomNote:
        #     dict_ransom[ch] += 1
        #
        # for ch in ransomNote:
        #     if dict_ransom[ch] > dict_mag[ch]:
        #         return False
        #
        # return True

        output = True
        for i in range(len(ransomNote)):
            if magazine.find(ransomNote[i]) == -1:
                output = False
                break
            else:
                magazine = magazine.replace(ransomNote[i], "", 1)
                output = True
        return output


if __name__ == "__main__":
    sol = Solution()
    ransomNote = ""
    magazine = ""
    print(sol.canConstruct(ransomNote, magazine))
