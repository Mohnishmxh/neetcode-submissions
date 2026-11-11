import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by their original start time
        meetings.sort(key=lambda x: x[0])
        
        # Min-heap of currently free room indices
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # Min-heap of busy rooms: (end_time, room_index)
        busy_rooms = []
        
        # Count meetings held in each room
        meeting_count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Release rooms that have finished before or at the current meeting's start time
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)
            
            if available_rooms:
                # An unused room is available
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                # All rooms are busy; wait for the earliest ending meeting
                earliest_end, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (earliest_end + duration, room))
            
            meeting_count[room] += 1
            
        # Find room with maximum meetings (lowest room index on tie)
        max_meetings = max(meeting_count)
        return meeting_count.index(max_meetings)