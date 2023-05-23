#set = колекция, която не е подредена, не е индексирана. Стойностите не се дублират

untesils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

for i in untesils:
    print(i)

print()
print("SET METHODS")
print()

#add = добавя елемнт в сета
print('ADD')
untesils.add("napkin")
for i in untesils:
    print(i)
print()

#remove = премахва елемент от сета
print('REMOVE')
untesils.remove("fork")
for i in untesils:
    print(i)
print()

#clear = премахва всички елемнти от сета
# print('CLEAR')
# untesils.clear()
# for i in untesils:
#     print(i)
# print()

#update = добавя стойностите на един сет в друг
# print('UPDATE')
# untesils.update(dishes)
# for i in untesils:
#     print(i)
# print()

#union = дава стойностите на два сета в нов, трети сет
print('UNION')
dinner_table = untesils.union(dishes)
for i in dinner_table:
    print(i)
print()

#difference = намира разликите в два сета
print('DIFFERENCE')
dishes.add("knife")
print(untesils.difference(dishes))
print()

#intersection = намира приликите в два сета
print('INTERSECTION')
print(untesils.intersection(dishes))
print()