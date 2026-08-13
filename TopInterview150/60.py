import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # kth value in return string: 2** (k-1) count in remainder
        # n = 4, k = 9: 2314

        list_flags = [False] * n
        # Find ith value that has not been used
        def check_ith_not_used(i):
            cnt = 0
            for j in range(n):
                if list_flags[j]:
                    continue
                else:
                    cnt += 1
                    if cnt == i:
                        list_flags[j] = True
                        return j
            return -1

        def ret_string(remain, cur_str):
            if remain == 1:
                for i in range(n):
                    if list_flags[i]:
                        continue
                    list_flags[i] = True
                    cur_str += str(i + 1)
                return cur_str
            elif remain == 0:
                for i in range(n - 1, -1, -1):
                    if list_flags[i]:
                        continue
                    list_flags[i] = True
                    cur_str += str(i + 1)
                return cur_str
            divisor = math.factorial(n - 1 - len(cur_str))
            target_val = remain // divisor 
            next_remain = remain - target_val * divisor
            if next_remain > 0:
                target_val += 1
            target_idx = check_ith_not_used(target_val)
            return ret_string(remain = next_remain, cur_str = cur_str + str(target_idx + 1))

        return ret_string(k, "")


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 9
    print(sol.getPermutation(n=n, k=k))


