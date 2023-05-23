# string slicing = създава подстринг, като извлича елементи от друг стринг
#indexing[] или slice()
# [начало:стоп:стъпка]

#PART 1

name = "Ivan Tsekov"

first_name = name[0:4] #[:index]
last_name = name[5:12] #[index:]
name2 = name[0:12:2] #[::index]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(name2)
print(reversed_name)

#PART 2

website = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4)

print(website[slice])
print(website2[slice])