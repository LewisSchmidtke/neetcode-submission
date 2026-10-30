from dataclasses import dataclass

class VideoSharingPlatform:
    def __init__(self):
        self.free_ids = []
        heapq.heapify(self.free_ids)
        self.next_id = 0

        self.video_data = {}


    def upload(self, video: str) -> int:
        if not self.free_ids:
            new_id = self.next_id
            self.next_id += 1
        else:
            new_id = heapq.heappop(self.free_ids)

        new_video = VideoMetadata(
            id=new_id, 
            video_content=video,
            video_length=len(video)
        )
        self.video_data[new_id] = new_video

        return new_id

    def remove(self, videoId: int) -> None:
        if videoId in self.video_data:
            self.video_data.pop(videoId)
            heapq.heappush(self.free_ids, videoId)
        
    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.video_data:
            return "-1"

        self.video_data[videoId].views += 1
        length_border = min(endMinute, self.video_data[videoId].video_length)

        return self.video_data[videoId].video_content[startMinute:length_border + 1]

    def like(self, videoId: int) -> None:
        if videoId not in self.video_data:
            return

        self.video_data[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId not in self.video_data:
            return

        self.video_data[videoId].dislikes += 1    

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.video_data:
            return [-1]
        
        return [self.video_data[videoId].likes, self.video_data[videoId].dislikes]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.video_data:
            return -1

        return self.video_data[videoId].views

@dataclass
class VideoMetadata:
    id : int
    video_content : str
    video_length : int
    views : int = 0
    likes : int = 0
    dislikes : int = 0
