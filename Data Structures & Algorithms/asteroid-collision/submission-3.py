class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_stack = []

        for asteroid in asteroids:
            if not collision_stack:
                collision_stack.append(asteroid)
                continue
            
            collides = False
            top_val = collision_stack[-1]
            current = asteroid
            while collision_stack and (current < 0 < top_val or top_val < 0 < current): # Opposite directions -> collision
                collides = True
                if abs(top_val) > abs(current): # Asteroid in stack is heavier than current one -> current one gets destroyed
                    current = None
                    break
                elif abs(collision_stack[-1]) < abs(asteroid):
                    collision_stack.pop()
                    top_val = collision_stack[-1] if collision_stack else 0
                else:
                    collision_stack.pop()
                    current = None
                    break

            if not collides:
                collision_stack.append(current)

        return collision_stack

