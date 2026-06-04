import json
from pathlib import Path

weather = {
    "city" : "北京",
    "temperature":30,
    "condition":"sunny",
    "humidity":60
}

#输出内容
print(weather)
#其实python 中 dict 是一个数据类型。
print(type(weather))

#下面这个是采用json模块里的dumps（）方法，把dict 转化为 json类型格式
json_text = json.dumps(weather,ensure_ascii=False,indent=4)
print(json_text)
print(type(json_text))

#将 json模块 重新变为 dict
return_weather = json.loads(json_text)
print(return_weather)
print(type(return_weather))



with open("data/weather.json","w",encoding="utf-8") as file:
    json.dump(weather,file,ensure_ascii=False,indent=3)

#选择保存的文件路径
folder = Path("./data02")

#保存文件的文件名
jsontxt = folder/"weather.json"

#保存文件的代码
with open(jsontxt,"w",encoding="utf-8") as file:
    json.dump(weather,file,ensure_ascii=False,indent=4)


#读取保存的 json文件
with open(jsontxt,"r",encoding="utf-8") as file:
    #print(file.read())
    content = json.load(file)
print(content)
print(type(content))
#print(type(json_text))
