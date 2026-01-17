# Another question which I had not seen before 
# so basically the intuition here is that there is no intuition its just brute force, you ahve to check each adn every point with each and every other point check if they intersect and if they. what is the length of intersection along x_axis and along y_axis and the minimum of that both length is the max_length sqaure we can fit inside thatintersection area and we do this for each point and return the maximum sqaure we found while looping.

from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0 # intializing variable which will keep track max_length sqaure we found till now
        n = len(bottomLeft) # variable to store number of rectangles given
        
        for i in range(n): # first loop 
            x_l_1, x_r_1 = bottomLeft[i][0], topRight[i][0] # getting left and right x_coordinates of rectangle i
            y_d_1, y_u_1 = bottomLeft[i][1], topRight[i][1] # getting down and up y_coordinates of rectangle i

            if x_r_1 - x_l_1 <= ans or y_u_1 - y_d_1 <= ans: # so this little optimzation we can do , if the current rectangle itself has any of its side less than or equal to what we found max_length so far we can just skip this beacuse no square larger than ans can be formed with this rectangle intersection even if the rectangle we are comapring to might have infite length side we can't form any sqaure in intersecting area larger then ans
                continue
            
            for j in range(i+1, n):
                x_l_2, x_r_2 = bottomLeft[j][0], topRight[j][0] # getting left and right x_coordinates of rectangle j
                y_d_2, y_u_2 = bottomLeft[j][1], topRight[j][1] # getting down and up y_coordinates of rectangle j

                if x_r_2 - x_l_2 <= ans or y_u_2 - y_d_2 <= ans: # same optimization as above for rectangle j
                    continue

                x_point_1 = [x_l_1, x_r_1] # creating x_points array for rectangle i
                x_point_2 = [x_l_2, x_r_2] # creating x_points array for rectangle j
                y_point_1 = [y_d_1, y_u_1] # creating y_points array for rectangle i
                y_point_2 = [y_d_2, y_u_2] # creating y_points array for rectangle j

                x_points = [x_point_1, x_point_2] # # storing array of x_points for both rectangles
                y_points = [y_point_1, y_point_2] # storing array of y_points for both rectangles

                x_points.sort() # sorting both arrays so that we can easily check if they intersect or not
                y_points.sort()
                
                # this is intersecting condition as we have already sorted the array of x_points and y_points if the second array start point lets say inside x_point is between first array start and end point then they intersect same for y_points as well and only if both of them is true we can say they intersect. You really need to visualize this as this is importanmt and hard to come-up with at first, but with practise you can get better at visualizing stuff and this will come naturally to you. 
                if x_points[0][0] <= x_points[1][0] < x_points[0][1] and y_points[0][0] <= y_points[1][0] < y_points[0][1]:
                    x_length = min(x_points[0][1], x_points[1][1]) - x_points[1][0] # calculating length of intersection along x_axis, and why min beacuse lets say one rectangle is from 1 to 10 and other is from 5 to 7, so yes 5 comes between 1 and 10 but the second rectangle x_axis length ends at 7, then intersection along x_axis will be from 5 to 7 and not 5 to 10 so we take min of both right points and subtracting with left point of second rectangle, same for y_axis
                    y_length = min(y_points[0][1], y_points[1][1]) - y_points[1][0]
                    square_length = min(x_length, y_length) # minimum of both length beacuse you need to make square so both x_length and y_length must be equal and minimum length is what we can make sqquare of that length
                    ans = max(ans, square_length) # updating ans if we found a square_length larger than ans
        return ans ** 2 # returning area of square which is side * side or length * length
    
    # N = number of rectangles given
    # Time Complexity: O(N^2) beacuse we are using two loops to check each rectangle with every other rectangle, well there is sort function but we knoe it only sorts out two array at given time so its O(1) effectively
    # Space Complexity: O(1) we are not using any extra space of any order except variables

               