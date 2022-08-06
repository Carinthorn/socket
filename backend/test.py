
from flask import jsonify
from database.mongoDB import getDatabase
from bson.json_util import dumps, loads

def test():
    rooms = getDatabase()['room']
    cursor = rooms.find()
    list_cur = list(cursor)
    json_data = dumps(list_cur, indent=2)
    
    with open('data.json', 'w') as file:
        file.write(json_data)

    return jsonify(getDatabase()['rooms'])

test()