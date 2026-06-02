# Phase 1 - Lesson 12: requests

import requests

url = "https://httpbin.org/get"

#response = requests.get(url)

#print("=== 响应状态码 ===")
#print(response.status_code)

#data = response.json()

#print("=== JSON 转换成 Python 字典 ===")
#print(type(data))


#print("=== 响应内容类型 ===")
#print(type(response.text))

#print("=== 前300个字符 ===")
#print(response.text[:300])

#print("=== 部分字段 ===")
#print(f"current_user_url:{data['current_user_url']}")
#print(f"user_url:{data['user_url']}")
#print(f"repository_url:{data['repository_url']}")

# 解决异常

try:
    response = requests.get(url,timeout=10)
    response.raise_for_status()

    data = response.json()



    print("=== org API 请求成功 ===")
    print(f"状态码：{response.status_code}")
   # print(f"currents_user_url:{data['current_user_url']}")

    print("==== 返回数据字段 ====")
    #print(f"user_url:{data['user_url']}")
    print(f"url:{data['url']}")
    print(f"origin:{data['origin']}")
    print(f"header 类型：{type(data['headers'])}")
    #print(f"repository_url:{data['repository_url']}")

except requests.exceptions.RequestException as e:
    print("=== org API 请求失败 ===")
    print(f"错误信息：{e}") 
