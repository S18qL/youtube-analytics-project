from googleapiclient.discovery import build
import os
import json

class Channel:
    """Класс для ютуб-канала"""
###    api_key: str = os.getenv('API_KEY')
    api_key = "AIzaSyALoInkGQqB_qIyF9QMl37aeSiSh960sN4"
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count
    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.channel()['items'][0]['snippet']['title']

    @property
    def description(self):
        return self.channel()['items'][0]['snippet']['description']


    @property
    def video_count(self):
        return self.channel()['items'][0]['statistics']['videoCount']

    @property
    def subscriber_count(self):
        return int(self.channel()['items'][0]['statistics']['subscriberCount'])

    @property
    def view_count(self):
        return self.channel()['items'][0]['statistics']['viewCount']

    @property
    def url(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    def channel(self):
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel


    def printj(self, dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        channel = self.channel()
        self.printj(channel)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename):
        data = {'channel_id': self.channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'video_count': self.video_count,
                'view_count': self.view_count,
                'subscriber_count': self.subscriber_count}
        with open(filename, 'w') as f:
            json.dump(data, f)

