import os

from dotenv import load_dotenv 

#需要有这个才能在当前文件加载 env文件 
load_dotenv()

#读取 env文件的 APP_NAME 并且赋值到 user_name 变量中
user_name = os.getenv("APP_NAME")
name = os.getenv("USER_NAME")

print(user_name)
print(name)

#读取 天气 密钥 如果读取成功，打印success 读取失败的话，打印fail
api_key = os.getenv("WEATHER_API_KEY")
if api_key:
    print("success")
else:
    print("fail")

weather_key = os.getenv("TEST_API_URL")
if weather_key:
    print("请求成功")
    print(f"{weather_key[:20]}")
else:
    print("fail")



