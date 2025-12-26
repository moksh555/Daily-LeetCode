# question
'''
You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

Constraints:
1 <= n == happiness.length <= 2 * 105
1 <= happiness[i] <= 108
1 <= k <= n
'''

class Solution:
    
    def maximize_happiness_of_selected_children(self, happiness, k):
        n = len(happiness)
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += max((happiness[i] - i),0)
        return ans



