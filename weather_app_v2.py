# Phase 1 Milestone Project: Weather CLI App V2

import json
from pathlib import Path


weather_data = {
    "los angeles": {
        "display_name": "Los Angeles",
        "temperature": 26,
        "condition": "Sunny",
        "humidity": 45,
    },
    "tokyo": {
        "display_name": "Tokyo",
        "temperature": 22,
        "condition": "Cloudy",
        "humidity": 60,
    },
    "singapore": {
        "display_name": "Singapore",
        "temperature": 30,
        "condition": "Rainy",
        "humidity": 80,
    },
}


data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

history_file = data_folder / "weather_history.json"


def normalize_city_name(city):
    return city.strip().lower()


def get_weather(city):
    normalized_city = normalize_city_name(city)
    return weather_data[normalized_city]


def print_weather(weather):
    print("=== 天气查询结果 ===")
    print(f"城市：{weather['display_name']}")
    print(f"温度：{weather['temperature']}°C")
    print(f"天气：{weather['condition']}")
    print(f"湿度：{weather['humidity']}%")


def load_history():
    if not history_file.exists():
        return []

    with open(history_file, "r", encoding="utf-8") as file:
        return json.load(file)


def save_history_record(city, weather):
    history = load_history()

    record = {
        "city": weather["display_name"],
        "temperature": weather["temperature"],
        "condition": weather["condition"],
        "humidity": weather["humidity"],
    }

    history.append(record)

    with open(history_file, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)


def show_supported_cities():
    print("当前支持的城市：Los Angeles, Tokyo, Singapore")


city = input("请输入城市名：")

try:
    weather = get_weather(city)
    print_weather(weather)
    save_history_record(city, weather)
    print(f"查询历史已保存到：{history_file}")
except KeyError:
    print("没有找到这个城市的天气数据。")
    show_supported_cities()
except json.JSONDecodeError:
    print("查询历史文件格式错误，请检查 weather_history.json。")