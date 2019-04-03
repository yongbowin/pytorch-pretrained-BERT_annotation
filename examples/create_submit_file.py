import json

BASE_PATH = "/DATA/disk1/wangyongbo/lic2019/DuReader/official_data/extracted/"

"""
/DATA/disk1/wangyongbo/lic2019/DuReader/official_data/extracted/test1set

{
    "question_id": 397032, 
    "question_type": "ENTITY", 
    "answers": ["浙江绿谷，秀山丽水。"], 
    "entity_answers": [[]], 
    "yesno_answers": []
}
"""
datasets = ["search", "zhidao"]
for dataset in datasets:
    with open(BASE_PATH + "results/predictions_first_filter_" + dataset + ".json", "r") as f:
        data_n = json.load(f)

    with open(BASE_PATH + "test1set/" + dataset + ".test1.json", "r", encoding="utf-8") as f:
        lines = f.readlines()

    res = []
    test_ids = []
    pred_search_ids = []
    for line in lines:
        line_json = json.loads(line)
        # avoid loss sample in predictions, save all ids to a list.
        test_ids.append(int(line_json["question_id"]))
        for k, v in data_n:
            pred_search_ids.append(int(k))
            if str(line_json["question_id"]) == str(k):
                res_line = {}
                res_line["question_id"] = int(k)
                res_line["question_type"] = line_json["question_type"]
                res_line["answers"] = [v]
                res_line["entity_answers"] = [[]]
                res_line["yesno_answers"] = []
                res.append(res_line)

    if len(res) != 30000:
        # fill in loss sample with "" (no answer)
        for id in test_ids:
            if id not in pred_search_ids:
                for line in lines:
                    line_json = json.loads(line)
                    if str(line_json["question_id"]) == str(id):
                        res_line = {}
                        res_line["question_id"] = int(id)
                        res_line["question_type"] = line_json["question_type"]
                        res_line["answers"] = [""]
                        res_line["entity_answers"] = [[]]
                        res_line["yesno_answers"] = []
                        res.append(res_line)

    with open(BASE_PATH + "results/test_result_" + dataset + ".json", 'w') as fout:
        for pred_answer in res:
            fout.write(json.dumps(pred_answer, ensure_ascii=False) + '\n')
