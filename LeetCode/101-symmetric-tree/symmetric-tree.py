class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        cur_list = [root]
        while cur_list:
            next_list = []
            flag_num = False
            for node in cur_list:
                if node:
                    flag_num = True
                    next_list.append(node.right)
                    next_list.append(node.left)
                else:
                    next_list.append(None)
                    next_list.append(None)

            if not flag_num:
                break

            if len(next_list) % 2 != 0:
                return False

            start, end = 0, len(next_list) - 1
            while start < end:
                if not (next_list[start] or next_list[end]):
                    start += 1
                    end -= 1
                    continue

                if not (next_list[start] and next_list[end]):
                    return False

                if next_list[start].val != next_list[end].val:
                    return False
                start += 1
                end -= 1

            cur_list = next_list

        return True
