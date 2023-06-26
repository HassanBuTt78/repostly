import praw
import youtube_dl
import os

from config import REDDIT_USER_AGENT, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, FFMPEG_PATH
root_path = os.path.dirname(os.path.abspath('./reddit'))

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)


def getPosts(subreddit, score_criteria=10):
    motivationSub = reddit.subreddit(subreddit)
    posts = motivationSub.top(time_filter="day")
    pTitleLinks = []
    for post in posts:
        if post.is_video:
            if post.score > score_criteria:
                post_data = {
                    "id": post.id,
                    "title": post.title,
                    "url":  post.url,
                    "score": post.score,
                    "commentCount":  post.num_comments,
                    "localPath": None,
                    "tags": []
                }
                pTitleLinks.append(post_data)
    return pTitleLinks


def downloadPost(url, title):
    ffmpeg_location = FFMPEG_PATH
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'ffmpeg_location': ffmpeg_location,
        'outtmpl': f"/videos/{title}",
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])
    videoPath = os.path.abspath(root_path + ydl_opts["outtmpl"]+'.mp4')
    return videoPath
