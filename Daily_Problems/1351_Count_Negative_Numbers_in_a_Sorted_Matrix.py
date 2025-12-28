from typing import List
class Solution:
    def countNegatives_firstapproach(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        # First Approach Iterating whole grid and counting negative number
            # time complexity -> O(R * C)
            # Space complexity -> O(1)
        negative_count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] < 0:
                    negative_count += 1
        return negative_count

    def countNegatives_secondapproach(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        # # Second Approach we oterate the every row and use binary search to find the first negative in that row and we can directly count the total number of negative numbers in that row
        #     # time complexity -> O(R * log(C))
        #     # Space complexity -> O(1)
        negative_count = 0
        for r in range(R):
            # Binary Search
            left = 0 # minimum of range
            right = C-1 # maximum of range
            first_negative_index = C # this is the first negative index in that we have found so far
            while left <= right:
                mid = left + (right - left)//2
                if grid[r][mid] < 0:
                    first_negative_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            negative_count += (C - first_negative_index)
        return negative_count

    def countNegatives_thirdapproach(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        # Third Approach this is an intuitive approach lets first amke some thing clear what we ar give
            # - we are given that row is sorted in non-decreasing oreder which means if we find a early negative in that row we can directly say how many negative are there in that row
            # - with this we can start from bottom left corner, why bottom left again giving emphaziz on "find early negative number in the row to reduce the computation" so we can get early negative if we start from bottom left
            # - third we are also given that each row is ordered in non decreasing so we can say that if any positive in that coloumn we can surely say above that particualr positive elemnt in the coloumn every element will be positive

        # seeting up ietrables at bottom left corner
            # time complexity -> O(R + C)
            # Space complexity -> O(1)
        start_row = R-1
        start_col = 0 
        negative_count = 0 # total count for negative numbers

        while start_row >= 0 and start_col < C:
            if grid[start_row][start_col] >= 0: # this will check if the particualr element at start_row and start_col is positive
                start_col += 1 # if positive we have not yet found early negative for that row so we will move towards right in that same row
            else: # and if we have found that eraly negative we will say we have got the number of negative in this row we will move upwards but same coloumn, why same coloumn again the coloumn are order in non-decreasing order so all the coloumns in same row were positive before we found the eraly negative and with this we can surely say that everyhitng above for thT coloumn will be positive and dont have to wrorry about that
                negative_count += (C - start_col)
                start_row -= 1
        return negative_count





