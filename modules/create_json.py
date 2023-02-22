import os
import json

def find_path_to_file(name_file):
    abs_path = os.path.abspath(__file__)
    abs_path = os.path.split("\\")
    del abs_path[-1]
    abs_path = os.path.join(abs_path, name_file)

def create_json(name_json,name_dict):
    with open(name_json, "w") as file:
        json.dump(name_dict, file, indent=4, ensure_ascii=True)

def read_json(name_json):
    with open(name_json, "r") as file:
        data = json.load(file)
        return data