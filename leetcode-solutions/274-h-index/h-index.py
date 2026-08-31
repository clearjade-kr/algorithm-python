class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h-index : maximum number h
        # that at least h paper has been cited h times

        # Simple solution : find biggest number in citations.
        # For i in range(max_val, -1, -1), count each number of papers
        # that has been cited more than i times.

        # Another solution : sort citation.
        # Target : find x s.t max(cnt{i:i>=x} >= x)
        len_citation = len(citations)
        citations.sort()
        ans = 0
        flag = False
        for i in range(1, len_citation + 1):
            if i <= citations[len_citation - i]:
                ans = i
            else:
                flag = True
                break
        if ans == 0:
            return 0
        if not flag:
            return len_citation
        return ans