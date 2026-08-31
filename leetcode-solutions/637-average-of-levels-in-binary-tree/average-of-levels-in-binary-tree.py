# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret_list = []
        if not root:
            return ret_list
    
        cur_nodes = [root]
        while cur_nodes:
            num_cur = len(cur_nodes)
            cur_sum = 0
            for i in range(num_cur):
                node = cur_nodes.pop(0)
                cur_sum += node.val
                if node.left:
                    cur_nodes.append(node.left)
                if node.right:
                    cur_nodes.append(node.right)
            ret_list.append(cur_sum / num_cur)
    
        return ret_list
