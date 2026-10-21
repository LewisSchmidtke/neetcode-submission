class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mapping = {}

        for trip in paths:
            src, dest = trip
            if src not in mapping:
                mapping[src] = 0
            else:
                mapping.pop(src)
            
            if dest not in mapping:
                mapping[dest] = 1
            else:
                mapping.pop(dest)
        
        for name, trip_type in mapping.items():
            if trip_type == 1:
                return name
