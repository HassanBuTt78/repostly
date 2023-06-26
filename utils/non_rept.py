import json



def check(post):
    id = post.id
    with open('./utils/processed.json', 'r') as file:
        file = file.read()
        file = json.loads(file)
        processed = file
    for post in processed:
        if id == post['id']:
            return True
    return False
    
    


def store_record(postClass):
    processed = []
    with open('./utils/processed.json', 'r') as file:
        file = file.read()
        file = json.loads(file)
        processed = file
    postClass = postClass.toDict()
    processed.append(postClass)
    file = open('./utils/processed.json', 'w')
    processed = json.dumps(processed)
    file.write(processed)
    print('Record Saved')


