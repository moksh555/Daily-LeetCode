"""
You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

Input: n = 2, m = 1, hBars = [2,3], vBars = [2]

Output: 4

Explanation:

The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].

One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

Constraints:

1 <= n <= 10**9
1 <= m <= 10**9
1 <= hBars.length <= 100
2 <= hBars[i] <= n + 1
1 <= vBars.length <= 100
2 <= vBars[i] <= m + 1
All values in hBars are distinct.
All values in vBars are distinct.
"""

# Wrong Path Explanation:
# ohh man feeling bit rusty today took 3 wrong answer to get to solution but hey got there in the end :)
# so at first I did completely go down a wrong path, I thought of removing matching bars in hBars which are also there in vBars, and that way I thought if I removed this both for example "2" in hBars and "2" in vBars then we got ourselves a square hole of size 2x2 but see here I was wrong bar in hBar can be "13" and "2" in vBars then to we have a square hole of size 2x2 if we remove both these bars 
# but what I got right was to make bigger square you need to remove continuos bars say if you remove bars "2" in both vBars and hBars you get 2x2 square hole and now if you again remove "3" in both you get a bigger sqaure of 3x3 so this part was right 

# Correct Path Explanation:
# so the correct was relies on the later correct part I had while I was going down the wrong path and thats, so we need to find how many continious bars we can remove in both hBars and vBars as this help us to acess how big a sqaure we can build
# and at last when you have this you just need to retrun whats the minimum of continous removal of abrs you got and sqaure it and retrun
# so why this beacuse lets say if you dont use continous bars which can be removes there can x where x > 0 bars between last removed and currently what you are removing and this will break the square formation so we need to make sure we remove continous bars only
# and why minimum beacuse if you can remove 3 continous bars in hBars and 2 in vBars then you can only make a square of size 2x2 as in one direction you are limited to 2 only
from typing import List

class Solution:
    # so this is the function which will help us to find how many continous bars we can remove
    # parameters is the bars list wethat we can remove
    def max_continous_bars(self,bars):
            maxi = 1 # what is the maximum we can remove it will always be 1 beacuse we are given bars array has atleast 1 bar ans one bar is always continous
            curr = 1 # what is the count of current continous bars we can remove
            for i in range(1,len(bars)): # we loop thorugh the bars array
                if bars[i-1] + 1 == bars[i]: # if the current bar is continous with previous bar
                    curr += 1 # we increase the current count
                    maxi = max(maxi, curr) # we update the maximum if current is greater
                else: # if not continous
                    curr = 1 # we reset the current count to 1
            return maxi # we return the maximum continous bars we can remove

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # we need to amke sure we sort these arrays beacuse we are relying on calcualting continous bars by just checking previous and current bar in the "max_continous_bars" function
        hBars.sort() 
        vBars.sort()
        
        vertical = self.max_continous_bars(vBars) # we get the result for vertical bars
        horizontal = self.max_continous_bars(hBars) # we get the result for horizontal bars

        return min(vertical+1, horizontal+1) ** 2 # we return the minimum of both + 1 and why +1 beacuse if you remove one bar from vertical you are making joining two coloumns together same for horizontal so we need to add 1 to get the size of square hole and we square it to get the area of square hole


# N = length of hBars
# M = length of vBars
# Time compelxity: O(N LogN + M logM + N + M) => O(N logN + M logM) beacuse we are sorting both the arrays and "N + M" beacuse we are looping through both the arrays once to get the maximum continous bars we can remove
# Space complexity: O(1) we are not using any extra space of any order except variables
