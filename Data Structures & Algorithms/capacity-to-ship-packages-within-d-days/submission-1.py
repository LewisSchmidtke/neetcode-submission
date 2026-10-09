class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # We assume non-negative, non-zero weights[i], days > 0

        # Minimum weight capacity = max(weights) | Lower bound by heaviest package on conveyor belt
        # Upper bound of min capacity array = sum(weights)
        # --> [max(weights), sum(weights)]
        left = max(weights)
        right = sum(weights)
        min_capacity = right

        while left <= right:
            capacity = left + ((right - left) // 2)
            needed_days = 0
            running_weights = 0
            for weight in weights:
                if running_weights + weight <= capacity:
                    running_weights += weight
                else:
                    needed_days += 1
                    running_weights = weight
            if running_weights > 0:
                needed_days += 1

            if needed_days > days:
                left = capacity + 1
            else:
                min_capacity = min(min_capacity, capacity)
                right = capacity - 1

        return min_capacity