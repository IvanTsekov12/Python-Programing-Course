#tuple = колекция, която е подредена и не може да се променя,
#        използвана за да групира свързани данни

student = ("Ivan", 18, "male")

#TUPLE METHODS

#count = намира колко пъти се появява дадена стойност
print("COUNT")
print(student.count(18))
print()

#index = намира индекса на дедена стойност
print("INDEX")
print(student.index("male"))
print()

for i in student:
    print(i)

if "Ivan" in student:
    print("Ivan is here")