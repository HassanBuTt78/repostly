from .tiktok_selenium import upload_tiktok, login


def upload(post):
    upload_tiktok(post.title, post.localPath, post.tags)


def manual_login():
    login()
