class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def calc_time(pos, speed, target):
            return (target - pos) / speed

        pos_speed_list = list(zip(position, speed))
        sorted_psl = sorted(pos_speed_list, key=lambda x: x[0], reverse=True)

        fleet_stack = [sorted_psl[0]]
        for pos, speed in sorted_psl[1:]:
            if speed <= fleet_stack[-1][1]: # car will not catch previous car
                fleet_stack.append((pos, speed))
            else:
                prev_pos, prev_speed = fleet_stack[-1]
                if calc_time(prev_pos, prev_speed, target) >= calc_time(pos, speed, target):
                    # Car will catch up
                    fleet_stack.pop()
                fleet_stack.append((pos, speed))

        return len(fleet_stack)
            
