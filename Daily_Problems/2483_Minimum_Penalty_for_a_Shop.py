"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Constraints:

1 <= customers.length <= 105
customers consists only of characters 'Y' and 'N'.
"""




class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # count of N and Y in customers array
        close_count_N = 0 
        close_count_Y = 0
        for i in range(n):
            if customers[i] == "Y":
                close_count_Y += 1
            else:
                close_count_N += 1
        
        # main iteration
        min_penalty = float("inf") # minimum of minimum penalty for n hours 
        hour_min_penalty = None # hour at which min_penatly incur, we are decalring it None but there will be no case that we will return None as their will be some hour for sure where penalty for that hour will be less then infinity
        open_count_N = 0 # count of N that will come when shop is open
        open_count_Y = 0 # count of Y that will come when shop is open

        for i in range(n+1):
            N_count_left = open_count_N # time when shop was open but no customers came
            Y_count_right = close_count_Y # time when shop will be closed but customers came
            penalty_ith = N_count_left + Y_count_right # total penalty for ith hour 
            
            if penalty_ith < min_penalty:
                min_penalty = penalty_ith
                hour_min_penalty = i
            
            # we are adding to open count and substarcting form close count, as it will be case the ith element will now arrive when shop is open for i+1th hour
            if i < n and customers[i] == "N": 
                open_count_N += 1 
                close_count_N -= 1
            elif i < n:
                open_count_Y += 1
                close_count_Y -= 1 

        return hour_min_penalty


# time complexity: O(n) for first iteration and O(n+1) for second iteration -> O(n + n + 1) -> O(n)
# space complexity: O(1)