import json

# BASE_PATH = "/home/wyb/PycharmProjects/DuReader/data/demo/"
BASE_PATH = "/DATA/disk1/wangyongbo/lic2019/DuReader/data/preprocessed/"

with open(BASE_PATH + "trainset/search.train_bert.json", "r", encoding='utf-8') as reader:
    source = json.load(reader)
    input_data = source["data"]

cou_equal = 0
cou_total = 0
for entry in input_data:
    for paragraph in entry["paragraphs"]:
        paragraph_text = paragraph["context"]

        for qa in paragraph["qas"]:
            cou_total += 1

            """
            {
                'text': 'in the late 1990s',
                'answer_start': 269  # by char
            }
            """
            answer_dict = qa["answers"][0]
            answer = answer_dict["text"]
            start_position = answer_dict["answer_start"]  # by word
            end_position = answer_dict["answer_end"]  # by word

            if paragraph_text[start_position:(end_position+1)] == answer.strip():
                cou_equal += 1

print("cou_equal / cou_total = ", cou_equal, " / ", cou_total)
