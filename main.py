from json import loads
from re import compile
import os


# 取菜谱json
def get_record():
    url = "./menu.json"
    if not os.path.isfile(url):
        return "菜谱获取失败"
    fo = open(url, "r", encoding='utf-8')
    ele_json = loads(fo.read())
    return ele_json


# 模糊搜索
def fuzzyfinder(user_input, collection_key_list):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = compile(pattern)  # Compiles a regex.
    a = 0
    for item in collection_key_list:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append(a)
        a = a + 1
    return suggestions


def get_cook(key):
    # 进一步解析资源json
    al_dict = get_record()
    collection_key = []  # 用来模糊匹配的key
    for b in al_dict['ingredients']:
        collection_key.append(b)
    fuzzyfinder_i_list = fuzzyfinder(key, collection_key)  # 模糊搜索资源
    fuzzyfinder_i_len = len(fuzzyfinder_i_list)
    if fuzzyfinder_i_len > 0:
        if collection_key[fuzzyfinder_i_list[0]].replace("、", "") == key.replace("、", ""):
            "".join([al_dict['name'][fuzzyfinder_i_list[0]], "丨", al_dict['ingredients'][fuzzyfinder_i_list[0]],
                     "\nB站教程BV号：", al_dict['url'][fuzzyfinder_i_list[0]], "\n难度：",
                     al_dict['difficulty'][fuzzyfinder_i_list[0]], "丨标签：", al_dict['tag'][fuzzyfinder_i_list[0]],
                     "\n方法：", al_dict['practice'][fuzzyfinder_i_list[0]], "丨工具：",
                     al_dict['tool'][fuzzyfinder_i_list[0]]])
            return
        else:
            re_text = "未找到精准关键词，模糊搜索到以下内容：\n"
            for c in fuzzyfinder_i_list:
                re_text = "".join(
                    [re_text, al_dict['name'][c], "丨", al_dict['ingredients'][c], "\nB站教程BV号：",
                     al_dict['url'][c], "\n难度：", al_dict['difficulty'][c],
                     "丨标签：", al_dict['tag'][c], "\n方法：", al_dict['practice'][c],
                     "丨工具：", al_dict['tool'][c], "\n"])

            return re_text
    else:
        content = "".join(["未找到" + key + "相关菜谱"])
        return content


if __name__ == "__main__":
    print(get_cook("牛肉、洋葱"))
