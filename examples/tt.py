


def E_trans_to_C(string):
    E_pun = u',.!?[]()<>"\''
    C_pun = u'，。！？【】（）《》“‘'
    table= {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}
    return string.translate(table)


s1 = '这里包含英文字符.'
s2 = E_trans_to_C(s1)
print(s2)
