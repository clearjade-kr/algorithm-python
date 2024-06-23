class Solution:
    def reverseWords(self, s: str) -> str:
        list_substr = s.strip(" ").split()
        list_substr.reverse()
        return " ".join(list_substr)
