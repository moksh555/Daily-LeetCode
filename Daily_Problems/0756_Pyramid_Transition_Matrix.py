"""
You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

Constraints:

2 <= bottom.length <= 6
0 <= allowed.length <= 216
allowed[i].length == 3
The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
All the values of allowed are unique.

"""

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # seeting up lookup table, what this lookup table, what this will do is directly helps us to traverse the top lement for left+right without iterating whole allowed array everytime, a little optimization 
        lookup = defaultdict(list) #lookup = {ab: [c,e,w], eb:[t,y,u]} so here "a" and "b" together "ab", are bottom left and bottom right block for which there are [c,e,w] block that can go on top

        for l,r,t in allowed:
            lookup[l+r].append(t) #each elemnt of allowed is three letters example "abc" so here l=a, r=b, t=c and giving and sotring lookup[ab].append(c)
        
        # main helper function to run backtracing and @cache helps to store similar result in memory so it can be reused again if same exists, so in another sense we are using memoization to resuse already visited path
        @cache
        def helper(ind, start, new):# new -> the string which we can build from start and lookuptable, start is the already build layers or bottom layer to which we are building "new" or top layer, and "ind" is again the index of which new layer we are on
            
            if len(start) == 1:# if length of start == 1, we will return Truw which means we ahve reached the topmost layer and no further layer possible
                return True 
            
            if ind == len(start)-1: # so if "new" string is built full which we can say from if "ind" is at len(start)-1 index which means the layer is already and we should go and build top layer which now start = new which will be bottom layer and new will be empty string as we will start to build new string absed on the bottom layer
                return helper(0, new, "")
            
            # getting bottom left and right to build new layer from bottom or start layer
            l = start[ind]
            r = start[ind+1]
            for char in lookup[l+r]:# iterating thorugh every possible answer for left and right combination in lookup table
                if helper(ind+1, start, new + char): # if any of it returns True we directly return True 
                    return True
            return False # if none returns True this will return False
        return helper(0,bottom, "") # calling helper fucntion with ind = 0 as will start to build the top layer for bottom and new will be empty string
