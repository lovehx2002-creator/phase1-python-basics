import requests

url = "https://httpbin.org/getaa"

#请求 访问 API 地址
try:
    response = requests.get(url)

    #查看 返回请求码 ，观察哪个请求是真的 请求成功
    print(response.status_code)

    # 接收返回的数据 是返回的 json 形式，但是后面 通过json（）方法 变成了 dict形式
    data = response.json()
    print(data)
    print(type(data))

    # 这个返回的 是json 数据形式， 使用 text属性 然后直接输出 json 类型
    print(response.text)
    print(type(response.text))

#写 try / except 是为了防止程序崩溃。
except requests.exceptions.RequestException as e:
    print(f"请求失败，报错为{e}")


    

