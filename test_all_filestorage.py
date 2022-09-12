#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()
classes = {
                     'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                     'Review': Review
                    }
print("All: {}".format(fs.all()))
print("State: {}".format(fs.all(State)))
