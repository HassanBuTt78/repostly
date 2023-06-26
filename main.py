import schedule

from postClass import Post
import reddit
from utils import non_rept
from utils import queue
from config import SUBREDDIT, SCORE_CRITERIA

import time

print(

"""
______  _____ ______  _____  _____  _____  _   __   __
| ___ \|  ___|| ___ \|  _  |/  ___||_   _|| |  \ \ / /
| |_/ /| |__  | |_/ /| | | |\ `--.   | |  | |   \ V / 
|    / |  __| |  __/ | | | | `--. \  | |  | |    \ /  
| |\ \ | |___ | |    \ \_/ //\__/ /  | |  | |____| |  
\_| \_|\____/ \_|     \___/ \____/   \_/  \_____/\_/  
"""
)
print('### Thanks for using this tool! Feel free to contribute to this project on GitHub! If you have any questions, feel free to submit a GitHub issue. You can find solutions to many common problems in the documentation: https://github.com/HassanBuTt78/repostly.git')

def cycle():
    try:
        posts = reddit.getPosts(SUBREDDIT, SCORE_CRITERIA)
        print(len(posts), " Videos Dicovered")
        for post in posts:
            temp = Post(post)
        queue.run(Post)
    except Exception as e:
        print(
            f'\u2193\u2193\u2193\u2193\u2193 ERROR \u2193\u2193\u2193\u2193\u2193 \n \n{e}\n\nTRYING AGAIN')

cycle()
schedule.every(4).hours.do(cycle)

while True:
    schedule.run_pending()
    time.sleep(1)