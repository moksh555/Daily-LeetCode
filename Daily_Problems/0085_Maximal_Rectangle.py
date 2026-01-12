"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.
"""
# I would really suggest to go over question 84 as this will help to do this questions easily, I would say it is extension of question 84 but with little modification but there are other ways to do it as well but this is how my intuition worked and I did it


# So lets go over question 84 a little "Largest Rectangle in Histogram", fair warning we will use monotonic stack here to solve this, so if you are not familiar with monotonic stack I would suggest to go over that first and then come back here.

# So it goes somehting like we wanted to find maximum area from the histograms we are given, from vertical rectangles of width 1 and heigths given in the array we need to what is the maximum area we can get or cut from that vertical rectangles, so the intuition here is pretty simple we will use monotonic stack to keep track of increasing heights and when we find a height which is smaller than the top of the stack we will start popping from the stack and calculate area for each popped height as the smallest height till now and calculate area with that height and width calculated from current index and index of new top of stack after popping, we will do this till we find a height which is smaller than current height or stack becomes empty, we will also add a sentinel value at end of heights array to make sure all heights are processed. So this is pretty much how we solve question 84. 

# So why does this work lets say you encounter a smaller height rectangle as comapred what you have seen last and append to stack, lets say heights of smaller rectangle is 4 and height of larger rectangle is 8, now when you enocunter 4 you cannot take that height 8 any further to right beacuse 4 is smaller than 8 obviously but also you will cut the rectangle or calculate the area which is not covered by these vertical rectangles we want the maximum of area from these rectangles, so when you encounter 4 you say okay we can only take rectangle of height 8 till here and we calulate the area and max_area if it.

from typing import List
class Solution:
    def maximalRectangle_firstapproach(self, matrix: List[List[str]]) -> int:
        # getting rows and columns for easy access
        R = len(matrix)
        C = len(matrix[0])

        # now this the modification in this question as comapread to question 84 there we were given heights in the array here we are given a matrix of 0 and 1 so we need to somehow make this to histogram, so for each row what we will do is we will caculate we go upwards from this row and column till how far can we go in other words on row "r" and coloumn "c" if you have "1" we will go uppward till we have encounter 1 and as soon as we hit "0" we will says that the maximum height we can go up and store that max_height from row "r" and column "c" in dp[r][c]
        # there is some optimization we can do to space complexity but thats for later first we need to solve this questions correctly 
        # so this dp matrix is count of each height of "1" from row "r" and column "c" and upwards and we hahve got ourselves a histogram array for each row now we can apply question 84 logic on each row of this dp matrix to get maximum area for each row and overall maximum area will be our answer
        dp = [[0 for _ in range(C+1)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == "1":
                    dp[r][c] = dp[r-1][c] + 1 if r-1 >=0 else 1
                
        # and this the logic to count maximum area for each row histogram using monotonic stack
        max_area = 0 # variable to keep track of overall maximum area
        for r in range(R):
            stack = [-1] # monotic stack for row r, we included "-1" so we can calculate width easily and dont have to check if stack is empty or not everytime we make some calulation that include stck
            
            # going for each column in that row
            for c in range(C+1):
                while stack[-1] != -1 and dp[r][stack[-1]] >= dp[r][c]:
                    height = dp[r][stack.pop()]
                    width = c - stack[-1] - 1 
                    max_area = max(max_area, height * width)
                stack.append(c)
        return max_area
    
    # so same logic but I have optimmized it here, space complexity I have reduced from R*C TO C
    # also we ahve reduced one loop as we are calculating the heights on the fly for each row
    def maximalRectangle_secondapproach(self, matrix: List[List[str]]) -> int:
        # getting rows and columns for easy access
        R = len(matrix)
        C = len(matrix[0])

        dp = [0 for _ in range(C+1)]
        max_area = 0 
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == "1":
                    dp[c] = dp[c] + 1
                else:
                    dp[c] = 0

            stack = [-1] 
            for c in range(C+1):
                while stack[-1] != -1 and dp[stack[-1]] >= dp[c]:
                    height = dp[stack.pop()]
                    width = c - stack[-1] - 1 
                    max_area = max(max_area, height * width)
                stack.append(c)
        return max_area

