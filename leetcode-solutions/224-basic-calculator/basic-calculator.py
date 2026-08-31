class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        def readInt(s: str, cur_idx: int) -> (int, int):
            while cur_idx < len(s) and s[cur_idx] == ' ' or s[cur_idx] == '(':
                cur_idx += 1

            flag_negative = False
            if s[cur_idx] == '-':
                flag_negative = True
                cur_idx += 1

            start_idx = cur_idx
            while cur_idx < len(s) and s[cur_idx].isdigit():
                cur_idx += 1

            ret_val = int(s[start_idx:cur_idx])
            if flag_negative:
                ret_val *= -1

            return ret_val, cur_idx

        def operate(a:int, b:int, operator: str) -> int:
            if operator == '+':
                return a + b
            else:
                return a - b

        cur_idx = 0
        cur_val = 0
        cur_op = ''
        while cur_idx < len(s):
            if s[cur_idx] == ' ':
                cur_idx += 1
                continue
            elif s[cur_idx] in '+-':
                # Current operator
                # get next operand
                cur_op = s[cur_idx]
                cur_idx += 1
            elif s[cur_idx] == '(':
                # if next operand is ( -> put cur_val and operator into stack
                if cur_op:
                    stack.append((cur_val, cur_op))
                    cur_op = ''
                    cur_val = 0
                cur_idx += 1
            elif s[cur_idx] == ')':
                # pop in stack and calculate, have it as current value
                if stack:
                    prev_val, prev_op = stack.pop()
                    cur_val = operate(prev_val, cur_val, prev_op)
                cur_idx += 1
            else:
                # integer, if cur_op: calculate with cur_val. else, save cur_val
                next_operand, cur_idx = readInt(s, cur_idx)
                if cur_op:
                    cur_val = operate(cur_val, next_operand, cur_op)
                else:
                    cur_val = next_operand

        while stack:
            prev_val, prev_op = stack.pop()
            cur_val = operate(prev_val, cur_val, prev_op)

        return cur_val