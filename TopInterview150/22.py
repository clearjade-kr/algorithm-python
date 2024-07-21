from typing import List


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#
#         def check_par(cur_str):
#             cnt_depth = 0
#             for i in cur_str:
#                 if i == '(':
#                     cnt_depth += 1
#                 else:
#                     cnt_depth -= 1
#                     if cnt_depth < 0:
#                         return False
#             return cnt_depth == 0
#
#         def dfs(cur_str:str, cnt_depth):
#             if len(cur_str) == n * 2:
#                 if check_par(cur_str):
#                     res.append(cur_str)
#                 return
#
#             cur_str += '('
#             cnt_depth += 1
#             dfs(cur_str, cnt_depth)
#             cnt_depth -= 1
#             cur_str = cur_str[:len(cur_str) - 1]
#
#             if cnt_depth > 0:
#                 cur_str += ')'
#                 cnt_depth -= 1
#                 dfs(cur_str, cnt_depth)
#                 cnt_depth += 1
#                 cur_str = cur_str[:len(cur_str) - 1]
#
#         dfs('', 0)
#         return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def genCombos(cnt_left_par, cnt_right_par, curr):
            if cnt_left_par == n and cnt_right_par == n:
                ret.append(curr)
            else:
                # When cnt_left_par is less than N
                if cnt_left_par < n:
                    genCombos(cnt_left_par + 1, cnt_right_par, curr + '(')

                # When cnt_right_par is less than cnt_left_par
                if cnt_right_par < cnt_left_par:
                    genCombos(cnt_left_par, cnt_right_par + 1, curr + ')')

        genCombos(0, 0, "")
        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
