# Phase 1 - Lesson 8 - try except

age_text = input("请输入你的年龄：")

try:
    age = int(age_text)
    print(f"你的年龄是：{age}岁！")
    print(f"5年后你将会是{age + 5}岁！")
except ValueError:
    print("输入的年龄无效，请输入一个有效的数字。")

print("=== 计算器 ===")
hours_text = input("你每天学习几小时？")
days_text = input("你每周学习几天？")

try:
    hours_per_day = float(hours_text)
    days_per_week = float(days_text)

    def total(hours_per_day, days_per_week):
        total_hours = hours_per_day * days_per_week
        return total_hours

    week_hours = total(hours_per_day, days_per_week)
    print(f"你每周学习{week_hours}小时！")
except ValueError:
    print("输入的学习时间无效，请输入有效的数字。")

if week_hours > 20:
    print("你学习的时间太多了，要注意休息哦！")
elif week_hours < 5:
    print("你学习的时间太少了，要加油哦！")
else:
    print("你的学习时间很合理，继续保持！")