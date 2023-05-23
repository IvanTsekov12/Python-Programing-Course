#dictionary = колекция, която е неподредена, може да се променя, изградена от уникални ключове:двойки стойности
#             Бързо, защото използва хашване, позволява ни бързо да достъпим стойност

capitals = {'USA':"Washington DC", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow"}

#print(capitals['Russia'])
#get - проверява библиотеката за даден ключ. Ако го има - връща стойността му, ако не - връща None
print('GET METHOD')
print(capitals.get('Germany'))
print()

#keys - връща ключовета на библиотеката
print('KEYS METHOD')
print(capitals.keys())
print()

#values - връща стойностите на библиотеката
print('VALUES METHOD')
print(capitals.values())
print()

#items - връща всички елемнти в библиотеката
print('ITEMS METHOD')
print(capitals.items())
print()

for key,values in capitals.items():
    print(key, values)
print()

#update - добавя или променя елемнти в библиотеката
print('UPDATE METHOD')
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
for key,values in capitals.items():
    print(key, values)
print()

#pop - премахва елемнти от библиотеката
print('POP METHOD')
capitals.pop('China')
for key,values in capitals.items():
    print(key, values)
print()

#clear - премахва всички елемнти от библиотеката
print('CLEAR METHOD')
capitals.clear()
for key,values in capitals.items():
    print(key, values)
print()
