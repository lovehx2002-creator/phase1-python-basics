# Phase 1 - lesson 6 - function

def say_hello():
    print("hello,Phase 1 python!")

say_hello()

print("=== 带参数的函数 ===")

def introduce(name,city):
    print(f"你好，我叫{name}，我来自{city}。")

introduce("小明","北京")
introduce("小红","上海")


print("=== 有返回值的函数 ===")
def calculate_weekly_hours(hours_per_day,days_per_week):
    weekly_hours = hours_per_day * days_per_week
    return weekly_hours

result = calculate_weekly_hours(2,5)
print(f"每周学习时间：{result}小时")


print("=== 函数处理字典 ===")
weather = {
    "city": "北京",
    "temperature": 30,
    "condition": "晴",
    "humidity": 60
}

def print_weather(weather_data):
    print(f"城市：{weather_data["city"]}")
    print(f"温度：{weather_data["temperature"]}°C")
    print(f"天气：{weather_data["condition"]}")
    print(f"湿度：{weather_data["humidity"]}%")

print_weather(weather)