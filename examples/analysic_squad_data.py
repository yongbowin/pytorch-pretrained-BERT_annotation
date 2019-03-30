import json

BASE_PATH = "/home/wyb/data/squad_v2.0/"


with open(BASE_PATH + "train-v2.0.json", "r", encoding='utf-8') as reader:
    source = json.load(reader)
    input_data = source["data"]
    version = source["version"]
#
#
# examples = []
# for entry in input_data:
#     """
#     entry format:
#         {"title": xxx, "paragraphs": xxxx}
#     """
#     for paragraph in entry["paragraphs"]:
#
#         paragraph_text = paragraph["context"]


paragraph_text = 'Beyoncé Giselle Knowles-Carter (/biːˈjɒnseɪ/ bee-YON-say).'
doc_tokens = []
char_to_word_offset = []
prev_is_whitespace = True
for c in paragraph_text:  # by char
    if is_whitespace(c):
        prev_is_whitespace = True
    else:
        if prev_is_whitespace:
            doc_tokens.append(c)
        else:
            doc_tokens[-1] += c
        prev_is_whitespace = False
    char_to_word_offset.append(len(doc_tokens) - 1)

print(doc_tokens)
print("----------------")
print(char_to_word_offset)





