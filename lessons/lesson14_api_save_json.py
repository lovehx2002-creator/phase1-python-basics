import os
import json
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("TEST_API_URL")

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

output_file = data_folder / "api_result.json"

print("=== API 请求与保存 JSON ===")

if not api_url:
    print("没有读取到 TEST_API_URL，请检查 .env 文件")
else:
    try:
        response = requests.get(api_url,timeout=10)
        response.raise_for_status()

        data = response.json()

        print("请求成功")
        print(f"状态码:{response.status_code}")
        print(f"请求地址:{data.get('url','没有url字段')}")
        print(f"来源IP:{data.get('origin','没有origin字段')}")

        with open(output_file,"w",encoding = "utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=2)
        
        print(f"API 返回结果已经保存到：{output_file}")

    except requests.exception.Requestion as error:
        print("请求失败：")
        print(error)

    except ValueError as error:
        print("JSON 解析失败：")
        print(error)