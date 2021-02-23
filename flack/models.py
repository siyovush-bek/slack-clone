import json

users = set()


class Channel:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.messages = []
    
    def __repr__(self):
        return f'{self.name}'

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            return True
    
    def add_message(self, msg):
        self.messages.append(msg)
    
    def remove_member(self, member):
        if member not in self.members:
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
    
    def __str__(self):
        return self.content

    @staticmethod
    def from_json(json_object):
        if(isinstance(json_object, str)):
            json_object = json.loads(json_object)

        return Message(
            json_object['content'],
            json_object['date'],
            json_object['sender']
        )