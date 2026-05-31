print("hello,Phase 1 python!")

# phase 1 ——lesson 1：Variables and Data Types

name = "Nolan"
age = 24
height = 1.75
is_learing_ai = True

print("我的名字是："+name)
print("我的年龄是："+str(age))
print("我的身高是："+str(height))
print("我正在学习人工智能吗？" , is_learing_ai) 


print(type(name))
print(type(age))
print(type(height))
print(type(is_learing_ai))

# Phase 1 ——lesson 2：String，number，and f-strings

print("===== 每周学习时间计算 =====")

hours_per_day = 2
days_per_week = 5
weekly_hours = hours_per_day * days_per_week

print(f"我每天学习 {hours_per_day} 小时")
print(f"我每周学习 {weekly_hours} 小时")
print(f"所以我每周大学学习{weekly_hours} 小时")

# Phase 1 ——Lesson 3:if / elif / else

name = "Nolan"
daily_study_hours = 2

print("===== AI 全栈学习进度判断 =====")
print(f"{name} 今天计划学习 {daily_study_hours} 小时")
if daily_study_hours >= 3:
    print("今天学习强度很高，今天很猛")
elif daily_study_hours >= 2:
    print("今天学习强度适中，继续保持")
elif daily_study_hours >= 0:
    print("今天学习强度较低，建议增加学习时间")
else:
    print("今天还没开始学习，至少打开vscode写十分钟吧")



print("===== git提交进度 =====")

has_committed_today= True

if has_committed_today:
    print("今天已经提交了代码，继续保持！")
else:
    print("今天还没有提交代码，记得及时提交哦！")