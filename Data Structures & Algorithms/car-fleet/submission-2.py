class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time_to_destination(pos, speed, target):
            return (target - pos) / speed

        # Merge position and speed info and sort list in reverse to have the furtherst car up the road first
        pos_speed_list = list(zip(position, speed))
        sorted_psl = sorted(pos_speed_list, key=lambda x: x[0], reverse=True)

        fleets = []
        for pos, speed in sorted_psl:
            time_to_dest = time_to_destination(pos, speed, target) # Calculate how long current car will need to reach target

            if not fleets: # Only true for first car
                fleets.append(time_to_dest)
                continue

            if time_to_dest <= fleets[-1]: # current car will catch car in front because it could reach the target quicker
                continue # We continue because no need to append the car

            # time to destination of current car is slower than the one of the nearest fleet, so it wont catch the fleet.
            else: # Add car (time) to fleets, creating a new fleet that can be caught.
                fleets.append(time_to_dest)

        return len(fleets)
            
