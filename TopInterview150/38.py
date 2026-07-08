class Solution:
    def countAndSay(self, n: int) -> str:
        ret_str = "1"
        for _ in range(n - 1):
            cur_pointer = 0
            new_str = ""
            while cur_pointer < len(ret_str):
                cnt = 0
                cur_char = ret_str[cur_pointer]
                while cur_pointer < len(ret_str) and ret_str[cur_pointer] == cur_char:
                    cnt += 1
                    cur_pointer += 1
                
                new_str = new_str + str(cnt) + cur_char
            
            ret_str = new_str
                
        return ret_str


if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.countAndSay(n=n))
