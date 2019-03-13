import re
import json

BASE_PATH = "/home/wyb/Downloads/"


with open(BASE_PATH + "test_result.json", "r", encoding="utf-8") as f:
    res = f.readlines()  # list, len=120000

# text = "This is a \n file \r that \r hello\r!"


def clean_sepc_char(text):
    replace_p = ["\t", "\n", "\r", "\u3000", "<splitter>", "/>"]
    for i in replace_p:
        if i in text:
            text = text.replace(i, "")

    return text


def E_trans_to_C(string):
    """
    transformer english char to chinese
    """
    E_pun = u',.!?[]()<>"\''
    C_pun = u'，。！？【】（）《》“‘'
    table = {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}

    return string.translate(table)


# for i in res:
#     data = json.loads(i)
#     if "&amp" in data["answers"][0]:
#         print(data)


# cate_type = set()  # {'DESCRIPTION', 'YES_NO', 'ENTITY'}
# for i in res:
#     data = json.loads(i)
#     if data["question_type"] == "YES_NO":
#         print(data)


# text = '小箭头。</p><p><imgsrc="28900480099"/>iiiiiiiiiiiiiiiiiiiii</p><p>2.点击小箭头，则就是筛选。'


def remove_html(text):
    reg = re.compile(r'<[^>]+>', re.S)
    text = reg.sub('', text)

    return text


"""
{
"question_id": 403770, 
"question_type": "YES_NO", 
"answers": ["我都是免费几分钟测试可以玩而已。"], 
"entity_answers": [[]], 
"yesno_answers": []
}
"""
json_list = []
for i in res:
    item_dict = {}

    data = json.loads(i)
    text = data["answers"][0]
    text = clean_sepc_char(text)
    text = remove_html(text)
    text = E_trans_to_C(text)

    item_dict["question_id"] = data["question_id"]
    item_dict["question_type"] = data["question_type"]
    item_dict["answers"] = [text]
    item_dict["entity_answers"] = data["entity_answers"]
    item_dict["yesno_answers"] = data["yesno_answers"]

    json_list.append(item_dict)

# ================ write to file ================
with open(BASE_PATH + "test_result_rm.json", 'w') as fout:
    for pred_answer in json_list:
        fout.write(json.dumps(pred_answer, ensure_ascii=False) + '\n')



