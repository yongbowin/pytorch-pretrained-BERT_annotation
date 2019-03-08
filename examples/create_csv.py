import json
import csv
import re


"""
{
  "question_id": 186358,
  "question_type": "YES_NO",
  "question": "上海迪士尼可以带吃的进去吗",
  "documents": [
    {
      'paragraphs': ["text paragraph 1", "text paragraph 2"]
    },
    ...
  ],
  "answers": [
    "完全密封的可以，其它不可以。",      // answer1
    "可以的，不限制的。只要不是易燃易爆的危险物品，一般都可以带进去的。",   //answer2
    "罐装婴儿食品、包装完好的果汁、水等饮料及包装完好的食物都可以带进乐园，",
    "但游客自己在家制作的食品是不能入园，因为自制食品有一定的安全隐患。"  // answer3
  ],
  "yesno_answers": [
    "Depends",                      // corresponding to answer 1
    "Yes",                          // corresponding to answer 2
    "Depends"                       // corresponding to asnwer 3
  ]
}
"""

PATH = '/home/wangyongbo/2019rc/DuReader_test/data/preprocessed/'
OUTPUT_PATH = '/home/wangyongbo/2019rc/DuReader_test/data/yesno/'


def clean_text(text):
    replace_p = ["\t", "\n", "\r", "\u3000", "<splitter>", "/>"]
    for i in replace_p:
        if i in text:
            text = text.replace(i, "")

    reg = re.compile(r'<[^>]+>', re.S)
    text = reg.sub('', text)
    return text


def write_2_csv():
    path_list = []
    for dataset in ["trainset", "devset", "testset"]:
        for source in ["search", "zhidao"]:
            if dataset == "trainset":
                file = PATH + dataset + "/" + source + ".train.json"
            if dataset == "devset":
                file = PATH + dataset + "/" + source + ".dev.json"
            if dataset == "testset":
                file = PATH + dataset + "/" + source + ".test.json"
            path_list.append(file)

    for file in path_list:
        # read json file
        with open(file, "r", encoding="utf-8") as f:
            res_list = f.readlines()
            # print("Total nums: ", len(res_list))

        yes_no_rows = [["question", "answer", "label"]]  # append title line
        for item in res_list:
            line = json.loads(item)
            if 'yesno_answers' in line:
                if line['yesno_answers']:
                    for i in zip(line['answers'], line['yesno_answers']):
                        new_line = []
                        new_line_clean = []
                        question = line['question']
                        new_line.append(question)
                        new_line.extend(list(i))

                        if "No_Opinion" not in new_line:
                            for item in new_line:
                                new_line_clean.append(clean_text(item))
                            yes_no_rows.append(new_line_clean)

        # write csv file
        output_file = OUTPUT_PATH + file.split("/")[-1].replace("json", "yesno.csv")
        with open(output_file, 'w') as fout:
            f_csv = csv.writer(fout)
            f_csv.writerows(yes_no_rows)
            print(output_file.split("/")[-1] + " finished!")


write_2_csv()
