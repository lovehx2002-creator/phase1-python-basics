# Phase 1: Python 地基

## 当前阶段

Phase 1: python 地基

## 本阶段重点

- python 语法基础
- 函数
- 数据结构
- 文件读写
- 异常处理
- 虚拟环境
- requests
- json
- python-dotenv

## 今日记录

- 创建pahse 1 项目目录
- 出书话Git 仓库
- 创建 README.md / notes.md /debug-log.md/main.py

## 虚拟环境
虚拟环境相当于一个小房间，不希望把每个项目都往系统python里面乱包装

给项目创建虚拟环境：python3 -m venv .venv

创建完虚拟环境需要激活：source .venv/bin/activate

## lesson 4:list 和 for 循环

学习了列表和for循环。

- list 用来保存一组数据
- for 可以逐个处理列表里的元素
- len() 可以用来统计列表长度
- append() 可以往列表最后添加新的元素

以后处理多个城市，多个文件，多个用户消息，搜索多个结果的时候，都会用到列表和循环。

## lesson 5:dict 字典

学习了 python 字典结构
- dict 用来保存 key-value 数据
- key 是字段名， value 是字段值
- 可以通过 student["name"] 读取字段值
- 可以通过 student["phase"] = "xxx" 修改字段
- 可以通过 student.item() 遍历所有字段

字段很重要，因为后面API返回的JSON数据，经常会被python转成dict来处理。

## Lesson 6: function 函数

学习了函数

- def 用来定义函数
- 函数不会自动执行，需要调用
- 参数可以把外部数据传进函数
- return 可以把函数内部结果返回出来
- 函数可以让代码复用，避免重复写出同样的逻辑

后面天气查询工具会用函数来拆分功能，比如说获取天气，解析数据，格式化输出

## Lesson 7:input 和类型转换

学习了input（） 和类型转换

- input（） 可以收用户在终端输入的内容
- input（） 得到的内容默认是字符串
- int（）可以把字符串转成整数
- float（） 可以吧字符串转成小数

后面的天气查询CLI工具会用input（）接收用户输入的城市名

## Lesson 8: try / except 异常处理

学习了异常处理

- try 用来包住可能出错的代码
- except 用来处理错误
- ValueError 是常见的值转换错误
- input（）输入中后的得到是字符串，有可能转化成int 或 float失败
- try / except 可以避免程序因为用户输入错误而直接崩溃

后面做天气查询 CLI工具时，如果用户输入错误、API请求失败，都需要异常处理

## Lesson 9: 文件读写 open（）

学习了python的文件读写

- open（） 可以打开文件
- “w” 是写入模式，运行一次回覆盖旧的内容
- “r” 是读取模式
- “a” 是追加模式，会在文件末尾增加新内容
- encoding = “utf-8” 可以支持中文
- with open（） 可以自动关闭文件

后面做AI工具时，经常会用到读取文档，保存日志，保存API返回结果。

## Lesson 10: pathlib 路径管理

今天学习了pathlib。

- Path 可以更清楚地管理文件路径
- Path“.” 表示当前运行目录
- 可以用 / 来拼接路径
- mkdir（exist_ok = True）可以创建文件夹
- eixst（） 可以判断文件夹或文件是否存在

后面做项目时，会把数据、日志、配置文件，放到不同的文件夹里，而不是全部堆积在根目录下。

## Lesson 11: JSON 数据处理

学习了 python 的 JSON 模块

- JSON 是网络API常见的数据格式
- json.dumps() 可以把 Python 字典转化成 JSON 字符串
- json.loads() 可以把 JSON 字符串转回 Python 字典
- json.dump() 可以把 Python 数据写入 JSON 文件
- json.load() 可以从 JSON文件中读取数据

后面调用天气API 和 AI API 时，经常会处理 JSON数据。

## Lesson 12: requests 网络请求

学习了requests 

- pip install requests 可以安装第三方库
- requests.get(url) 可以向URL 发起 GET请求
- respones.status_code 是响应状态码
- respones.text 是原始文本内容
- respones.json() 可以吧 JSON响应转化成python 数据
- timeout 可以避免请求一直卡住
- response.raise_for_status() 可以检查HTTP 错误

后面的天气查询 CLI 工具会用 requests 调用天气API

## Lesson 13: .env 和环境变量

学习了 .env 和 python-dotenv

- .env用来保存配置和密钥
- python-dotenv 可以用来读取 .env文件
- load_dotenv() 会加载 .env
- os.getenv(“变量名”) 可以读取环境变量
- 从 .env 读出来的默认值是字符串
- .env 不能提交到GitHub，必须写进 .gitignore

后面调用天气API、OpenAI API时，API key会放在 .env里

## Lesson 14:API 请求并保存 JSON

做了一个小整合练习

- 从 .env 读取 TEST_API_URL
- 用 requests.get() 请求 API
- 用 response.json() 把返回结果转换成Python字典
- 用 pathlib 创建 data 文件
- 用 json.dump() 把结果保存成 JSON 文件
- 用 try / except 处理请求异常和 JSON 解析异常

这节课开始接近真实项目流程：读取配置、请求接口、数据处理、保存结果。

#### 今日疑问

1. f-string 是干什么的？
2. age + years_later 为什么能算出 future_age？
3. git push 是把什么推到 GitHub？

#### 答案
f-string 用来把变量放进字符串里，让输出更自然。

age 和 years_later 都是数字，所以可以做加法运算，结果保存到 future_age。

git push 是把本地 commit 过的版本推送到 GitHub 远程仓库。