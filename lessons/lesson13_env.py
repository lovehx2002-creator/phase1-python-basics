import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
user_name = os.getenv("USER_NAME")
daily_study_hours = os.getenv("DAILY_STUDY_HOURS")

print("=== 环境变量读取结果 ===")
print(f"应用名称：{app_name}")
print(f"用户名{user_name}")
print(f"每日学习小时数：{daily_study_hours}")
print(f"daily_study_hours的类型：{type(daily_study_hours)}")

print(" ==== 类型转换 ====")

daily_hours_number = float(daily_study_hours)
weekly_hours = daily_hours_number * 5

print(f"每周学习时间：{weekly_hours}小时")


print("=== 读取不存在的变量 ===")

api_key = os.getenv("FAKE_API_KEY")

if api_key:
    print("已经读取到 API key")
else:
    print("没有读取到")

print("=== 模拟读取天气 API Key ===")

weather_api_key = os.getenv("WEATHER_API_KEY")

if weather_api_key:
    print("天气API Key 已经读取成功")
    print(f"Key 前 4 位：{weather_api_key[:4]}***")
else:
    print("没有读取到 WEAEHER_API_KEY，请检查 .env 文件")
