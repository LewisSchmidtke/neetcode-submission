from dataclasses import dataclass
class FileSharing:
    def __init__(self, m: int):
        self.free_ids = []
        heapq.heapify(self.free_ids)
        self.next_id = 1
        self.user_data = {}

    def join(self, ownedChunks: List[int]) -> int:
        if self.free_ids:
            new_id = heapq.heappop(self.free_ids)
        else:
            new_id = self.next_id
            self.next_id += 1
        
        self.user_data[new_id] = set(ownedChunks)

        return new_id

    def leave(self, userID: int) -> None:
        heapq.heappush(self.free_ids, userID)
        self.user_data.pop(userID)


    def request(self, userID: int, chunkID: int) -> List[int]:
        res = []
        for user in sorted(self.user_data.keys()):
            if chunkID in self.user_data[user]:
                res.append(user)
        if res:
            self.user_data[userID].add(chunkID)
            return res

        return []

