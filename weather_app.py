# Phase 1 Milestone Project：Weather CLI APP v1

weather_data = {
    "Los Angeles" :{
        "temperature" : 26,
        "condition" : "sunny",
        "humidity" : 45
    },
    "Tokyo" : {
        "temperature" : 22,
        "condition" : "cloudy",
        "humidity" : 60
    },
    "Singapore" :{
        "temperature" : 30,
        "condition" : "Rainy",
        "humidity" : 80
    }
}

def get_weather(city):
    return weather_data[city]

def print_weather(city,weather):
    print("==== 天气查询结果 ====")
    print(f"城市：{city}")
    print(f"温度：{weather['temperature']}°C")
    print(f"天气：{weather['condition']}")
    print(f"温度：{weather['humidity']}%")

city = input("请输入城市名：")

try:
    weather = get_weather(city)
    print_weather(city,weather)
except KeyError:
    print("没有找到这个城市的天气数据。")
    print("当前支持的城市：los Angeles，Tokyo，Singapore")
