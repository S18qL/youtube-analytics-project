from src.channel import Channel
from src.video import Video
import datetime
import isodate
class PlayList:
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
    def playlist(self):
        playlist = Channel.get_service().playlists().list(id=self.playlist_id,
                                     part='contentDetails,snippet',
                                     maxResults=50,
                                     ).execute()
        return playlist

    @property
    def title(self):
        return self.playlist()['items'][0]['snippet']['title']

    @property
    def url(self):
        return f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def playlist_items(self):
        playlist = Channel.get_service().playlistItems().list(playlistId = self.playlist_id,
                                                              part='contentDetails',
                                                              maxResults=50,
                                                              ).execute()
        return playlist

    def get_videos(self):
        videos = []
        for i in self.playlist_items()['items']:
            video = i['contentDetails']['videoId']
            videos.append(video)
        return videos

    @property
    def total_duration(self):
        count = datetime.timedelta()
        videos = self.get_videos()
        for i in videos:
            video = Video(i)
            video_time = video.video()['items'][0]['contentDetails']['duration']
            video_duration = isodate.parse_duration(video_time)
            count += video_duration
        return count

    def show_best_video(self):
        best_video = ""
        max = 0
        videos = self.get_videos()
        for i in videos:
            video = Video(i)
            if int(video.like_count) > max:
                max = int(video.like_count)
                best_video = video.url
        return best_video