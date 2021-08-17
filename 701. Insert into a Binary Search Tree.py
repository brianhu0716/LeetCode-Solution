# algorithm:
"""
(a) for each node we meet, compare its value to the value we want to insert(called target), if target > node.val, next node will move to node.right else move to node.left
(b) no matter we move to node.right or node.left, we can repeat the process until there is a node without node.left or node.right, then it is the position where we need to
    insert the target to
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        ptr = root
        while ptr:
            if val > ptr.val:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = TreeNode(val)
                    return root
            else:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = TreeNode(val)
                    return root