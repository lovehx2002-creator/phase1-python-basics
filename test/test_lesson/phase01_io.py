file_01 = "log.txt"

#创建一个文件，打日志吧 ”utf-8“支持中文
with open(file_01,"w",encoding="utf-8") as file:
    file.write("这是我自己的第一个测试文件\n")
    file.write("希望能够运行成功\n")

with open("log02.txt","w",encoding="utf-8") as file:
    file.write("测试直接以文件名命\n")
    file.write("我感觉文件出现的位置应该也是终端\n")


#现在来读文件看看
with open("log02.txt","r",encoding="utf-8") as file:
    content = file.read()
print(content)

#现在添加文件，看看会不会覆盖之前文件夹到内容
with open("log02.txt","a",encoding="utf-8") as haha:
    haha.write("这是我更换所谓打开文件夹的名字，并且添加的内容\n")
    
