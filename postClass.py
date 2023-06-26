from utils import non_rept
from utils import queue
from utils.strings import remove_non_bmp, extract_tags_and_remove
from config import TIKTOK_DEFAULT_HASHTAGS
import reddit
import tiktok

import os


class Post:
    def __init__(self, post):
        self.id = post['id']
        self.title = post["title"]
        self.url = post['url']
        self.score = post['score']
        self.commentCount = post['commentCount']
        self.localPath = post['localPath']
        self.tags = post['tags']
        self.modifyTitle()
        if len(self.tags) <= 0:
            self.tags = TIKTOK_DEFAULT_HASHTAGS
        if non_rept.check(self) ==  False:
            self.downloadVid()
            self.store_in_record()
            self.add_to_queue()
        else:
            print(f'\u2713 ALREADY PROCESSED = {self.title}')

    def downloadVid(self):
        self.localPath = reddit.downloadPost(self.url, self.title)
        print("FILE SAVE AT:", self.localPath)

    def uploadVid(self):
        tiktok.upload(self)

    def modifyTitle(self):
        title = self.title
        tags, title_without_tags = extract_tags_and_remove(title)
        self.tags.extend(tags)
        title_without_tags = remove_non_bmp(title_without_tags)
        self.title = title_without_tags.strip()

    def delete_file(self):
        try:
            os.remove(self.localPath)
            print(f"Video file '{self.localPath}' deleted successfully.")
        except OSError as e:
            print(f"Error occurred while deleting the video file: {e}")
    

    def add_to_queue(self):
        queue.add(self)

    def store_in_record(self):
        non_rept.store_record(self)

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "score": self.score,
            "commentCount": self.commentCount,
            "localPath": self.localPath,
            "tags": self.tags
        }


    