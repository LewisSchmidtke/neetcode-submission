class TimeMap:

    def __init__(self):
        self.time_map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        # Theoretically we can use 1 list as value with tuples (value, timestamp)

        if key not in self.time_map:
            self.time_map[key] = {"mood" : [value], "timestamp" : [timestamp]}
        else:
            self.time_map[key]["mood"].append(value)
            self.time_map[key]["timestamp"].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        timestamps = self.time_map[key]["timestamp"]

        if len(timestamps) <= 1:
            try:
                return self.time_map[key]["mood"][0]
            except IndexError:
                return ""


        # Stored in ascending order so we can do a binary search
        left = 0
        right = len(timestamps) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if timestamp == timestamps[mid]:
                return self.time_map[key]["mood"][mid]
            elif timestamp > mid:
                left = mid + 1
            else:
                right = mid - 1
        print(self.time_map)
        print(mid)
        if mid - 1 < 0:
            return ""
        else:
            return self.time_map[key]["mood"][mid - 1]
