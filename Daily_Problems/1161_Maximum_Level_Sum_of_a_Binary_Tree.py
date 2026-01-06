"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # my intuition is that we hace to calculate each and every row or level sum so BFS is best and easiest way to go, so we will have a queue and calcualte the sum of current level while also adding the childrens of that current level

        # setting up queue
        q = deque()

        # you dont need this check but I just wanted it
        if root:
            q.append(root) # adding the root to the queue or in other way there will only root on first level

        # setting up variable, one  we will keep track of the maximum sum we ahve encountered so far and other will what level that maximum sum was for
        max_level_sum = float("-inf")
        max_level = None
        # thisvariable twll up which level we currently are ont
        curr_level = 0

        # starting my while loop or BFS
        while q:
            # adding the 1 to level as with every new loop you will be in different or one down level
            curr_level += 1
            # setting up variable to calcualte the sum of current level we are on
            curr_level_sum = 0

            # for loop to only calculate the node which are on that level, beacuse we will be simultaneoulsy working with nodes of current level and also adding the childresn of it so we want to process only one level at a time so only iterating thrugh current level of nodes
            for i in range(len(q)):
                popped_root = q.popleft() # popping nodes from current level
                curr_level_sum += popped_root.val # adding its value to curretn level sum
                
                # we will only add children if the they are not None
                if popped_root.left: 
                    q.append(popped_root.left)
                if popped_root.right:
                    q.append(popped_root.right)
            
            # making sure our variable of max_level_sum and max_level are up-to-date as we keep on iterating thorugh each layer
            if curr_level_sum > max_level_sum:
                max_level = curr_level
                max_level_sum = curr_level_sum
        return max_level

        # N -> Number of Nodes in given tree
        # time complexity: O(N) as we will go thorugh each and every node in the tree only once
        # space complexity: 0(N) as our queue will have each and every node once in its tree
