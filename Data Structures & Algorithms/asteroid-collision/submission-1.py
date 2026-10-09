class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_stack = []

        for asteroid in asteroids:
            if not collision_stack:
                collision_stack.append(asteroid)
                continue
            
            collides = False
            while collision_stack and (asteroid < 0 < collision_stack[-1] or collision_stack[-1] < 0 < asteroid): # Opposite directions -> collision
                collides = True
                if abs(collision_stack[-1]) > abs(asteroid):
                    break
                elif abs(collision_stack[-1]) < abs(asteroid):
                    collision_stack.pop()
                    collision_stack.append(asteroid)
                else:
                    collision_stack.pop()
                    break

            if not collides:
                collision_stack.append(asteroid)

        return collision_stack

