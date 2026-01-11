"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.


Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""

# so here are three approach:
    # first approach: memoization
    # second approach: pure bottom-up dp
    # third approach: pure bottom-up dp with optimization

class Solution:
    def minimumDeleteSum_firstapproach(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        dp = {}

        def helper(ite1, ite2):
            if ite1 >= N and ite2 >= M:
                return 0
            
            if (ite1, ite2) in dp:
                return dp[(ite1, ite2)]
            
            curr = float("inf")
            # check if its same we can include that
            if ite1 < N and ite2 < M and s1[ite1] == s2[ite2]:
                curr = min(curr, helper(ite1+1, ite2+1))
            
            # we can delete ite1
            if ite1 < N:
                curr = min(curr, helper(ite1+1, ite2) + ord(s1[ite1]))
            # we can delete ite2
            if ite2 < M:
                curr = min(curr, helper(ite1, ite2+1) + ord(s2[ite2]))
            dp[(ite1,ite2)] = curr
            return curr 

        return helper(0,0)
    
    def minimumDeleteSum_secondapproach(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

        current_row_sum = 0
        for i in range(N-1,-1,-1):
            current_row_sum += ord(s1[i])
            dp[i][-1] = current_row_sum
            
        
        current_col_sum = 0
        for i in range(M-1,-1,-1):
            current_col_sum += ord(s2[i])
            dp[-1][i] = current_col_sum
            
        

        for r in range(N-1,-1,-1):
            for c in range(M-1,-1,-1):
                curr = float("inf")
                if s1[r] == s2[c]:
                    curr = min(curr, dp[r+1][c+1])
                
                curr = min(curr, dp[r+1][c] + ord(s1[r]))
                curr = min(curr, dp[r][c+1] + ord(s2[c]))
                dp[r][c] = curr
        return dp[0][0]

        
    def minimumDeleteSum_thirdapproach(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        dp = [0 for _ in range(M+1)]

        current_row_sum = 0

        current_col_sum = 0
        for i in range(M-1,-1,-1):
            current_col_sum += ord(s2[i])
            dp[i] = current_col_sum
            
        
        for r in range(N-1,-1,-1):
            current_row_sum += ord(s1[r])
            new_dp = [0 for _ in range(M+1)]
            new_dp[-1] = current_row_sum
            for c in range(M-1,-1,-1):
                curr = float("inf")
                if s1[r] == s2[c]:
                    curr = min(curr, dp[c+1])
                
                curr = min(curr, dp[c] + ord(s1[r]))
                curr = min(curr, new_dp[c+1] + ord(s2[c]))
                new_dp[c] = curr
            
            dp = new_dp
        return dp[0]

        
    