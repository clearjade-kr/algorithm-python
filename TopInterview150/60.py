import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # kth value in return string: 2** (k-1) count in remainder
        # n = 4, k = 9: 2314

        list_numbers = list(range(1, n + 1))
        ret_list = []

        # make k start from 0, not from 1
        k -= 1

        fact_val = math.factorial(n - 1)
        for i in range(n - 1, 0, -1):
            target_idx = k // fact_val
            ret_list.append(str(list_numbers.pop(target_idx)))

            # update k with remaining
            k %= fact_val

            # decrease factorial value with next repeat
            fact_val //= i

        ret_list.append(str(list_numbers[0]))
        return "".join(ret_list)


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 9
    print(sol.getPermutation(n=n, k=k))


