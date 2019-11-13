import json

def create_json(path, data):
    with open(path, 'w') as json_file:
        json_file.write(json.dumps(data, indent = 4))
        print('CSV successfully converted')