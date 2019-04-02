import json

BASE_PATH = "/DATA/disk1/wangyongbo/lic2019/DuReader/data/extracted/"


with open(BASE_PATH + "dureader/predictions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open(BASE_PATH + "dureader/predictions_filter.json", "r", encoding="utf-8") as f:
    data_filter = json.load(f)

with open(BASE_PATH + "devset/zhidao.dev.json", "r", encoding='utf-8') as f1:
    lines = f1.readlines()

# nbest_para = get_best_ans()

for line in lines:  # raw
    sample = json.loads(line)
    ans_list = []
    for k, v in data.items():  # pred
        if str(sample["question_id"]) == (str(k)).split("_")[0]:
            ans_list.append(v[0])
    print("------------------------------------------------------")
    print("question_id: " + (str(k)).split("_")[0])
    if sample["fake_answers"]:
        print("fake_answers: \n" + str(sample["fake_answers"][0]))

    print(" ")

    print("answer: count=" + str(len(sample["answers"])))
    for idx,ans_item in enumerate(sample["answers"]):
        print(str(idx) + "==> " + ans_item)

    print(" ")

    print("pred answer: count=" + str(len(ans_list)))
    answer_docs_id = -1
    if "answer_docs" in sample and sample["answer_docs"] and sample["answer_docs"][0] < len(ans_list):
        answer_docs_id = sample["answer_docs"][0]

    for idx, ans_item in enumerate(ans_list):
        state1 = ""  # flag of 'has fake_answers'
        state2 = ""  # flag of 'best answers'
        for k1, v1 in data_filter.items():
            if v1 == ans_item:
                state2 = "(pred BEST answers)"

        if idx == answer_docs_id:
            state1 = "(has fake_answers)"

        print(str(idx) + "==>" + state1 + state2 + " " + ans_item)








