import json

BASE_PATH = "/home/wyb/PycharmProjects/DuReader/data/demo/"


with open(BASE_PATH + "trainset/search.train.json", "r", encoding='utf-8') as reader:
    source = reader.readlines()

    # source = json.load(reader)
    # input_data = source["data"]
    # version = source["version"]


# print(len(source))
# print(type(source))  # <class 'list'>

"""
keys: (one documents)
    documents
    answer_spans
    fake_answers
    question
    segmented_answers
    answers
    answer_docs
    segmented_question
    question_type
    question_id
    fact_or_opinion
    match_scores
"""
line_json = json.loads(source[0])
for i in line_json.keys():
    print(i)




