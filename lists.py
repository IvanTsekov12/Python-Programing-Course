#list(списък) = съдържа няколко стойности в една променлива

food = ["pizza", "hot dog", "spaghetti", "hamburger"]

food[0] = "sushi"

for i in food:
    print(i)

print()
print("LIST METHODS")
print()
#append --> добавя елемнт в края на списъка
print("APPEND")
food.append("ice cream")
for i in food:
    print(i)
print()
#remove --> премахва даден елемт от списъка
print("REMOVE")
food.remove("hot dog")
for i in food:
    print(i)
print()
#pop --> премахва последният елемент от списъка
print("POP")
food.pop()

print()
#insert --> вмъква елемнт на даден индекс
print("INSERT")
food.insert(0, "cake")
for i in food:
    print(i)
print()
#sort --> сортира списъка по азбучен ред(за стрингове)
print("SORT")
food.sort()
for i in food:
    print(i)
print()
#clear --> премахва всички елемнти от списъка(занулява списъка)
print("CLEAR")
food.clear()
for i in food:
    print(i)
