class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowels = 'aeiouAEIOU'
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s = s[:start] + s[end] + s[start + 1:end] + s[start] + s[end + 1:]
                start += 1
                end -= 1
            if s[start] not in vowels:
                start += 1
            if s[end] not in vowels:
                end -= 1
        return s
