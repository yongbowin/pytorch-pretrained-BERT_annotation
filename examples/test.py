# import re
#
# text = '小箭头。</p><p><imgsrc="28900480099"/>iiiiiiiiiiiiiiiiiiiii</p><p>2.点击小箭头，则就<a>是筛选</a>。'
#
#
# def remove_html(text):
#     reg = re.compile(r'<[^>]+>', re.S)
#     text = reg.sub('', text)
#
#     return text
#
#
# print(remove_html(text))


a = "This is a test。"
print(a[1:])
print(a.replace("。", ""))
