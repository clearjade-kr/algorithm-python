class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Each child must have at least one candy.
        # Children with a higher rating get more candies than their neighbors.

        list_candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                list_candy[i] = list_candy[i - 1] + 1

        for i in range(len(ratings) -1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                list_candy[i - 1] = max(list_candy[i - 1], list_candy[i] + 1)

        # print(list_candy)
        return sum(list_candy)