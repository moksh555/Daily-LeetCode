"""
There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

Constraints:

3 <= m, n <= 109
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences and vFences are unique.
"""


# AHH here we go again at first I thought why I am been taken to yestersday'sproblem but yeah this one different, and really this was my first time solving it mayber skipped over it earlier beacue, I used to do solve it number wise when I was solving leetcode for learning DSA, but aehh this one was fun had me thinking a little at first, but simple implmentation.

# So now we given hFences and vFences but this time these arrays contains the fences which are present horizontally and vertically respectively and again you can remove any one of them, now whats different here from yesterday is that here you are given fences or lines in the array which are the only present lines, there maybe some line skipped but in yesterdays you were given the lines you can remove from all line that were already present already present. So here what lines are present are given and yesterday all lines were present which you can remove were given.

# So now I looked at the diagram for a bit to get intuiton, I thought why not check for each and every line present if we remove everything in between these lines what amount of free space we can create
    # so for example lets say you were given hFences= [2,3,6,8] and n = 10, and we are given line 1 and line 10 are already present but you can't remove that, so now it becomes hFences = [1,2,3,6,8,10], which first and last not removable.
    # Now lets we remove everything between 2 and 8, so we remove 3 and 6 and we can create freww space of 8 - 2 = 6, vertically, why vertical I think you need to take pen and paper and draw three lines horizontally and now draw vertical line going thorugh these lines you see there are three points of contant and again draw two lines an preferably draw first and last line just on the side of previous diagram and also draw a vertical line though this two horizontal line there will be only two point of contact and you freed up space for vertical line, if we remove between 3 and 8 we can create a space of 8 - 3 = 5 vertically and so on, so with this we can see what space we can create horizontally and we can do same for vertical or vFences as well to free horizontal space.
    # Now to make a sqaure you need all sides equal, so you need to have same length of free space in vertical and horizontal direction and this is the whole problem. 
from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m]) # we add the fixed fences which cannot be removed this is beacuse we need to calcualte what free space we can create for between every possible fences
        vFences.extend([1,n]) 
        
        # you can sort the hFences and vFences to remove the use of abs() or absolute function while I tried submitting both and to a shocking suprise sorting was faster on leetcode then just using abs() function (Somethings wrong I can feel it ;) 

        N = len(hFences) # getting length od both to make it easy to use in loops
        M = len(vFences)

        all_possible_spaces = set() # a set so we can save free sapces from one direction and check against other direction for same free spaces, noe why set beacuse lookup in set is O(1) on everage
        MOD = 10 ** 9 + 7 # we are given this that answer can be large use MOD 

        # looping though hFences to get all possible free spaces we can create horizontally
        for i in range(N):
            for j in range(i+1, N):
                all_possible_spaces.add(abs(hFences[j] - hFences[i]))

        max_area = -1 # max_area initialized to -1 so if we dont find any square area we can return -1 as given in problem statement

        # looping though vFences to get all possible free spaces we can create vertically and check if this free space is present in all_possible_space set that we calcualted from horizontal fences earlier
        for i in range(M):
            for j in range(i+1, M):
                w = abs(vFences[j] - vFences[i])
                if w in all_possible_spaces:
                    max_area = max(max_area, w * w) # can if present we update the max_area if we have found bigger square area
        
        return max_area % MOD if max_area > -1 else -1 # so if we ahve ans == -1 we return -1 beacuse -1 % MOD will be some large positive number but we are told to return -1 and if not -1 we can max_are % MOD
    
    # N = len(hFences)
    # M = len(vFences)
    # Time Complexity: O(N^2 + M^2) beacuse we are looping
    # Space Complexity: O(K) where K is number of unique free spaces we can create horizontally
