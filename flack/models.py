import json

users = set()


class Channel:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.messages = []
    
    def __repr__(self):
        return f'{self.name} ({len(self.members)} members)'

    def add_member(self, member):
        self.members.append(member)
    
    def add_message(self, msg):
        self.messages.append(msg)
    
    def remove_member(self, member):
        self.members.remove(member)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


class Message:
    def __init__(self, content, date, sender):
        self.content = content
        self.date = date
        self.sender = sender

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    @staticmethod
    def from_json(json_object):
        if(isinstance(json_object, str)):
            json_object = json.loads(json_object)

        return Message(
            json_object['content'],
            json_object['date'],
            json_object['sender']
        )