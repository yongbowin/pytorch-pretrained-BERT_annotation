import json

base_path = "/home/wyb/data/squad_v1.1/"
train_file_name = "train-v1.1.json"
dev_file_name = "dev-v1.1.json"
input_file = base_path + train_file_name

with open(input_file, "r", encoding='utf-8') as reader:
    input_data = json.load(reader)["data"]

# dic = {'a': 1, 'b': 2, 'c': 3}
# js = json.dumps(input_file, sort_keys=True, indent=4, separators=(',', ':'))
# print(js)

print(len(input_data))
print(input_data[0])
print(input_data[1])
print(type(input_data[1]))