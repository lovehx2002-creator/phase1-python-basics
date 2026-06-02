file_path = "study_log.txt"

with open(file_path,"w",encoding="utf-8") as file:
    file.write("今天学习了Python的文件输入输出操作。\n")
    file.write("我正在学习AI全栈工程师线路。\n")
    file.write("这是程序写入的内容。\n")
   

print("文件写入完成")

print("=== 读取文件内容 ===")
with open(file_path,"r",encoding="utf-8") as file:
    content = file.read()

print(content)

print("=== 追加内容到文件 ===")
with open(file_path,"a",encoding="utf-8") as file:
    file.write("这一行是后来追加的内容。\n")

with open(file_path,"r",encoding="utf-8") as file:
    updated_content = file.read()

print(updated_content)

print("==== 简单学习记录器 ====")

lesson_name = input("请输入今天的课程名称：")
summary = input("请输入今天的学习总结：")

with open(file_path,"a",encoding = "utf-8") as file:
    file.write("\n=== 新学习记录 ===\n")
    file.write(f"课程：{lesson_name}\n")
    file.write(f"总结：{summary}\n")

print("学习记录已保存。")

with open(file_path,"r",encoding = "utf-8") as file:
    final_content = file.read()
print(final_content)
