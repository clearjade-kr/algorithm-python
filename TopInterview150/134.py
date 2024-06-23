from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        len_circuit = len(gas)
        total_val = 0
        ans = 0
        cur_sum = 0
        for i in range(len_circuit):
            cur_sum += gas[i] - cost[i]
            if cur_sum < 0:
                total_val += cur_sum
                cur_sum = 0
                ans = i + 1

        total_val += cur_sum
        if total_val < 0:
            return -1
        return ans


if __name__ == "__main__":
    sol = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    # gas = [2,3,4]
    # cost = [3,4,3]
    print(sol.canCompleteCircuit(gas, cost))
