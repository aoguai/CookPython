# CookPython
好的，今天我们来做菜！(python实现版本)

对原项目的python实现。支持模糊查找。同时提供了json数据。
## 参考

- [隔离食用手册大全](https://docs.qq.com/sheet/DZUpJS0tQZm1YYWlt)
- [YunYouJun/cook: 🍲 好的，今天我们来做菜！](https://github.com/YunYouJun/cook)

## 说明

本项目初衷是方便特殊时期隔离在家而材料有限的小伙伴，因此菜谱材料会尽量限制在特定范围内。

## 演示
```python
if __name__ == "__main__":
    print(get_cook("牛肉、洋葱"))
```
### 输出
```
>>>未找到精准关键词，模糊搜索到以下内容：
>>>电饭煲罗宋汤丨牛肉、番茄、洋葱、芹菜、胡萝卜、土豆、卷心菜
>>>B站教程BV号：https://www.bilibili.com/video/BV16Q4y1m7nU
>>>难度：简单丨标签：杂烩
>>>方法：丨工具：电饭煲
>>>胡萝卜炖牛肉丨胡萝卜、牛肉、洋葱
>>>B站教程BV号：https://www.bilibili.com/video/BV1UR4y1V7nV
>>>难度：困难丨标签：法式
>>>方法：炖丨工具：一口大锅
>>>烧汁牛肉粒丨牛肉、洋葱、菌菇
>>>B站教程BV号：https://www.bilibili.com/video/BV1NU4y1d7ot
>>>难度：普通丨标签：国宴菜
>>>方法：炒丨工具：一口大锅
>>>番茄土豆炖牛腩丨牛肉、土豆、番茄、洋葱
>>>B站教程BV号：https://www.bilibili.com/video/BV1344y1n73V
>>>难度：普通丨标签：下饭
>>>方法：煮丨工具：一口大锅
>>>法式胡萝卜炖牛肉丨胡萝卜、牛肉、洋葱
>>>B站教程BV号：https://www.bilibili.com/video/BV1UR4y1V7nV
>>>难度：困难丨标签：
>>>方法：炖丨工具：一口大锅
>>>辣味牛肉凉拌小黄瓜丨黄瓜、牛肉、洋葱
>>>B站教程BV号：https://www.bilibili.com/video/BV1qr4y1Y792
>>>难度：简单丨标签：
>>>方法：丨工具：一口大锅
>>>洋葱虾仁滑蛋丨鸡蛋、牛肉、洋葱、虾
>>>B站教程BV号：https://www.bilibili.com/video/BV1uE411N7AN
>>>难度：丨标签：
>>>方法：丨工具：一口大锅
```
