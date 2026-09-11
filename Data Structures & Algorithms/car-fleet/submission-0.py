class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Combine position and speed, then sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0
        
        for p, s in cars:
            time = (target - p) / s
            
            # If the current car takes longer than the fleet ahead, it's a new fleet
            if time > max_time:
                fleets += 1
                max_time = time
                
        return fleets