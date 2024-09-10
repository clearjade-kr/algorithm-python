class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowels = 'aeiouAEIOU'
        while start < end:
            while start < end and s[start] not in vowels:
                start += 1
            while start < end and s[end] not in vowels:
                end -= 1

            if start < end:
                s = s[:start] + s[end] + s[start + 1:end] + s[start] + s[end + 1:]
                start += 1
                end -= 1

        return s
