# Phase1 - Lesson 10: pathlib

from pathlib import Path

project_root = Path(".")
data_folder = project_root / "data"
log_file = data_folder / "study_log.txt"
log = data_folder / "log.txt"

print("=== 路径信息 ===")
print(f"项目根目录: {project_root}")
print(f"数据文件夹: {data_folder}")
print(f"日志文件: {log_file}")


print("==== 创建 data 文件夹 ====")
data_folder.mkdir(exist_ok=True)
print("data 文件夹已经准备好。")

print("==== 写入日志文件 ====")
with open(log_file,"w",encoding="utf-8") as file:
    file.write("这是保存在data文件夹里的学习日志。\n")
    file.write("今天学习了pathlib模块，文件管理路径。\n")

print("日志文件写入完成。")

print("==== 读取日志文件 ====")
with open(log_file,"r",encoding="utf-8") as file:
    content = file.read()
print(content)

print("===== 判断文件是否存在 =====")
if log_file.exists():
    print(f"{log_file} 文件存在。")
else:
    print(f"{log_file} 文件不存在。")

if log.exists():
    print(f"{log} 文件存在。")
else:    print(f"{log} 文件不存在。")

