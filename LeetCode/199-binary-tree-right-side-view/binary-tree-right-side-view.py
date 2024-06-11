# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret_list = []
        if not root:
            return ret_list
        
        cur_nodes = [root]
        while cur_nodes:
            ret_list.append(cur_nodes[-1].val)
            next_nodes = []
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                    
            cur_nodes = next_nodes
        
        return ret_list