import json

with open("nbest_predictions.json", "r") as f:
    data_n = json.load(f)

"""
{
    'text': '手 账 ， 指 用 于 记 事 的 本 子 。', 
    'probability': 0.8307071064735555, 
    'start_logit': 8.693561553955078, 
    'end_logit': 8.59373664855957
}
"""
nbest_para = []
para_dict = {}
for k, v in data_n.items():
    id = k.split("_")[0]
    prob = 0
    text = ""
    for sents in v:
        if sents["probability"] > prob:
            prob = sents["probability"]
            text = sents["text"]
    para_dict["id"] = id
    para_dict["prob"] = prob
    para_dict["text"] = text

    if nbest_para:
        for item in nbest_para:
            if id == item["id"]:
                if prob > item["prob"]:
                    item["prob"] = prob
                    item["text"] = text
            else:
                nbest_para.append(para_dict)
    else:
        nbest_para.append(para_dict)
