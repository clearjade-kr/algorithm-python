class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def check_par(cur_str):
            cnt_depth = 0
            for i in cur_str:
                if i == '(':
                    cnt_depth += 1
                else:
                    cnt_depth -= 1
                    if cnt_depth < 0:
                        return False
            return cnt_depth == 0

        def dfs(cur_str:str, cnt_depth):
            if len(cur_str) == n * 2:
                if check_par(cur_str):
                    res.append(cur_str)
                return

            cur_str += '('
            cnt_depth += 1
            dfs(cur_str, cnt_depth)
            cnt_depth -= 1
            cur_str = cur_str[:len(cur_str) - 1]

            if cnt_depth > 0:
                cur_str += ')'
                cnt_depth -= 1
                dfs(cur_str, cnt_depth)
                cnt_depth += 1
                cur_str = cur_str[:len(cur_str) - 1]

        dfs('', 0)
        return res