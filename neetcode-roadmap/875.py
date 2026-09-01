from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile - 1) // speed + 1
            return hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    s = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    print(s.minEatingSpeed(piles, h))
