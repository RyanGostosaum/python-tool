import csv

from controllers.create_json import create_json

csv_file_path = './content/pornhub.com-db.csv'

json_file_path = './result/result.json'

data = {}

with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader: 
        data = rows

create_json(json_file_path, data)