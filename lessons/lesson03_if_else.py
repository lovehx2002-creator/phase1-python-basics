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