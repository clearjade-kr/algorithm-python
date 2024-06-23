from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h-index : maximum number h
        # that at least h paper has been cited h times

        # Simple solution : find biggest number in citations.
        # For i in range(max_val, -1, -1), count each number of papers
        # that has been cited more than i times.

        # Another solution : sort citation.
        # Target : find x s.t max(cnt{i:i>=x} >= x)

        # -- My previous solution --
        # len_citation = len(citations)
        # citations.sort()
        # ans = 0
        # flag = False
        # for i in range(1, len_citation + 1):
        #     if i <= citations[len_citation - i]:
        #         ans = i
        #     else:
        #         flag = True
        #         break
        # if ans == 0:
        #     return 0
        # if not flag:
        #     return len_citation
        # return ans

        # -- Cleaner solution found --
        # Same approach, but sorting reverse and using enumerate
        citations.sort(reverse=True)

        h_index = 0
        for i, citation in enumerate(citations, start=1):
            if citation >= i:
                h_index = i
            else:
                break

        return h_index



if __name__ == "__main__":
    sol = Solution()
    citations = [3,0,6,1,5]
    # citations = [0,1,4,5,6]
    # citations = [0,1,99,106,112]
    # citations = [11,15]
    # citations = [1,1,3]
    # citations = [0]
    print(sol.hIndex(citations))
