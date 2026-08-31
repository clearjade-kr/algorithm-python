class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if v.isdigit() or v.startswith('-') and v[1:].isdigit():
                stack.append(int(v))
            else:
                e, s = stack.pop(), stack.pop()
                if v == '+':
                    stack.append(s + e)
                elif v == '-':
                    stack.append(s - e)
                elif v == '*':
                    stack.append(s * e)
                else:
                    ret_val = s // e
                    if s * e < 0 and s % e != 0:
                        ret_val += 1
                    stack.append(ret_val)
        return stack[0]