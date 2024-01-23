import json
file_path = "ecommerce_data.json"
def load_data():
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data