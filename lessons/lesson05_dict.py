# phase1 - lesson05_dict.py

student = {
    "name":"Nolan",
    "age": 24,
    "city":"Los Angeles",
    "phase":"phase 1",
    "is_learning_ai": True
}

print("=== 学生信息 ===")
print(student)

print("=== 单独读取字段 ===")
print(f"学生姓名：{student['name']}")
print(f"学生年龄：{student['age']}")
print(f"学生所在城市：{student['city']}")
print(f"学生所在阶段：{student['phase']}")
print(f"学生是否在学习AI：{student['is_learning_ai']}")

print("=== 更新学生信息 ===")
student["phase"] = "Phase1 - Python Basic"
student["weekly_hours"] =10

print(f"新的学习阶段：{student['phase']}")
print(f"每周学习小时数：{student['weekly_hours']}")

print("=== 遍历学生信息 ===")
for key,value in student.items():
    print(f"{key}: {value}")

print(" === 模拟天气数据 ===")
weather = {
    "city":"Los Angeles",
    "temperature": 25,
    "condition":"Sunny",
    "humidity": 60
}

print(f"城市：{weather['city']}")
print(f"温度：{weather['temperature']}°C")
print(f"天气状况：{weather['condition']}")
print(f"湿度：{weather['humidity']}%")