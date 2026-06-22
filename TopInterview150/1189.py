from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict_cnt = defaultdict(int)
        letters_in_balloon = 'balon'
        
        for letter in text:
            if letter in letters_in_balloon:
                dict_cnt[letter] += 1

        letter_max_cnt = len(text) // 7
        for letter in letters_in_balloon:
            current_max = 0
            if letter in 'lo':
                current_max = dict_cnt[letter] // 2
            else:
                current_max = dict_cnt[letter]

            letter_max_cnt = min(letter_max_cnt, current_max)

        # print(letter_max_cnt)
        return letter_max_cnt



if __name__ == "__main__":
    sol = Solution()
    test_str = 'loonbalxballpoon'
    sol.maxNumberOfBalloons(test_str)