import requests
from json import loads

class User():
    def __init__(self, user):
        self.user = user
    def track(self):
        req = requests.get(f'https://api.github.com/users/{self.user}/events')
        data = loads(req.text)
        for i in data:
            if i['type'] == 'PushEvent':
                print(f"Pushed {i['payload']['size']} commit to {i['repo']['name']}")
            elif i['type'] == 'ReleaseEvent':
                print(f"Released in {i['repo']['name']}")
            elif i['type'] == 'CommitCommentEvent':
                print(f"A commit comment is created in {i['repo']['name']}")
            elif i['type'] == 'CreateEvent':
                if i['payload']['ref_type'] != 'repository':
                    print(f"The {i['payload']['ref']} {i['payload']['ref_type']} is created in {i['repo']['name']}")
                else:
                    print(f"The {i['repo']['name']} repository has been created")
            elif i['type'] == 'DeleteEvent':
                print(f"The {i['payload']['ref']} {i['payload']['ref_type']} has been deleted")
u = User('ornihex')
u.track()