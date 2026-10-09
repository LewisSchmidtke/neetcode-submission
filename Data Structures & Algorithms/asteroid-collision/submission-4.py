class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Negative moving left
        # Positive moving right
        # If stack is empty and element is negative -> No collision

        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue

            # Asteroid will be negative here so we can check collisions
            # Previous asteroid also negative -> no collision
            if stack and stack[-1] < 0 or not stack:
                stack.append(asteroid)
                continue
            
            # Collision:
            while stack and stack[-1] > 0:
                if abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break
    
                elif abs(asteroid) < abs(stack[-1]):
                    break

                else: # Asteroid is larger
                    stack.pop()

        return stack