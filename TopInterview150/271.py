from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            start_str = j + 1
            end_str = start_str + length
            result.append(s[start_str:end_str])
            
            i = end_str
            
        return result

    
if __name__ == "__main__":
    sol = Solution()
    s = [""]
    enc_s = sol.encode(strs=s)
    print(enc_s)
    dec_s = sol.decode(s=enc_s)
    print(dec_s)
