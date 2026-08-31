class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur_msg = []

        for word in words:
            if len(" ".join(cur_msg)) + len(word) + 1 > maxWidth:
                if len(cur_msg) == 0:
                    cur_msg.append(word)
                    continue                
                elif len(cur_msg) == 1:
                    app_str = cur_msg[0].ljust(maxWidth)
                else:
                    # justify words in cur_msg
                    len_words = len("".join(cur_msg))
                    cnt_space = maxWidth - len_words
                    default_space = " " * (cnt_space // (len(cur_msg) - 1))
                    left_space = cnt_space - len(default_space) * (len(cur_msg) - 1)

                    app_str = ""
                    for i in range(len(cur_msg)):
                        app_str = app_str + cur_msg[i]
                        if i != len(cur_msg) - 1:
                            app_str = app_str + default_space
                            if left_space != 0:
                                app_str = app_str + " "
                                left_space -= 1

                ans.append(app_str)
                cur_msg = []

            cur_msg.append(word)

        if cur_msg:
            ans.append(" ".join(cur_msg).ljust(maxWidth))
        return ans
