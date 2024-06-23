from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # ret = []
        # cnt_word = len(words)
        # len_word = len(words[0])
        # # count number of words for each word in [words]
        # dict_count = {}
        # for word in words:
        #     if word in dict_count:
        #         dict_count[word] += 1
        #     else:
        #         dict_count[word] = 1
        #
        # for i in range(len(s) - len_word * cnt_word + 1):
        #     dict_cur_count = {}
        #     substr = s[i : i + len_word * cnt_word]
        #     flag_check = True
        #     for j in range(0, len_word * cnt_word, len_word):
        #         cur_word = substr[j : j + len_word]
        #         if cur_word not in dict_count:
        #             flag_check = False
        #             break
        #
        #         if cur_word in dict_cur_count:
        #             dict_cur_count[cur_word] += 1
        #         else:
        #             dict_cur_count[cur_word] = 1
        #
        #     if not flag_check:
        #         continue
        #     flag_count = True
        #     for word in words:
        #         if word not in dict_cur_count \
        #                 or dict_count[word] != dict_cur_count[word]:
        #             flag_count = False
        #             break
        #
        #     if flag_count:
        #         ret.append(i)
        # return ret

        from collections import defaultdict
        word_length = len(words[0])
        number_of_words = len(words)
        total_length = word_length * number_of_words

        if total_length > len(s):
            return []

        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        results = []

        for start in range(word_length):
            seen_words = defaultdict(int)
            count = 0
            window_start = start

            for i in range(start, len(s) - word_length + 1, word_length):
                current_word = s[i:i+word_length]
                if current_word in word_count:
                    seen_words[current_word] += 1
                    count += 1

                    while seen_words[current_word] > word_count[current_word]:
                        left_word = s[window_start:window_start+word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        window_start += word_length

                    if count == number_of_words:
                        results.append(window_start)
                        left_word = s[window_start:window_start+word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        window_start += word_length
                else:
                    seen_words.clear()
                    count = 0
                    window_start = i + word_length

        return results


if __name__ == "__main__":
    sol = Solution()
    # s = "barfoothefoobarman"
    # words = ["foo","bar"]

    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]

    # s = "ababaab"
    # words = ["ab", "ba", "ba"]
    print(sol.findSubstring(s, words))
