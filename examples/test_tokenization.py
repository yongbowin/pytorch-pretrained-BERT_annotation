import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenized input
text = "[CLS] Who 这是一个测试 was Jim Henson ? [SEP] Jim Henson was a puppeteer [SEP]"  # test version
# text = "[CLS] Who was Jim Henson ? [SEP] Jim Henson was a puppeteer [SEP]"

"""
tokenized_text:
    ['[CLS]', 'who', '[UNK]', '[UNK]', '一', '[UNK]', '[UNK]', '[UNK]', 'was', 'jim', 'henson', '?', '[SEP]', 
        'jim', 'henson', 'was', 'a', 'puppet', '##eer', '[SEP]']
"""
tokenized_text = tokenizer.tokenize(text)

# Mask a token that we will try to predict back with `BertForMaskedLM`
masked_index = 8
tokenized_text[masked_index] = '[MASK]'
# assert tokenized_text == \
#        ['[CLS]', 'who', 'was', 'jim', 'henson', '?', '[SEP]', 'jim', '[MASK]', 'was', 'a',
#         'puppet', '##eer', '[SEP]']

# test version
assert tokenized_text == \
       ['[CLS]', 'who', '[UNK]', '[UNK]', '一', '[UNK]', '[UNK]', '[UNK]', '[MASK]', 'jim', 'henson', '?',
        '[SEP]', 'jim', 'henson', 'was', 'a', 'puppet', '##eer', '[SEP]']

# Convert token to vocabulary indices
"""
indexed_tokens:
    [101, 2040, 100, 100, 1740, 100, 100, 100, 103, 3958, 27227, 1029, 102, 3958, 27227, 2001, 1037, 13997, 11510, 102]
"""
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
# Define sentence A and B indices associated to 1st and 2nd sentences (see paper)
# segments_ids = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# test version
segments_ids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

"""
tokens_tensor:
    tensor([[  101,  2040,   100,   100,  1740,   100,   100,   100,   103,  3958,
             27227,  1029,   102,  3958, 27227,  2001,  1037, 13997, 11510,   102]])

segments_tensors:
    tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]])
"""
# Convert inputs to PyTorch tensors
tokens_tensor = torch.tensor([indexed_tokens])
segments_tensors = torch.tensor([segments_ids])

