from src.channel import Channel
class Video:
    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id

    def __str__(self):
        return f'{self.title}'

    @property
    def title(self):
        try:
            return self.video()['items'][0]['snippet']['title']
        except:
            return None

    @property
    def url(self):
        return f'https://www.youtube.com/watch?v={self.__video_id}'

    @property
    def view_count(self):
        try:
            return self.video()['items'][0]['statistics']['viewCount']
        except:
            return None
    @property
    def like_count(self):
        try:
            return self.video()['items'][0]['statistics']['likeCount']
        except:
            return None

    def video(self):
        video = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=self.__video_id
                                       ).execute()
        return video

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    @property
    def playlist_id(self):
        return self.playlist_id