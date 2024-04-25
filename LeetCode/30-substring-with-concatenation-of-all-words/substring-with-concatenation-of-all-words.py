class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        cnt_word = len(words)
        len_word = len(words[0])
        # count number of words for each word in [words]
        dict_count = {}
        for word in words:
            if word in dict_count:
                dict_count[word] += 1
            else:
                dict_count[word] = 1

        for i in range(len(s) - len_word * cnt_word + 1):
            dict_cur_count = {}
            substr = s[i : i + len_word * cnt_word]
            flag_check = True
            for j in range(0, len_word * cnt_word, len_word):
                cur_word = substr[j : j + len_word]
                if cur_word not in dict_count:
                    flag_check = False
                    break

                if cur_word in dict_cur_count:
                    dict_cur_count[cur_word] += 1
                else:
                    dict_cur_count[cur_word] = 1

            if not flag_check:
                continue
            flag_count = True
            for word in words:
                if word not in dict_cur_count \
                        or dict_count[word] != dict_cur_count[word]:
                    flag_count = False
                    break

            if flag_count:
                ret.append(i)
        return ret
