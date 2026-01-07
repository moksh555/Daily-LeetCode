"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.MOD = 10 ** 9 + 7

    def getTotalSum(self, root):
        if not root:
            return 0
        
        left = self.getTotalSum(root.left)
        right = self.getTotalSum(root.right)
        return left + right + root.val
    
    def getMaxProduct(self, root, totalSum):
        if not root:
            return float("-inf"), 0
        
        # this are variable which we will calculate for curr_max and also amke sure we have left and right sum
        curr_max = 0
        left_sum = 0
        right_sum = 0

        # check if left children exixts 
        if root.left:
            left_max, left_sum = self.getMaxProduct(root.left,totalSum) # first we will rcurse to children and calculate tat subtree
            curr_max = max(left_max, (totalSum - left_sum) * left_sum) # now we will calculate maximum from the subtree that we traversed first and also if we break current root and its left children
        if root.right:
            right_max, right_sum = self.getMaxProduct(root.right,totalSum)
            curr_max = max(curr_max, right_max)
            curr_max = max(curr_max, (totalSum - right_sum) * right_sum)
        
        return curr_max, left_sum + right_sum + root.val

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # The intuition here is pretty simple that we need to traverse to each and every root and check for each of its children if we seperate that children and make two subtrees then what is the product. So we will use recursion here starting from root traverse to very bottom every time and start from and then recursively calculate for each and every root.


        # first we will get the total sum of values in tree this will help us to make the main calulation easy and effiecient
        totalSum = self.getTotalSum(root)

        # now we will calculate the for each and every root and its chidlren
        maxProduct, totalSum = self.getMaxProduct(root, totalSum)
        return maxProduct % self.MOD
