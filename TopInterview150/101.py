from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None or (root.right == None and root.left == None):
            return True
        return self.check_sub(root.left, root.right)


    def check_sub(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        if left.val != right.val:
            return False

        return self.check_sub(left.left, right.right) and self.check_sub(left.right, right.left)


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#
#         cur_list = [root]
#         while cur_list:
#             next_list = []
#             flag_num = False
#             for node in cur_list:
#                 if node:
#                     flag_num = True
#                     next_list.append(node.right)
#                     next_list.append(node.left)
#                 else:
#                     next_list.append(None)
#                     next_list.append(None)
#
#             if not flag_num:
#                 break
#
#             if len(next_list) % 2 != 0:
#                 return False
#
#             start, end = 0, len(next_list) - 1
#             while start < end:
#                 if not (next_list[start] or next_list[end]):
#                     start += 1
#                     end -= 1
#                     continue
#
#                 if not (next_list[start] and next_list[end]):
#                     return False
#
#                 if next_list[start].val != next_list[end].val:
#                     return False
#                 start += 1
#                 end -= 1
#
#             cur_list = next_list
#
#         return True


if __name__ == "__main__":
    tn1 = TreeNode(val=3)
    tn2 = TreeNode(val=4)
    tn3 = TreeNode(val=4)
    tn4 = TreeNode(val=3)

    tn5 = TreeNode(val=2, left=tn1, right=tn2)
    tn6 = TreeNode(val=2, left=tn3, right=tn4)

    tn7 = TreeNode(val=1, left=tn5, right=tn6)

    sol = Solution()
    print(sol.isSymmetric(tn7))
