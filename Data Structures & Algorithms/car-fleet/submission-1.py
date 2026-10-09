class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def calc_time(pos, speed, target):
            return (target - pos) / speed

        pos_speed_list = list(zip(position, speed))
        sorted_psl = sorted(pos_speed_list, key=lambda x: x[0], reverse=True)

        fleet_stack = []

        for pos, speed in sorted_psl:
            time_to_dest = calc_time(pos, speed, target)
            if not fleet_stack:
                fleet_stack.append(time_to_dest)
                continue

        
            if time_to_dest <= fleet_stack[-1]: # current car will catch car in front because it would reach dest quicker
                continue # We continue because no need to append the car
            else:
                fleet_stack.append(time_to_dest)

        return len(fleet_stack)
            
