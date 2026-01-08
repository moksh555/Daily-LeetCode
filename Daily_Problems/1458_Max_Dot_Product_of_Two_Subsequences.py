"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""

from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # the intution for me was that we need to somehow check each and every index in nums1 for each and every index in nums2 and somehow get maximum dot product from all possible pairs chosen, so I thought the best way was to go for dp, here I did little mistake which I will talk about in later
        # So yeah we need to somehow check for each and every index in nums1 for each and every index in nums2 

        N = len(nums1)
        M = len(nums2)

        # a helper fucntion for which we will do memoization, I have done a simple thing "@cache" there are alternative how we can implement this with disctionary or even array
        @cache
        def helper(ite1, ite2, taken):#ite1 or iterator for nums1 and ite2 or iterator for nums2
        # what is taken here, this is where I did a little mistake, so without taken there can be a case where No pairs are accecpted and I returned just 0 which was wrong must be non empty sub-sequence as it says in question.
            if ite1 >= N or ite2 >= M: # checking if none of the iterator goes beyong the length of respective arrays
                return 0 if taken else float("-inf") # so if none of the pair is accecpted we return negative infinity beacuse it is compulsory to accept one and if selected taken will be True and we can return 0 as now there can be no more accepted pairs 
            
            curr = float("-inf") # variable which will tell starting from ite1 and ite2 what is the maximum dot product we can achieve for remaining elements
            # accept ite1 and ite2
            curr = max(curr, helper(ite1+1, ite2+1, True) + (nums1[ite1] * nums2[ite2]))
            # do not accept ite1 and increase ite1 by 1
            curr = max(curr, helper(ite1+1, ite2, taken))
            # do not accept ite2 and increase ite2 by 1
            curr = max(curr, helper(ite1, ite2+1, taken))
            return curr # return curr
        return helper(0,0, False)

    # so the main intution was starting from ite1 and ite2 what can be maximum dot product subsequence which we can acheive, and for that reason we can use DP here

    # N = length of nums1
    # M = length of nums2
    # time complexity: O(N*M*2) N for traversing each index in nums1 and M for traversing each index in nums2 and "2" for taken which can be true or False
    # space comaplexity: O(N*M*2) same as time-complexity as each and every (ite1,ite2,taken) state will be stored.