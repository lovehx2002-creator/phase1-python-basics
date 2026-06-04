from pathlib import Path

#先给跟目录命名
project_root = Path(".")

#创建新的文件夹 （其实确定文件夹路径，文件夹还没有创建）
data_folder = project_root / "data"

#创建新的文件 （路径下确定文件）
log_file = data_folder / "log.txt"

print("路径信息")
print(f"根目录：{project_root}")
print(f"文件夹：{data_folder}")
print(f"日志文件：{log_file}")

data_folder.mkdir(exist_ok=True)

with open(log_file,"w",encoding="utf-8") as file:
    file.write("这个是新根据分类下写的目录文件\n")
    file.write("看一看会不会成功")

with open(log_file,"r",encoding="utf-8") as haha:
    content = haha.read()

print(content)

file_loader = Path("./data02")
file_loader.mkdir(exist_ok=True)

wenjian = file_loader / "log.txt"

with open(wenjian,"w",encoding="utf-8") as haha:
    haha.write("看一看这样行不行")
