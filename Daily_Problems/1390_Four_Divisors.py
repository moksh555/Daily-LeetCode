"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        # So the intuition is that there is no intuition we cannot mathematically get how many divisors does a number have so we have to calculate for each and everyone individually 
        # so we will traverse thorugh each and every element in "nums" and we will make caluculate how many divisors does it have 
        
        # we can make a little optimization by saving the data of already calcualted number so we do not recalucualte it 
        dp = {1:[1,1]}

        # a helper fucntion which will calculate and return total sum of divisors and also total number of divisors, and paramater "n" is the number we are calcluating it for
        def helper(n):
            # ealry breaking we already have this in dp saved or in other words we already calcualted for the given number
            if n in dp:
                return dp[n]

            # two variables which we will calculate but started with 1 and number itself as 1 and number itself will always be the divisor of the number
            total_sum = 1 + n
            total_length = 2

            # iterating from 2, square root of number + 1
            # optimization, why we are using "int(n ** (1/2)) + 1" or oterating till square root + 1, because till that we will find all the divisors. on one side and for other side we will just divide the number with divisor found
            for i in range(2, int(n ** (1/2)) + 1):
                # if and only if "i" is divisor of "n"
                if n % i == 0:
                    # here we found the number on one side to get other we are diving "n" by "i" and also there can be a possibility where i and n//i are both same like in case of n=4, i=2, so n//i = 4//2 = 2, soo making sure it does not add divisor 2 two times we need this if else
                    total_sum += (i + (n // i) if i != n // i else i)
                    total_length += (2 if i != n//i else 1)
                
                if total_length > 4: #early breaking if the length of divisor is already greater than 4 
                    break
            dp[n] = [total_sum, total_length] # saving the data in dp 
            return dp[n]

        
        ans = 0
        for i in range(len(nums)):
            divisor_sum, divisor_length = helper(nums[i]) # calcualting with helper function
            if divisor_length == 4: # if length of divisor is exactly 4 we add the sum to ans 
                ans += divisor_sum

        return ans

# Let N be the length of nums
# Let M be the maximum element in nums
# Time Complexity -> O(N * √M) 
    # the N for ietarting each and every element in nums and for each and every elemnt we traversing from 2 to square of that number 
# Space Complexity -> O(N) 
    # the dp dictionary we are creating to save element