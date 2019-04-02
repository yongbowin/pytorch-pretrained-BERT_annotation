import json

with open("predictions.json", "r") as f:
    data_n = json.load(f)

nbest_para = []
for k, v in data_n.items():
    para_dict = {}
    id = k.split("_")[0]
    prob = 0
    text = ""

    if float(v[-1]) > prob:
        para_dict["id"] = id
        para_dict["text"] = v[0]

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
#--------------------------------------------------
best_res = {}
for k1, v1 in data_n.items():
    best_sample = {}
    id1 = k1.split("_")[0]
    if id1 in best_res:
        continue
    best_sample["id"] = id1
    best_sample["prob"] = float(v1[-1])
    best_sample["text"] = v1[0]

    for k2, v2 in data_n.items():
        if id1 == k2.split("_")[0] and float(v2[-1]) > float(v1[-1]):
            best_sample["prob"] = float(v2[-1])
            best_sample["text"] = v2[0]

    best_res[id1] = best_sample["text"]

with open("predictions_filter.json", "w") as writer:  # predictions.json
    writer.write(json.dumps(best_res, indent=4) + "\n")