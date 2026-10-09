class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = list(zip(timestamp, username, website))
        data.sort()
        
        visitors = defaultdict(list)
        for _, user, w in data:
            visitors[user].append(w)

        result_map = defaultdict(int)

        for websites in visitors.values():
            if len(websites) < 3:
                continue
            
            for k in range(len(websites)):
                if k + 3 > len(websites):
                    break
                pattern = tuple(websites[k: k + 3])
                result_map[pattern] += 1

        pattern_data = list(result_map.items())
        res = sorted(pattern_data, key= lambda x: x[1])
        return list(pattern_data[0][0])

            
