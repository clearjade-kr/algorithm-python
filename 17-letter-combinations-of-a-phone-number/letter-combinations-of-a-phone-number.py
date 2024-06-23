class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        list_combs = []
        for i in digits:
            if not list_combs:
                list_combs = [j for j in letter_map[i]]
            else:
                list_combs = [m + n for m in list_combs for n in letter_map[i]]
        return list_combs