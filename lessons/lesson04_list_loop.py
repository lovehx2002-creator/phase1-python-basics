# Phase1 - Lesson 04 - List and for loop

cities = ["Los Angeles","Tokyo","Singapore","Seoul"]

print("=== 城市列表 ===")

for city in cities:
    print(f"城市：{city}")

print("=== 城市数量 ===")
print(f"城市数量：{len(cities)}")


# 练习append方法
print("=== 添加城市 ===")
cities.append("New York")

for city in cities:
    print(f"城市：{city}")

print(f"城市数量：{len(cities)}")
