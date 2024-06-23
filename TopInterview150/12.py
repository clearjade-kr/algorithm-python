class Solution:
    def intToRoman(self, num: int) -> str:
        dict_roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        ans = ''
        keys = sorted(dict_roman.keys(), reverse=True)
        for v in keys:
            if num >= v:
                cnt_v = num // v
                ans = ans + (dict_roman[v] * cnt_v)
                num -= v * cnt_v
        return ans


if __name__ == "__main__":
    sol = Solution()
    num = 1994
    print(sol.intToRoman(num))
