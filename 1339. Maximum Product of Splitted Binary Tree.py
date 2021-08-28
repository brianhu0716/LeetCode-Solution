# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):

            node_sum = 0 # node_sum saves the nodes sum from the current node as parent
            for next_node in [node.left, node.right]:
                if next_node:
                    node_sum += dfs(next_node)
            self.subtree_sum_list.append(node_sum + node.val) # subtree_sum_list saves all the node_sum
            return self.subtree_sum_list[-1]

        self.subtree_sum_list = list()
        dfs(root)
        print(self.subtree_sum_list)
        total = self.subtree_sum_list.pop() # total sum of the tree
        max_product = float('-inf')
        for subtree_sum in self.subtree_sum_list:
            max_product = max(max_product, subtree_sum * (total - subtree_sum))
        return max_product % (10 ** 9 + 7)