# Phase 1 - Lesson 7: input and type conversion

name = input("请输入你的名字：")
city = input("请输入你所在的城市：")
age_text = input("请输入你的年龄：")

age = int(age_text)
futere_age = age + 5

print("=== 用户信息 ===")
print(f"名字：{name}")
print(f"你现在在，城市：{city}学习AI全栈")
print(f"你现在的年龄是：{age}，5年后你将会是{futere_age}岁！")

print("=== 计算器 ===")
hours_text = input("你每天学习几小时？")
days_text = input("你每周学习几天？")

hours_per_day = float(hours_text)
days_per_week = float(days_text)

def total(hours_per_day,days_per_week):
    total_hours = hours_per_day * days_per_week
    return total_hours

week_hours = total(hours_per_day,days_per_week)
print(f"你每周学习{week_hours}小时！")