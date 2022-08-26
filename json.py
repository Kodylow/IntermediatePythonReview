import json
j = {
    "firstname": "John",
    "lastname": "Doe",
    "hobbies": [
        "coding",
        "programming"
    ],
    "city": "unknown",
    "doxxed": False
}

to_json = json.dumps(person, indent=4, sort_keys=True)

# Serialize to json from python
with open('example.json', 'w') as file:
    json.dump(to_json, file, indent=4)

# Deserialize json to python
with open('example.json', 'r') as file:
    x = json.load(file)


# Serialize python class as json
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {
            'name': o.name,
            'age': o.age,
            o.__class__.__name__: True
        }
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)


# Alternatively...
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {
                'name': o.name,
                'age': o.age,
                o.__class__.__name__: True
            }
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)

# Or
userJSON = UserEncoder().encode(user)

# Json to python dict to User object
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct
user = json.loads(userJSON, object_hook=decode_user)
