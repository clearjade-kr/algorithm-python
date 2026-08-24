from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        ret_list = [0] * N
        stack_idx = []

        for i in range(N):
            if not stack_idx:
                stack_idx.append(i)

            else:
                while stack_idx and temperatures[stack_idx[-1]] < temperatures[i]:
                    lower_idx = stack_idx.pop()
                    ret_list[lower_idx] = i - lower_idx
                stack_idx.append(i)

        return ret_list


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(sol.dailyTemperatures(temperatures=temperatures))
