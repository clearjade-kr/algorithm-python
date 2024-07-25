class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # print("m:", bin(m))
        # print("n:", bin(n))
        return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if m < n else m