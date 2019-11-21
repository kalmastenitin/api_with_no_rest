import json

def valid_json(data):
    try:
        json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
