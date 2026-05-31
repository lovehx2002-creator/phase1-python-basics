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

print("===== 每周学习时间计算 =====")

hours_per_day = 2
days_per_week = 5
weekly_hours = hours_per_day * days_per_week

print(f"我每天学习 {hours_per_day} 小时")
print(f"我每周学习 {weekly_hours} 小时")
print(f"所以我每周大学学习{weekly_hours} 小时")