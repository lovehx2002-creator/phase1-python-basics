# Phase 1 - Lesson 11 - JSON

import json

weather = {
    "city": "北京",
    "temperature": 30,
    "condition": "晴",
    "humidity": 60}

print("=== Python 字典 ===")
print(weather)
print(type(weather))

joson_text = json.dumps(weather, ensure_ascii=False,indent = 4)

print("==== JSON 字符串 ====")
print(joson_text)
print(type(joson_text))

print("=== JSON 字符串转回 Python 字典 ====")

new_weather = json.loads(joson_text)

print(new_weather)
print(type(new_weather))
print(f"城市：{new_weather['city']}")
print(f"温度：{new_weather['temperature']}°C")

print("==== JSON文件写入 ====")
with open("data/weather.json","w",encoding="utf-8") as file:
    json.dump(weather,file,ensure_ascii=False,indent=4)

print("weather.json 文件写入完成。")

print("==== JSON文件读取 ====")
with open("data/weather.json","r",encoding="utf-8") as file:
    loaded_weather = json.load(file)

print(loaded_weather)
print(type(loaded_weather))
print(f"读取到的城市：{loaded_weather['city']}")
print(f"读取到的温度：{loaded_weather['temperature']}°C")
