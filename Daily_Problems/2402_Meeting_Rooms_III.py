"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

Constraints:

1 <= n <= 100
1 <= meetings.length <= 105
meetings[i].length == 2
0 <= starti < endi <= 5 * 105
All the values of starti are unique.
"""
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # rooms that are avaialable at any given time, at start all rooms are avaiable
        # rooms_avaialble will be heap with each element having value the room number
        rooms_avaialble = [i for i in range(n)] 
        
        # rooms that are currently in use at any given time
        # rooms_currently_in_use will be a heap with each value [end_time, room_allocated], end_time will the time at which meeting will end 
        rooms_currently_in_use = [] 
        
        # sorting the meetings array as we want to process meetings with eralier start time first
        meetings.sort()
        
        # maintaining the number of meetinf each room hold during allocation at start each and every room will have 0 meetings allocated
        meetingsHeldPerRoom = defaultdict(int)
        # the current room with most meeting hold
        ans_room = None
        # the value for room with most meetings currently
        ans_meeting = 0
        
        # iterating thorugh each and every meeting
        for S,E in meetings:
            # first we will check if there are any meeting that was ongoing but is finished before "S" and if so wwe will remove that from "rooms_currently_in_use" and add the room back to rooms_avaialble
            # the "rooms_currently_in_use[0][0] <= s" equal too sign beacuse it is half closed interval a meeting room help up for [2,5) will be avaible at 5 for any new meeting starting at 5
            while rooms_currently_in_use and rooms_currently_in_use[0][0] <= S:
                meeting_end_time, meeting_room = heapq.heappop(rooms_currently_in_use)
                heapq.heappush(rooms_avaialble, meeting_room)

            # now we check to which room we will allocate this meeting 
            if rooms_avaialble: # if rooms_avaialble is not empty we will allocate the meeting to lowest number room ans as it is a heap we just need to use heapq.heappop() and we will get the smallest room available and push it inot the rooms_currently_in_use with [end_time of meeting, room_number]
                room_number = heapq.heappop(rooms_avaialble)
                heapq.heappush(rooms_currently_in_use, [E, room_number])
            else:
            # and if room are not avaiable we need to remove the room which will be avaiable first and we can get that from head of rooms_currently_in_use as it will sorted according to meeting time
                meeting_end_time, room_number = heapq.heappop(rooms_currently_in_use)
                # the push logic is little differnt as now the room was made avaible at meeting_end_time for meeting currently for which the room is hold and after that meeting that we are going to allocated has total time of E-S which will happen after meeting_end_time so we need to add E-S to meeting time
                heapq.heappush(rooms_currently_in_use, [E-S + meeting_end_time, room_number])
            
            # adding 1 to room_number which the meeting was allocated
            meetingsHeldPerRoom[room_number] += 1
            
            # checking if the room_number which was allocated has most meetings allocated to that room we update the ans_meeting and ans_room
            if meetingsHeldPerRoom[room_number] > ans_meeting:
                ans_meeting = meetingsHeldPerRoom[room_number]
                ans_room = room_number
            # if the meeting of room_number is same as the maximum value of meetings allocated we will check whoch room number is lowest ans assin ans_room to that as we are requied to return room_number with lowest number if there are multiple answers
            elif meetingsHeldPerRoom[room_number] == ans_meeting:
                ans_room = min(room_number, ans_room)
        
        return ans_room
