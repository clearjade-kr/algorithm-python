class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ? = any single char / * = any multiple char
        # two pointer approach with s index and p index
        # save star index and count of chars ingested with star
        # increase save count as we encounter mismatch

        s_index, p_index = 0, 0
        match_index = 0
        star_index = -1

        while s_index < len(s):
            # If current p char is ? or p char matches with s char
            if p_index < len(p) and (p[p_index] == '?' or p[p_index] == s[s_index]):
                p_index += 1
                s_index += 1

            # If p char is star - save current index and start with 0 match
            elif p_index < len(p) and p[p_index] == '*':
                star_index = p_index
                match_index = s_index
                p_index += 1

            # Mismatch found, but has star index before
            # Increase match index to 1 and start with match index again
            elif star_index != -1:
                p_index = star_index + 1
                match_index += 1
                s_index = match_index

            else:
                return False

        # Drop remaining star patterns
        while p_index < len(p) and p[p_index] == '*':
            p_index += 1

        return p_index == len(p)


if __name__ == "__main__":
    sol = Solution()
    # s = "aa"
    # p = "aa"
    # s = "adceb"
    # p = "*a*b"
    # s = "a"
    # p = "*"
    s = ""
    p = "*****"
    print(sol.isMatch(s = s, p = p))
