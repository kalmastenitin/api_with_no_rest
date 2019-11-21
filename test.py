import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    r = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.status_code)
    print(r.json())

def create_resource():
    new_student = {
        'name' : 'gajodhar',
        'rollno' : '106',
        'marks' : '5',
        'teacher' : 'joshi',
        'f_subject' : 'biology'
    }
    r = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_student))
    print(r.status_code)
    print(r.json())

def update_resource(id):
    new_data = {
        'id':id,
        'marks':'5',
    }
    r = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())

def delete_resource(id):
    data = {
        'id':id,
    }
    r = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.status_code)
    print(r.json())

# delete_resource()
# update_resource(5)
# create_resource()
get_resource()
