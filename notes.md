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


#### 今日疑问

1. f-string 是干什么的？
2. age + years_later 为什么能算出 future_age？
3. git push 是把什么推到 GitHub？

#### 答案
f-string 用来把变量放进字符串里，让输出更自然。

age 和 years_later 都是数字，所以可以做加法运算，结果保存到 future_age。

git push 是把本地 commit 过的版本推送到 GitHub 远程仓库。