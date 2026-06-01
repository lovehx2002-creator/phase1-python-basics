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

#### 今日疑问

1. f-string 是干什么的？
2. age + years_later 为什么能算出 future_age？
3. git push 是把什么推到 GitHub？

#### 答案
f-string 用来把变量放进字符串里，让输出更自然。

age 和 years_later 都是数字，所以可以做加法运算，结果保存到 future_age。

git push 是把本地 commit 过的版本推送到 GitHub 远程仓库。