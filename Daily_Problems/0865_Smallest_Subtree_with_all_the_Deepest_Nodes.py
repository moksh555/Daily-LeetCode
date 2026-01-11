"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    # my intuition here is that we traverse to the leaf nodes and we recurse back from each leaf node and calculate the maximum depth of left subtree and right subtree for each root and check if the max depth is equal we got the smallest subtree where deepest node are same for left and right subtree adn if not we can return what we can get from max left or right subtree

    # a helper funciton which will depth first serach and got to leaf node and traverse back returning depth and smallest root node with deepest node every time
    def dfs(self, root):
            if not root:
                return 0, None # so if there is no root we can return depth qual 0 and smallest node with deepest nodes None this will be our base case for recursion
            
            # making sure first we calcualte for subtrees of the root before calculating for the root as to get the maximum depth from this root to its left and right subtree
            left_depth, left_ans_node = self.dfs(root.left)
            right_depth, right_ans_node = self.dfs(root.right)

            # so these are the cases 
            # first case if the left_depth is equal to right_depth we can say that the deepest node in from this root are same for left and right and this can be potential smallest subtree such that it contains all the deepest nodes 
            if left_depth == right_depth:
                return left_depth+1, root
            # second case if left has more deep nodes then we would have already got the smallest subtree root which could be potential answer for us and we can return that with adding 1 to depth so the roots can be calcualted 
            elif left_depth > right_depth:
                return left_depth+1, left_ans_node
            # third case same as second only difference that right_depth is longer than left_depth
            else:
                return right_depth+1, right_ans_node

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we call the helper fucntion dfs and get the answer max_depth and the smallest subtree
        max_depth, smallest_subtree = self.dfs(root)
        return smallest_subtree

