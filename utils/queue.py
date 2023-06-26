import json


def read_queue():
    with open('./utils/queue.json', 'r') as file:
        file = file.read()
        file = json.loads(file)
    return file

def write_queue(array):
    with open('./utils/queue.json', 'w') as file:
        file.write(json.dumps(array))

def in_queue(post):
    queue = read_queue()
    post = post.toDict()
    if post in queue:
        return True
    else:
        return False



def add(post):
    queue = read_queue()
    queue.append(post.toDict())
    write_queue(queue)
    return queue

def remove(post):
    post = post.toDict()
    queue = read_queue()
    if post in queue:
        queue.remove(post)
        print("Object removed from the queue.")
        write_queue(queue)
        return queue
    else:
        print("Object not found in the list.")
        return queue


def run(Post):
    queue = read_queue()
    print(f'{len(queue)} posts in queue')
    if len(queue)>0:
        post = queue[0]
        post = Post(post)
        print(f"uploading {post.title}")
        post.uploadVid()
        post.delete_file()
        remain = remove(post)
        print(f"{len(remain)} left in the queue")
    else:
        print("Queue is Empty")